from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test whether creating a user with an email ID is successful"""
        email = "recipe_chef@myapp.com"
        password = "test123"
        user = get_user_model().objects.create_user(
            username=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
