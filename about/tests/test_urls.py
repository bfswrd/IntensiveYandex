from django.test import TestCase


class AboutURLTests(TestCase):
    # Check homepage endpoint
    def test_about_endpoint(self):
        response = self.client.get(path="/about/")
        self.assertEqual(response.status_code, 200)
