from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from authentication.models import UserProfile


class UserRegisterTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testUser',
            'email': 'test@gmail.com',
            'password': 'secret123$%',
            'groups': '2',
        }

    def test_valid_register(self):
        response = self.client.post(reverse("authentication:register"), **self.credentials)
        user_exists = get_user_model().objects.filter(username=self.credentials["username"]).exists()
        self.assertTrue(user_exists)
        self.assertTrue(response.status_code, 200)

    def test_register_duplicated_username(self):
        self.test_valid_register(self)
        self.credentials["email"] = "diffrenetEmail@gmail.com"
        response = self.client.post(reverse("authentication:register"), **self.credentials)
        self.assertTrue(response.status_code, 400)

    def test_register_duplicated_email(self):
        self.test_valid_register(self)
        self.credentials["username"] = "differentUsername"
        response = self.client.post(reverse("authentication:register"), **self.credentials)
        self.assertTrue(response.status_code, 400)

    def test_user_profile_created_after_register(self):
        self.test_valid_register(self)
        registered_user = get_user_model().objects.get(username=self.credentials["username"])
        registered_user_profile_exists = UserProfile.objects.filter(user=registered_user).exists()
        self.assertTrue(registered_user_profile_exists)


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testUser',
            'password': 'secret123$%'}
        get_user_model().objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post(reverse("authentication:login"), **self.credentials)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_login_with_invalid_password(self):
        self.credentials["password"] = "wrongPassword"
        response = self.client.post(reverse("authentication:login"), **self.credentials)
        self.assertFalse(response.context['user'].is_authenticated)

    def test_login_with_nonexistent_username(self):
        self.credentials["username"] = "imaginaryUsername"
        response = self.client.post(reverse("authentication:login"), **self.credentials)
        self.assertFalse(response.context['user'].is_authenticated)


class UserProfileTest(TestCase):
    def setUp(self):

        self.credentials = {
            'username': 'testUser',
            'password': 'secret123$%'
        }
        # the UserProfile gets created automatically when a user is created (tested in UserRegisterTest)
        get_user_model().objects.create_user(**self.credentials)

    # needs image upload preparations
    def change_profile_avatar_test(self):
        return self.assertTrue(True)
