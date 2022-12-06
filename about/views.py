from django.shortcuts import render
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "about/about.html"
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
