from datetime import datetime, timedelta

from django.core.exceptions import ValidationError


def date_validator(date) -> bool:
    if (datetime.now() - timedelta(days=43800)).date() > date:
        raise ValidationError(
            "Вам точно не больше 120 лет :3")
    if date > datetime.now().date():
        raise ValidationError(
            "Машину времени еще не придумали)")
    return date
