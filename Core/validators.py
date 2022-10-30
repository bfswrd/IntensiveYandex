from django.core.exceptions import ValidationError
from functools import wraps


def validate_must_be_param(*args):
    must_be_in_our_item = {i.lower() for i in args}

    @wraps(validate_must_be_param)
    def validate_amazing(value: str):
        cleaner_value = set(value.lower().split())

        difference = must_be_in_our_item - cleaner_value

        if len(difference) == len(must_be_in_our_item):
            raise ValidationError(f"Обязательно используйте слова {must_be_in_our_item}")
        return value

    return validate_amazing
