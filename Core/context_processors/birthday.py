from users.models import User
from django.utils import timezone


def birthday_users(request):
    datetime_now = timezone.now()
    birthday_today = User.objects.filter(birthday__day=datetime_now.day, birthday__month=datetime_now.month).values(
        User.first_name.field.name, User.email.field.name)
    return {
        "birthday_users": birthday_today
    }
