from django.contrib import admin

from catalog.models import Item, Category, Tag

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Tag)
