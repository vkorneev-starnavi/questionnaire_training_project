from rest_framework.serializers import HyperlinkedModelSerializer
from questionnaire.models import Questionnaire, QuestionnaireField


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
