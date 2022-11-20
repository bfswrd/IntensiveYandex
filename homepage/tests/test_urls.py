from django.test import TestCase


class HomepageURLTests(TestCase):
    # Check homepage endpoint
    def test_homepage_endpoint(self):
        response = self.client.get(path="/")
        self.assertEqual(response.status_code, 200)
