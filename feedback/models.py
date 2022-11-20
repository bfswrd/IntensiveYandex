from django.db import models


class Feedback(models.Model):
    text = models.TextField(
        verbose_name="Обратная связь",
        help_text=f"Введите обращение"
    )
    created_on = models.DateTimeField(
        auto_now_add=True, blank=True,
        verbose_name="Время создания"
    )
