from django.test import Client, TestCase


class HomepageURLTests(TestCase):
    # Check homepage endpoint
    def test_homepage_endpoint(self):
        response = Client().get(path="/")
        self.assertEqual(response.status_code, 200)
