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
    )


class Tag(CommonCatalog, Slug):
    pass


class Item(CommonCatalog):
    text = models.TextField(
        validators=[
            validate_must_be_param("превосходно", "прекрасно"),
        ],
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="tag")
