from django.db import models

from catalog.models import Item
from users.models import User


class RatingManager(models.Manager):
    def get_or_none_rating(self, user_id, item_id,):
        try:
            return self.get(user_id=user_id, item_id=item_id).rating
        except:
            return None


class Rating(models.Model):
    RATINGS = [
        (1, "Ненависть"),
        (2, "Неприязнь"),
        (3, "Нейтрально"),
        (4, "Обожание"),
        (5, "Любовь"),
    ]
    rating = models.PositiveSmallIntegerField(
        choices=RATINGS,
        verbose_name="Оценка",
    )

    user = models.ForeignKey(
        to=User, null=False, on_delete=models.CASCADE,
        verbose_name="Пользователь",)

    item = models.ForeignKey(
        to=Item, on_delete=models.CASCADE,
        verbose_name="Товар",
        help_text="Выберите товар, к которому необходимо привязать фото"
    )

    objects = RatingManager()

    class Meta:
        verbose_name = "оценку"
        verbose_name_plural = "Оценки"
        constraints = (
            models.UniqueConstraint(
                fields=["rating", "user", "item"], name="unique_user_item"),
        )

    def __str__(self) -> str:
        return str(self.item)
