from django.db import models
from django.utils.safestring import mark_safe
from django.core.validators import validate_slug

from sorl.thumbnail import get_thumbnail


class CommonCatalog(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Название",
        help_text="Введите название",
    )
    is_published = models.BooleanField(
        default=True, verbose_name="Опубликовано",
        help_text="Введите публикацию",
    )

    class Meta:
        abstract = True


class Slug(models.Model):
    slug = models.SlugField(
        max_length=200, unique=True,
        validators=[
            validate_slug,
        ],
        verbose_name="Идентификатор",
        help_text="Это идентификатор"
    )

    class Meta:
        abstract = True


class PreviewCore(models.Model):
    preview = models.ImageField(upload_to="uploads/%Y/%m")

    @property
    def get_image(self):
        return get_thumbnail(
            self.preview, "300x300", crop="center", quality=51
        )

    def image_tbm(self):
        if self.preview:
            return mark_safe(f'<img src="{self.get_image.url}">')
        return "Изображение не найдено"

    image_tbm.short_description = "Превью"
    image_tbm.allow_tags = True

    class Meta:
        abstract = True


class GalleryCore(models.Model):
    gallery_image = models.ImageField(
        upload_to="uploads/%Y/%m",
        verbose_name="Картинка"
    )

    @property
    def get_image(self):
        return get_thumbnail(
            self.gallery_image, "300x300", crop="center", quality=51
        )

    def image_tbm(self):
        if self.gallery_image:
            return mark_safe(f'<img src="{self.get_image.url}">')
        return "Изображение не найдено"

    image_tbm.short_description = "Галерея"
    image_tbm.allow_tags = True

    class Meta:
        abstract = True
