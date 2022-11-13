from django.http import HttpResponse
from django.shortcuts import render


def item_list(request):
    return render(request, "catalog/items_list.html")


def item_detail(request, pk: int):
    return HttpResponse("Подробно элемент")
