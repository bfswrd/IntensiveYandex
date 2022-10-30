from django.contrib import admin

from catalog.models import Item, Category, Tag


class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published",)
    list_editable = ("is_published",)
    list_display_links = ("name",)

    filter_horizontal = ("tags",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "weight", "is_published",)
    list_editable = ("is_published",)
    list_display_links = ("name",)


class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_published",)
    list_editable = ("is_published",)
    list_display_links = ("name",)


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
