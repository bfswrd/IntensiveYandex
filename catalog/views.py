from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from catalog.models import Item


class ItemListView(ListView):
    model = Item
    template_name = "catalog/item_list.html"
    context_object_name = "items"

    def get_queryset(self):
        return Item.objects.published()


def item_detail(request, pk: int):
    item = get_object_or_404(Item.objects.published(), pk=pk)

    context = {
        "item": item,
    }

    return render(request, "catalog/item_detail.html", context=context)
