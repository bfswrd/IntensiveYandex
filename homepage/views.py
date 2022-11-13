from django.shortcuts import render

from catalog.models import Item


def home(request):
    items = Item.objects.published().filter(is_on_main=True)
    context = {
        "items": items
    }
    return render(request, template_name="homepage/homepage.html", context=context)
