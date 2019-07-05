from rest_framework.serializers import HyperlinkedModelSerializer
from questionnaire.models import Questionnaire, QuestionnaireField


class QuestionnaireSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('url', 'id', 'author', 'description', 'created_at')
        read_only_fields = ('created_at',)


class QuestionnaireFieldSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = QuestionnaireField
        fields = ('url', 'id', 'questionnaire', 'position', 'field_type',
                  'text_before', 'text_after', 'default_val', 'min_val',
                  'max_val')
