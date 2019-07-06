from rest_framework.serializers import HyperlinkedModelSerializer, \
    ModelSerializer, CharField
from questionnaire.models import Questionnaire, QuestionnaireField, \
    FieldValue, QuestionnaireAnswer


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


class QuestionnaireAnswerSerializer(HyperlinkedModelSerializer):
    field_values = FieldValueSerializer(many=True)

    class Meta:
        model = QuestionnaireAnswer
        fields = ('questionnaire', 'respondent', 'field_values')

    def create(self, validated_data):
        values = validated_data.pop('field_values')
        answer = QuestionnaireAnswer.objects.create(**validated_data)
        for val in values:
            FieldValue.objects.create(answer=answer, **val)
        return answer
