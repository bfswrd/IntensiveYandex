from django.core.mail import send_mail
from django.shortcuts import redirect, render

from feedback import forms
from feedback.models import Feedback


def feedback(request):
    form = forms.FeedbackForm(request.POST or None)
    context = {
        "form": form
    }
    if request.POST and form.is_valid():
        send_mail(
            "Привет",
            (f"Мы улышали тебя и хоти сказать спасибо"
             f" за обраную свзязь {form.cleaned_data.get('text')}"),
            "from@to.ru",
            ["ex1@amp.le", "ex2@amp.le", ],
            fail_silently=False,
        )
        Feedback.objects.create(**form.cleaned_data).save()
        return redirect("feedback:feedback")
    return render(request, "feedback/feedback.html", context=context)
