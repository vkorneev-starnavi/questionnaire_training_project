from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView


from questionnaire.models import Questionnaire, QuestionnaireField
from questionnaire.serializers import QuestionnaireSerializer, \
    QuestionnaireFieldSerializer


class QuestionnaireViewSet(ModelViewSet):
    serializer_class = QuestionnaireSerializer
    queryset = Questionnaire.objects.all()


class QuestionnaireFieldCreate(CreateAPIView):
    queryset = QuestionnaireField.objects.all()
    serializer_class = QuestionnaireFieldSerializer


class QuestionnaireFieldDetail(RetrieveUpdateDestroyAPIView):
    queryset = QuestionnaireField.objects.all()
    serializer_class = QuestionnaireFieldSerializer
