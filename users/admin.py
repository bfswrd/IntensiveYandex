from django.contrib import admin
from users.models import User, Birthday
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import Group


class BirthdayInline(admin.StackedInline):
    model = Birthday


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = [
        BirthdayInline
    ]


admin.site.unregister(Group)
