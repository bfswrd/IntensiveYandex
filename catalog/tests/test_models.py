from django.core.exceptions import ValidationError
from django.test import TestCase

from catalog.models import Item, Category, Tag


class CategoryModelsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(name="Тест1", slug="test_1")

    def testCategoryWeightNegativeValidators(self):
        _TESTS = (
            -200,
            0,
            32767,
            100000
        )
        for value in _TESTS:
            with self.subTest(item=(value,)):
                with self.assertRaises(ValidationError):
                    self.category = Category(
                        name=f"Негативный тест {value}",
                        slug=f"negative_test_{value}",
                        weight=value
                    )
                    self.category.full_clean()
                    self.category.save()

    def testCategoryWeightPositiveValidators(self):
        _TESTS = (
            1,
            100,
            10000,
            32726
        )
        for value in _TESTS:
            with self.subTest(item=(value,)):
                self.category = Category(
                    name=f"Позитивный тест {value}",
                    slug=f"positive_active_{value}",
                    weight=value
                )
                self.category.full_clean()
                self.category.save()


class TagModelsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.tag = Tag.objects.create(name="Тест1", slug="test_1")

    def testSlugNegativeValidators(self):
        _TESTS = (
            "фыв",
            "asd//asd",
            "q0,asd",
            "a a",
        )
        for value in _TESTS:
            with self.subTest(item=(value,)):
                with self.assertRaises(ValidationError):
                    self.tag = Tag(
                        name=f"Негативный тест {value}",
                        slug=value,
                    )
                    self.tag.full_clean()
                    self.tag.save()

    def testSlugWeightPositiveValidators(self):
        _TESTS = (
            "test",
            "12345",
            "test_123456"
            "Asdf"
        )
        for value in _TESTS:
            with self.subTest(item=(value,)):
                self.tag = Tag(
                    name=f"Позитивный тест {value}",
                    slug=value,
                )
                self.tag.full_clean()
                self.tag.save()


class ItemModelsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        category = Category(name="Тест1", slug="test_1")
        category.full_clean()
        category.save()
        cls.Item = Item.objects.create(name="Тест1", category=category, category_id=category.id)

    def testTextNegativeValidators(self):
        _TESTS = (
            "",
            "Прекрасный",
            "Прекраснны",
            "Прек расно",
        )
        for value in _TESTS:
            with self.subTest(item=(value,)):
                with self.assertRaises(ValidationError):
                    self.item = Item(
                        name=f"Негативный тест {value}",
                        text=value,
                    )
                    self.item.full_clean()
                    self.item.save()

    def testTextPositiveValidators(self):
        _TESTS = (
            "Прекрасно",
            "прекрасно",
            "прекрасно!",
            "!прекрасно",
            "Идеально",
            "идеально",
        )
        for value in _TESTS:
            with self.subTest(item=(value,)):
                with self.assertRaises(ValidationError):
                    self.item = Item(
                        name=f"Негативный тест {value}",
                        text=value,
                    )
                    self.item.full_clean()
                    self.item.save()
