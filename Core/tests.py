from datetime import date

from django.test import TestCase

from users.models import User


class BirthdayContextProcessorTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(
            first_name="Test", last_name="User",
            email="test_user@gmail.com", birthday=date.today())

    def test_birthday_users_set_in_context(self):
        response = self.client.get('/')

        self.assertIn("birthday_users", response.context)
        self.assertIsNotNone(response.context["birthday_users"])
