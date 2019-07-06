from django.urls import path
from rest_framework.routers import SimpleRouter

from questionnaire.views import QuestionnaireViewSet, \
    QuestionnaireFieldCreate, QuestionnaireFieldDetail, \
    QuestionnaireAnswerListCreate

router = SimpleRouter()
router.register('questionnaires', QuestionnaireViewSet)

urlpatterns = [
    path('questionnaire-fields/', QuestionnaireFieldCreate.as_view(),
         name='questionnairefield-list'),
    path('questionnaire-fields/<pk>/', QuestionnaireFieldDetail.as_view(),
         name='questionnairefield-detail'),
    path('questionnaire-answers/', QuestionnaireAnswerListCreate.as_view(),
         name='questionnaireanswer-list')
]
urlpatterns += router.urls
