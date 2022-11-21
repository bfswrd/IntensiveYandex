import re
from functools import wraps

from django.core.exceptions import ValidationError


def validate_must_be_param(*args):
    must_be_in_our_item = set(args)

    @wraps(validate_must_be_param)
    def validate_amazing(value: str):
        cleaner_value = set(re.sub(r"[^\w\s]", " ", value).lower().split())

        difference = must_be_in_our_item - cleaner_value

        if len(difference) == len(must_be_in_our_item):
            raise ValidationError(
                f"Обязательно используйте слова {must_be_in_our_item}")
        return value

    return validate_amazing
