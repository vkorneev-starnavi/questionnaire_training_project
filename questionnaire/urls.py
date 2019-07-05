from rest_framework.routers import SimpleRouter
from questionnaire.views import QuestionnaireViewSet

router = SimpleRouter()
router.register('questionnaires', QuestionnaireViewSet)
urlpatterns = router.urls
