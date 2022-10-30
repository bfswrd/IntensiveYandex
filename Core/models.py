from django.db import models
from django.core.validators import validate_slug


class CommonCatalog(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Название",
        help_text="Это поле отвечает за название",
    )
    is_published = models.BooleanField(
        default=True, verbose_name="Опубликовано",
        help_text="Это поле отвечает за публикацию",
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
