from django.db import models
from django.shortcuts import reverse

from Core.models import CommonCatalog, Slug, PreviewCore, GalleryCore
from Core.validators import validate_must_be_param


class Category(CommonCatalog, Slug):
    weight = models.PositiveSmallIntegerField(
        default=100,
        verbose_name="Вес",
        help_text="Введите вес товара"
    )

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Tag(CommonCatalog, Slug):
    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class ItemManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
                .filter(is_published=True)
                .select_related("category")
                .prefetch_related(
                models.Prefetch(
                    'tags',
                    queryset=Tag.objects.filter(is_published=True)
                )
            )
        )


class Item(CommonCatalog):
    objects = ItemManager()

    is_on_main = models.BooleanField(
        default=False, verbose_name="Опубликовано на главной",
        help_text="Включите, если публикация должна отображаться на главной",
    )

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

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Товары"
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("catalog:item_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Gallery(GalleryCore):
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE,
        verbose_name="Товар",
        help_text="Выберите товар, к которому необходимо привязать фото"
    )

    class Meta:
        verbose_name = "фото"
        verbose_name_plural = "Галерея"

    def __str__(self):
        return self.gallery_image.url


class Preview(PreviewCore):
    item = models.OneToOneField(
        Item, on_delete=models.CASCADE,
        verbose_name="Товар",
        help_text="Выберите товар, к которому необходимо привязать фото"
    )

    class Meta:
        verbose_name = "Превью"
        verbose_name_plural = "Превьюхи"

    def __str__(self):
        return self.preview.url
