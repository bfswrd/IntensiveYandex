from django.contrib import admin

from rating.models import Rating


@admin.register(Rating)
class AdminRating(admin.ModelAdmin):
    list_display = ("rating", "user", "item",)
    list_display_links = ("rating",)
