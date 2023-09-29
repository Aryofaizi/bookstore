from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class SignUpTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test user",
            email="test email",
            password="test password",
        )

    def test_signup_url_by_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_signup_url(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view(self):
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.user.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.user.email)


