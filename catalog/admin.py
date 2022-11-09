from django.contrib import admin

from catalog.models import Item, Category, Tag, Gallery, Preview
from sorl.thumbnail.admin import AdminImageMixin
from django_summernote.admin import SummernoteModelAdmin


class GalleryInline(admin.TabularInline):
    model = Gallery
    fk_name = "item"


class PreviewInline(admin.TabularInline):
    model = Preview
    fk_name = "item"


class ItemAdmin(AdminImageMixin, SummernoteModelAdmin):
    summernote_fields = "text"

    list_display = ("name", "is_published")
    list_editable = ("is_published",)
    list_display_links = ("name",)

    filter_horizontal = ("tags",)

    inlines = [PreviewInline, GalleryInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "weight", "is_published",)
    list_editable = ("is_published",)
    list_display_links = ("name",)


class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_published",)
    list_editable = ("is_published",)
    list_display_links = ("name",)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ("image_tbm", "item",)
    list_display_links = ("image_tbm",)
    list_editable = ("item",)


class PreviewAdmin(admin.ModelAdmin):
    list_display = ("image_tbm", "item",)
    list_display_links = ("image_tbm",)
    list_editable = ("item",)


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Preview, PreviewAdmin)
