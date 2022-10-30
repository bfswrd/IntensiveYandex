import re

from django.core.exceptions import ValidationError
from functools import wraps


def validate_must_be_param(*args):
    must_be_in_our_item = args

    @wraps(validate_must_be_param)
    def validate_amazing(value: str):

        for word in must_be_in_our_item:
            if word in value:
                raise ValidationError(f"Обязательно используйте слова {must_be_in_our_item}")
        return value

    return validate_amazing
