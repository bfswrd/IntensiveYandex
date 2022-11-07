from django.core.exceptions import ValidationError
from django.test import TestCase

from catalog.models import Item, Category, Tag


class ItemModelsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(name="Тест1", slug="test_1")
        cls.tag = Tag.objects.create(name="Тест1", slug="test_1")

    def testTextNegativeValidators(self):
        _TESTS = (
            "",
            "превосходный",
            "превос ходно",
            "превос!!ходно",
        )

        for value in _TESTS:
            with self.subTest(item=(value,)):
                with self.assertRaises(ValidationError):
                    item_count = Item.objects.count()
                    self.item = Item(
                        name=f"Негативный тест",
                        text=value,
                        category=Category.objects.get(id=1),
                        preview="/"
                    )
                    self.item.full_clean()
                    self.item.save()
                    self.item.tags.add(Tag.objects.get(id=1))
                    self.item.save()
                    self.assertEqual(item_count, Item.objects.count())

    def testTextPositiveValidators(self):
        _TESTS = (
            "Превосходно",
            "превосходно",
            "превосходно!",
            "!превосходно",
            "Роскошно    ",
            "роскошно",
        )
        for value in _TESTS:
            with self.subTest(item=(value,)):
                item_count = Item.objects.count()
                self.item = Item(
                    name=f"Позитивный тест {value}",
                    text=value,
                    category=Category.objects.get(id=1),
                    preview="/"
                )
                self.item.full_clean()
                self.item.save()
                self.item.tags.add(Tag.objects.get(id=1))
                self.item.save()
                self.assertEqual(item_count + 1, Item.objects.count())
