from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView, \
    CreateAPIView, ListCreateAPIView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from questionnaire.models import Questionnaire, QuestionnaireField, \
    QuestionnaireAnswer
from questionnaire.serializers import QuestionnaireSerializer, \
    QuestionnaireFieldSerializer, QuestionnaireAnswerSerializer


class IsSelfOrAdminToUpdateOrDelete(permissions.BasePermission):
    message = "The user profile can be edited only by this user " \
              "or site administrator."

    def has_object_permission(self, request, view, questionnaire):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user and (questionnaire.author == request.user
                             or request.user.is_staff):
            return True
        return False


class QuestionnaireViewSet(ModelViewSet):
    serializer_class = QuestionnaireSerializer
    queryset = Questionnaire.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsSelfOrAdminToUpdateOrDelete)


class QuestionnaireFieldCreate(CreateAPIView):
    queryset = QuestionnaireField.objects.all()
    serializer_class = QuestionnaireFieldSerializer


class QuestionnaireFieldDetail(RetrieveUpdateDestroyAPIView):
    queryset = QuestionnaireField.objects.all()
    serializer_class = QuestionnaireFieldSerializer


class QuestionnaireAnswerListCreate(ListCreateAPIView):
    queryset = QuestionnaireAnswer.objects.all()
    serializer_class = QuestionnaireAnswerSerializer
