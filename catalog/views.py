from django.shortcuts import get_object_or_404, render

from catalog.models import Item


def item_list(request):
    items = Item.objects.published().order_by("category__name", "name")

    context = {
        "items": items,
    }
    return render(request, "catalog/items_list.html", context=context)


def item_detail(request, pk: int):
    item = Item.objects.get_or_404(pk=pk, is_published=True)

    context = {
        "item": item,
    }

    return render(request, "catalog/item_detail.html", context=context)
