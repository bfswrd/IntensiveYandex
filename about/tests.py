from django.test import Client, TestCase


class AboutURLTests(TestCase):
    # Check homepage endpoint
    def test_about_endpoint(self):
        response = Client().get(path="/about/")
        self.assertEqual(response.status_code, 200)
