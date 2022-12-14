from django.shortcuts import reverse
from django.test import TestCase

from catalog.models import Category, Item, Tag


class CatalogURLTests(TestCase):
    # Check catalog endpoint
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(name="Тест1", slug="test_1")
        cls.tag = Tag.objects.create(name="Тест1", slug="test_1")
        cls.item = Item(
            name="Позитивный",
            text="Роскошно",
            category=Category.objects.get(id=1),
        )
        cls.item.full_clean()
        cls.item.save()
        cls.item.tags.add(Tag.objects.get(id=1))
        cls.item.save()

    def test_catalog_endpoint(self):
        response = self.client.get(path="/catalog/")
        self.assertEqual(response.status_code, 200)

    # Check catalog items endpoint
    def test_catalog_item_endpoint(self):
        _TESTS = (
            ("/catalog/1/", 200),  # Digit > 0
            ("/catalog/0/", 404),  # Digit = 0
            ("/catalog/-123/", 404),  # Digit < 0
            ("/catalog/1.23/", 404),  # Digit with dot
            ("/catalog/str/", 404),  # Str
            ("/catalog/str123/", 404),  # Str + Int
            ("/catalog/123str/", 404),  # Int + Str
        )
        for path, status_code in _TESTS:
            with self.subTest(item=(path, status_code)):
                response = self.client.get(path=path)
                self.assertEqual(response.status_code, status_code)


class TaskPageTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(name="Тест1", slug="test_1")
        cls.tag = Tag.objects.create(name="Тест1", slug="test_1")
        cls.item = Item(
            name="Позитивный",
            text="Роскошно",
            category=Category.objects.get(id=1),
        )
        cls.item.full_clean()
        cls.item.save()
        cls.item.tags.add(Tag.objects.get(id=1))
        cls.item.save()

    def test_home_page_show_correct_context(self):
        response = self.client.get(reverse("homepage:home"))
        self.assertIn("items", response.context)
        self.assertEqual(len(response.context["items"]), 0)

    def test_item_list_page_show_correct_context(self):
        response = self.client.get(reverse("catalog:item_list"))
        self.assertIn("items", response.context)
        self.assertEqual(len(response.context["items"]), 1)

    def test_item_detail_page_show_correct_context(self):
        response = self.client.get(reverse("catalog:item_detail",
                                           kwargs={"pk": 1}))
        self.assertIn("item", response.context)
        self.assertEqual(response.context["item"], Item.objects.get(pk=1))
