from rest_framework.serializers import HyperlinkedModelSerializer, \
    ModelSerializer, CharField
from questionnaire.models import Questionnaire, QuestionnaireField, \
    FieldValue


class QuestionnaireFieldSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = QuestionnaireField
        fields = ('url', 'id', 'questionnaire', 'position', 'field_type',
                  'text_before', 'text_after', 'default_val', 'min_val',
                  'max_val')


class QuestionnaireSerializer(HyperlinkedModelSerializer):
    fields = QuestionnaireFieldSerializer(many=True, read_only=True)

    class Meta:
        model = Questionnaire
        fields = ('url', 'id', 'author', 'description', 'fields', 'created_at')
        read_only_fields = ('created_at',)


class FieldValueSerializer(ModelSerializer):
    value = CharField(max_length=255, required=False)

    class Meta:
        model = FieldValue
        fields = ('id', 'field', 'value')

    def validate(self, data):
        field = data['field']
        if 'value' not in data:
            data['value'] = field.default_val
        return data
