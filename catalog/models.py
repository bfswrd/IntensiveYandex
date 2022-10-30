from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from Core.models import CommonCatalog, Slug
from Core.validators import validate_must_be_param


class Category(CommonCatalog, Slug):
    weight = models.IntegerField(
        default=100,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(32766),
        ],
        verbose_name="Вес",
        help_text="Это поле отвечает за вес товара"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "Категории"


class Tag(CommonCatalog, Slug):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "Теги"


class Item(CommonCatalog):
    text = models.TextField(
        validators=[
            validate_must_be_param("превосходно", "прекрасно"),
        ],
        verbose_name="Описание",
        help_text=f"Это поле отвечает за описание товара"
    )

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Это поле отвечает за категорию товара"
    )
    tags = models.ManyToManyField(
        Tag, related_name="tag",
        verbose_name="Теги",
        help_text="Это поле отвечает за теги товара, их может быть очень много"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Товары"
