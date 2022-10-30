from django.db import models


class CommonCatalog(models.Model):
    name = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Slug(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        abstract = True
