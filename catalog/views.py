from django.shortcuts import render, get_object_or_404

from catalog.models import Item


def item_list(request):
    items = Item.objects.published().order_by("category")

    context = {
        "items": items,
    }
    return render(request, "catalog/items_list.html", context=context)


def item_detail(request, pk: int):
    item = get_object_or_404(Item, pk=pk)

    context = {
        "item": item,
    }

    return render(request, "catalog/item_detail.html", context=context)
