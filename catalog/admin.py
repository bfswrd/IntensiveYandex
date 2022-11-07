from django.contrib import admin

from catalog.models import Item, Category, Tag, Gallery
from sorl.thumbnail.admin import AdminImageMixin
from django_summernote.admin import SummernoteModelAdmin


class ItemAdmin(AdminImageMixin, SummernoteModelAdmin):
    summernote_fields = "text"

    list_display = ("name", "is_published", "image_tbm")
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


class GalleryAdmin(admin.ModelAdmin):
    list_display = ("image_tbm", "gallery_image",)
    list_display_links = ("gallery_image", "image_tbm",)


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Gallery, GalleryAdmin)
