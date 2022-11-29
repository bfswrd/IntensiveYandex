from datetime import datetime, timedelta

from django.core.exceptions import ValidationError


def date_validator(date) -> bool:
    if (datetime.now().date() < date or
            (datetime.now() - timedelta(days=43800)).date() > date):
        raise ValidationError(
            "Введите дату в пределах разумного, вам точно не 120 лет :3")
    return date
