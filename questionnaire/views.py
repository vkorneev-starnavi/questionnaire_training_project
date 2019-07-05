from rest_framework.viewsets import ModelViewSet

from questionnaire.models import Questionnaire
from questionnaire.serializers import QuestionnaireSerializer


class QuestionnaireViewSet(ModelViewSet):
    serializer_class = QuestionnaireSerializer
    queryset = Questionnaire.objects.all()
