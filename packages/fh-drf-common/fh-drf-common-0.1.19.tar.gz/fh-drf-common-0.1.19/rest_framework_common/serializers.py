import re

from django_enumfield import enum
from rest_framework import serializers
from rest_framework.utils.field_mapping import get_field_kwargs, ClassLookupDict
import base32_crockford


class Base32CrockfordField(serializers.CharField):

    def to_internal_value(self, data):
        data = super(Base32CrockfordField, self).to_internal_value(data)
        try:
            return base32_crockford.normalize(data)
        except ValueError:
            raise serializers.ValidationError('Invalid {}'.format(self.source))


class USPhoneNumberField(serializers.CharField):

    def to_internal_value(self, data):
        data = re.sub('[^0-9]', '', data)
        data_length = len(data)

        if 10 > data_length > 11:
            raise serializers.ValidationError('The {} should be 10 to 11 numbers in length.'.format(self.source))

        # Prepend the country code
        if data_length == 10:
            data = '+1{}'.format(data)
        else:
            data = '+{}'.format(data)

        return data


class DateTimeSerializerMixin(serializers.Serializer):

    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


class PrimaryKeyMixin(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)


class WritableIDSerializer(serializers.Serializer):
    id = serializers.CharField()


class ObjectWithIDSerializer(serializers.Serializer):
    id = serializers.CharField()


class EnumField(serializers.ChoiceField):
    """ A field that takes a field's value as the key and returns
    the associated value for serialization """
    def __init__(self, choices, *args, **kwargs):
        self.representations = {}
        self.internal_values = {}

        for k, v in choices:
            if v in self.internal_values:
                raise ValueError(
                    'The field is not deserializable with the given choices.'
                    ' Please ensure that choices map 1:1 with values'
                )
            self.internal_values[v.name] = k
            self.representations[k] = v.name

        super(EnumField, self).__init__(self.internal_values, **kwargs)

    def to_internal_value(self, data):
        res = super(EnumField, self).to_internal_value(data)
        return self.internal_values.get(data) if res else 3

    def to_representation(self, value):
        return self.representations.get(value)


class FileProxyURLField(serializers.Field):
    """
    Allows you to proxy through services like Imgix back to where your original file storage location is.

    Mostly just wraps up replacing the URL returned with the proper domain (proxy's domain), and stripping out any
    path prefix if necessary incase your proxy is setup to dive deeper by default.
    """

    def __init__(self, proxy_base_url, strip_prefix=None, *args, **kwargs):
        self.proxy_base_url = proxy_base_url
        self.strip_prefix = strip_prefix
        super(FileProxyURLField, self).__init__(*args, **kwargs)

    def to_representation(self, file):
        # Handle local tests/fixtures that store the URL to an image on randomuser.me
        # Get storage and remove base_url to test
        if file:
            base_filepath = file.url.replace(file.storage.base_url, '')
        else:
            return None

        if base_filepath.startswith('http'):
            url = base_filepath
        else:
            if self.proxy_base_url:
                if self.strip_prefix:
                    base_filepath = base_filepath.replace('{}/'.format(self.strip_prefix), '')
                url = '{}{}'.format(self.proxy_base_url, base_filepath)
            else:
                url = file.url
                request = self.context.get('request', None)
                if request is not None:
                    url = request.build_absolute_uri(url)

        return url


class Serializer(PrimaryKeyMixin, serializers.Serializer):

    def __init__(self, *args, **kwargs):
        nested_write = kwargs.pop('nested_write', False)
        if nested_write:
            for k, field in self.fields.items():
                if field.field_name == 'id':
                    field.read_only = False
                else:
                    field.read_only = True
        super(Serializer, self).__init__(*args, **kwargs)

    def build_standard_field(self, field_name, model_field):
        field_mapping = ClassLookupDict(self.serializer_field_mapping)

        field_class = field_mapping[model_field]
        field_kwargs = get_field_kwargs(field_name, model_field)

        if not issubclass(field_class, serializers.ModelField):
            # `model_field` is only valid for the fallback case of
            # `ModelField`, which is used when no other typed field
            # matched to the model field.
            field_kwargs.pop('model_field', None)

        if field_class == EnumField:
            return field_class, field_kwargs
        else:
            return super(Serializer, self).build_standard_field(field_name, model_field)


class ModelSerializer(PrimaryKeyMixin, serializers.ModelSerializer):
    serializer_field_mapping = serializers.ModelSerializer.serializer_field_mapping
    serializer_field_mapping[enum.EnumField] = EnumField

    def __init__(self, *args, **kwargs):
        nested_write = kwargs.pop('nested_write', False)
        if nested_write:
            for k, field in self.fields.items():
                if field.field_name == 'id':
                    field.read_only = False
                else:
                    field.read_only = True
        super(ModelSerializer, self).__init__(*args, **kwargs)

    def get_default_field_names(self, declared_fields, model_info):
        """
        Return the default list of field names that will be used if the
        `Meta.fields` option is not specified.
        """
        return (
            [model_info.pk.name] +
            [self.url_field_name] +
            list(declared_fields.keys()) +
            list(model_info.fields.keys()) +
            list(model_info.forward_relations.keys())
        )

    def build_standard_field(self, field_name, model_field):
        field_mapping = ClassLookupDict(self.serializer_field_mapping)

        field_class = field_mapping[model_field]
        field_kwargs = get_field_kwargs(field_name, model_field)

        if not issubclass(field_class, serializers.ModelField):
            # `model_field` is only valid for the fallback case of
            # `ModelField`, which is used when no other typed field
            # matched to the model field.
            field_kwargs.pop('model_field', None)

        if field_class == EnumField:
            return field_class, field_kwargs
        else:
            return super(ModelSerializer, self).build_standard_field(field_name, model_field)


class HyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    serializer_field_mapping = serializers.HyperlinkedModelSerializer.serializer_field_mapping
    serializer_field_mapping[enum.EnumField] = EnumField

    def build_standard_field(self, field_name, model_field):
        field_mapping = ClassLookupDict(self.serializer_field_mapping)

        field_class = field_mapping[model_field]
        field_kwargs = get_field_kwargs(field_name, model_field)

        if not issubclass(field_class, serializers.ModelField):
            # `model_field` is only valid for the fallback case of
            # `ModelField`, which is used when no other typed field
            # matched to the model field.
            field_kwargs.pop('model_field', None)

        if field_class == EnumField:
            return field_class, field_kwargs
        else:
            return super(HyperlinkedModelSerializer, self).build_standard_field(field_name, model_field)
