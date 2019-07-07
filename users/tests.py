from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from users.models import User


class UserViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        user1 = User.objects.create_user('test1', email='test1@email.com',
                                         password='test1')
        user1.raw_password = 'test1'
        user2 = User.objects.create_user('test2', email='test2@email.com',
                                         password='test2')
        user2.raw_password = 'test2'
        self.users = (user1, user2)

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

    def test_user_can_change_his_email(self):
        user = self.users[0]
        user_path = reverse('user-detail', kwargs={'pk': user.id})

        r = self.client.get(user_path)
        self.assertEqual(r.json()['email'], user.email)

        auth = get_authorization_header(self.client, user)
        r = self.client.patch(user_path, {'email': 'new_email@email.com'}, **auth)
        self.assertEqual(r.status_code, 200)

        del user.email
        self.assertEqual(user.email, 'new_email@email.com')

    def test_user_cant_change_anothers_email(self):
        user1 = self.users[0]
        user1_path = reverse('user-detail', kwargs={'pk': user1.id})
        r = self.client.get(user1_path)
        self.assertEqual(user1.email, r.json()['email'])

        user2 = self.users[1]
        auth = get_authorization_header(self.client, user2)
        bad_email = 'new_bad_email@email.com'
        r = self.client.patch(user1_path, {'email': bad_email}, **auth)
        self.assertEqual(r.status_code, 403)

        del user1.email
        self.assertNotEqual(user1.email, bad_email)


def get_authorization_header(client, user):
    """Get authorization header for user using the passed client."""
    # obtain authorization token
    response = client.post(
        reverse('token-obtain'),
        {'username': user.username, 'password': user.raw_password}
    )
    token = response.json()['access']
    return {'HTTP_AUTHORIZATION': f'Bearer {token}'}
