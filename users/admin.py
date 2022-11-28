from django.contrib import admin
from django.contrib.auth.admin import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.forms import UserChangeForm, UserCreationForm
from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ("email", "is_staff", "is_superuser",)
    list_filter = ("is_superuser",)
    fieldsets = (
        (None, {"fields": (
            "email", "password", "birthday",
            "first_name", "last_name",
            "is_superuser", "is_active")}),
    )
    add_fieldsets = (
        (None, {"fields": (
            "email", "password", "birthday",
            "first_name", "last_name",
            "is_superuser", "is_active")}),
    )

    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


admin.site.unregister(Group)
