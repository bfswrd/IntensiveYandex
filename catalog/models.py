from django.db import models

from Core.models import CommonCatalog, Slug, PreviewCore, GalleryCore
from Core.validators import validate_must_be_param


class Category(CommonCatalog, Slug):
    weight = models.PositiveSmallIntegerField(
        default=100,
        verbose_name="Вес",
        help_text="Введите вес товара"
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


class Item(CommonCatalog, PreviewCore):
    text = models.TextField(
        validators=[
            validate_must_be_param('превосходно', 'роскошно')
        ],
        verbose_name="Описание",
        help_text=f"Введите описание товара"
    )

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Введите категорию товара"
    )

    tags = models.ManyToManyField(
        Tag, related_name="tag",
        verbose_name="Теги",
        help_text="Введите теги товара, их может быть очень много"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Товары"


class Gallery(GalleryCore):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.gallery_image.url

    class Meta:
        verbose_name = "фото"
        verbose_name_plural = "Галерея"
