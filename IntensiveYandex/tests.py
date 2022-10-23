from django.test import Client, TestCase


class CatalogURLTests(TestCase):
    # Check not correct endpoint
    def test_catalog_endpoint(self):
        response = Client().get(path="/qwerty/")
        self.assertEqual(response.status_code, 404)