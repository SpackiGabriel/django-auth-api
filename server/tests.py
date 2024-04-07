from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class VerifyViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

    def test_verify_authenticated_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        response = self.client.get('/verify/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'User is authenticated')
        self.assertEqual(response.data['user']['username'], self.user.username)

        print("\nAuthentication Test: User is authenticated.")
        print("User details retrieved successfully.")

    def test_verify_unauthenticated_user(self):
        response = self.client.get('/verify/')
        
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')
        
        print("\nUnauthenticated Test: No authentication credentials provided.")
