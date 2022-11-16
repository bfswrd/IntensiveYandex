from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from sorl.thumbnail.admin import AdminImageMixin

from catalog.models import Category, Gallery, Item, Preview, Tag


class GalleryInline(admin.TabularInline):
    model = Gallery
    fk_name = "item"
    extra = 0
    readonly_fields = ("image_tbm",)
    fields = ("image_tbm", "gallery_image",)


class PreviewInline(admin.TabularInline):
    model = Preview
    fk_name = "item"
    extra = 0
    readonly_fields = ("image_tbm",)
    fields = ("image_tbm", "preview",)


@admin.register(Item)
class ItemAdmin(AdminImageMixin, SummernoteModelAdmin):
    summernote_fields = "text"

    list_display = ("name", "is_published", "is_on_main",)
    list_editable = ("is_published", "is_on_main",)
    list_display_links = ("name",)

    filter_horizontal = ("tags",)

    inlines = [PreviewInline, GalleryInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "weight", "is_published",)
    list_editable = ("is_published",)
    list_display_links = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_published",)
    list_editable = ("is_published",)
    list_display_links = ("name",)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("image_tbm", "item",)
    list_display_links = ("image_tbm",)
    list_editable = ("item",)


@admin.register(Preview)
class PreviewAdmin(admin.ModelAdmin):
    list_display = ("image_tbm", "item",)
    list_display_links = ("image_tbm",)
    list_editable = ("item",)
