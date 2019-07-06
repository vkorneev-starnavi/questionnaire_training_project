from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView, \
    CreateAPIView, ListCreateAPIView


from questionnaire.models import Questionnaire, QuestionnaireField, \
    QuestionnaireAnswer
from questionnaire.serializers import QuestionnaireSerializer, \
    QuestionnaireFieldSerializer, QuestionnaireAnswerSerializer


class QuestionnaireViewSet(ModelViewSet):
    serializer_class = QuestionnaireSerializer
    queryset = Questionnaire.objects.all()


class QuestionnaireFieldCreate(CreateAPIView):
    queryset = QuestionnaireField.objects.all()
    serializer_class = QuestionnaireFieldSerializer


class QuestionnaireFieldDetail(RetrieveUpdateDestroyAPIView):
    queryset = QuestionnaireField.objects.all()
    serializer_class = QuestionnaireFieldSerializer


class QuestionnaireAnswerListCreate(ListCreateAPIView):
    queryset = QuestionnaireAnswer.objects.all()
    serializer_class = QuestionnaireAnswerSerializer
