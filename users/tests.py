from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from users.models import User


class UserViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_can_register_user_with_email(self):
        user_data = {'username': 'test', 'password': 'test',
                     'email': 'test@email.com'}
        r = self.client.post(reverse('user-list'), user_data)
        assert r.status_code == 201

        # shouldn't raise DoesNotExist
        User.objects.get(username=user_data['username'])

    def test_can_register_user_without_email(self):
        user_data = {'username': 'test', 'password': 'test'}
        r = self.client.post(reverse('user-list'), user_data)
        assert r.status_code == 201

        # shouldn't raise DoesNotExist
        User.objects.get(username=user_data['username'])
