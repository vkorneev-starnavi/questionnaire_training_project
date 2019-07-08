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
                                     email='test1@email.com'),
            User.objects.create_user(username='test2', password='test2',
                                     email='test2@email.com')
        ]

    def test_unauthenticated_user_cant_create_questionnaire(self):
        user_url = reverse('user-detail', kwargs={'pk': self.users[0].id})
        questionnaire_data = {'author': user_url, 'description': 'Test'}
        r = self.client.post(reverse('questionnaire-list'), questionnaire_data)
        self.assertEqual(r.status_code, 401)

    def test_user_can_create_questionnaire(self):
        user_url = reverse('user-detail', kwargs={'pk': self.users[0].id})
        questionnaire_data = {'author': user_url, 'description': 'Test'}

        self.client.force_authenticate(self.users[0])
        r = self.client.post(reverse('questionnaire-list'), questionnaire_data)
        self.assertEqual(r.status_code, 201)
        Questionnaire.objects.get(pk=r.json()['id'])  # shouldn't raise

    def test_user_cant_update_not_his_questionnaire(self):
        user1_url = reverse('user-detail', kwargs={'pk': self.users[0].id})
        questionnaire_data = {'author': user1_url, 'description': 'Test'}

        # user1 creates new questionnaire
        self.client.force_authenticate(self.users[0])
        r = self.client.post(reverse('questionnaire-list'), questionnaire_data)
        self.assertEqual(r.status_code, 201)

        # user2 tries to change it
        questionnaire_url = reverse('questionnaire-detail',
                                    kwargs={'pk': r.json()['id']})
        self.client.force_authenticate(self.users[1])
        r = self.client.patch(questionnaire_url, {'description': 'Bad data'})
        self.assertEqual(r.status_code, 403)

