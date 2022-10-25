from django.test import Client, TestCase


class CatalogURLTests(TestCase):
    # Check catalog endpoint
    def test_catalog_endpoint(self):
        response = Client().get(path="/catalog/")
        self.assertEqual(response.status_code, 200)

    # Check catalog items endpoint
    def test_catalog_item_endpoint(self):
        _TESTS = (
            ("/catalog/123/", 200),  # Digit > 0
            ("/catalog/0/", 404),  # Digit = 0
            ("/catalog/-123/", 404),  # Digit < 0
            ("/catalog/1.23/", 404),  # Digit with dot
            ("/catalog/str/", 404),  # Str
            ("/catalog/str123/", 404),  # Str + Int
            ("/catalog/123str/", 404),  # Int + Str
        )
        for path, status_code in _TESTS:
            with self.subTest(item=(path, status_code)):
                response = Client().get(path=path)
                self.assertEqual(response.status_code, status_code)
