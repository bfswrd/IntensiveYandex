from django.shortcuts import render
from django.views import View
from django.views.generic.base import ContextMixin

from catalog.models import Item


class Home(ContextMixin, View):
    def get(self, request, *args, **kwargs):
        items = Item.objects.published().filter(is_on_main=True)

        print(request, args, kwargs)
        context = self.get_context_data(**kwargs)
        context["items"] = items
        return render(request, template_name="homepage/homepage.html",
                      context=context)
