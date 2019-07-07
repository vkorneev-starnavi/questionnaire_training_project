from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from questionnaire.models import Questionnaire
from users.models import User


class QuestionnaireTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.users = [
            User.objects.create_user(username='test1', password='test1',
                                     email='test1@email.com')
        ]

    def test_user_can_create_questionnaire(self):
        user_url = reverse('user-detail', kwargs={'pk': self.users[0].id})
        questionnaire_data = {'author': user_url, 'description': 'Test'}
        r = self.client.post(reverse('questionnaire-list'), questionnaire_data)

        assert r.status_code == 201
        Questionnaire.objects.get(pk=r.json()['id'])  # shouldn't raise
