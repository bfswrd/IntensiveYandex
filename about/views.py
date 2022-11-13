from django.http import HttpResponse
from django.shortcuts import render


def description(request):
    return render(request, "about/about.html")
