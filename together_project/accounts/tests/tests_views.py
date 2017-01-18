from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from accounts.models import User


class BaseTestCase(APITestCase):

    def setUp(self):

        # Create a user
        self.email = 'testuser@test.com'
        self.username = 'testuser'
        self.password = 'cacacaca'
        self.user = User.objects.create_user(
            self.username, self.email, self.password)

        # Login data
        self.data = {
            'username': self.username,
            'password': self.password
        }

        # Set headers that will be included on all subsequent requests
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.get_token())

    def get_token(self):
        url = reverse('api_token_auth')
        response = self.client.post(url, self.data, format='json')
        return response.data['token']


class AccountTests(BaseTestCase):

    def test_api_user_list(self):
        url = reverse('api_user_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
