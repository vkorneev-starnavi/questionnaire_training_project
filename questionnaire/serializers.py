from rest_framework.serializers import HyperlinkedModelSerializer
from questionnaire.models import Questionnaire


class QuestionnaireSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('url', 'id', 'author', 'description', 'created_at')
        read_only_fields = ('created_at',)
