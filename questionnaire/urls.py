from django.urls import path
from rest_framework.routers import SimpleRouter

from questionnaire.views import QuestionnaireViewSet, \
    QuestionnaireFieldCreate, QuestionnaireFieldDetail

router = SimpleRouter()
router.register('questionnaires', QuestionnaireViewSet)

urlpatterns = [
    path('questionnaire-fields/', QuestionnaireFieldCreate.as_view(),
         name='questionnairefield-list'),
    path('questionnaire-fields/<pk>/', QuestionnaireFieldDetail.as_view(),
         name='questionnairefield-detail')
]
urlpatterns += router.urls
