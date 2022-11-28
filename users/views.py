from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.views import View
from django.views.generic.base import ContextMixin

from .forms import UserChangeForm, UserCreationForm
from .models import User


def signup(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save(commit=True)
            return redirect(reverse("homepage:home"))
    else:
        user_form = UserCreationForm()
    return render(request, "users/login.html",
                  {"form": user_form, "name": "Регистрация",
                   "button": "Создать"})


class Profile(ContextMixin, View):
    template_name = "users/login.html"

    def get(self, request, *args, **kwargs):
        if str(request.user) == "AnonymousUser":
            return redirect(reverse("homepage:home"))
        user_form = UserChangeForm(instance=request.user)

        context = self.get_context_data(**kwargs)
        context["form"] = user_form
        context["button"] = "Сохранить"
        context["name"] = "Профиль"
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        user_form = UserChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect(reverse("homepage:home"))
        context = {"form": user_form, "button": "Сохранить", "name": "Профиль"}
        return render(request, self.template_name,
                      context=context)


def user_list(request):
    users = User.objects.is_active()

    context = {"users": users}
    return render(request, "users/user_list.html", context=context)


def user_detail(request, pk):
    user = get_object_or_404(User.objects.is_active(), pk=pk)

    context = {
        "user": user
    }
    return render(request, "users/user_detail.html", context=context)
