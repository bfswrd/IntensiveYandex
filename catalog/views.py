from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Item


def item_list(request):
    items = Item.objects.published().order_by("category")

    context = {
        "items": items,
    }
    return render(request, "catalog/items_list.html", context=context)


def item_detail(request, pk: int):
    return HttpResponse("Подробно элемент")
