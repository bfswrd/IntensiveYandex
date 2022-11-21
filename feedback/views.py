from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.conf import settings

from feedback import forms
from feedback.models import Feedback


def feedback(request):
    form = forms.FeedbackForm(request.POST or None)
    context = {
        "form": form
    }
    if request.POST and form.is_valid():
        Feedback.objects.create(**form.cleaned_data)
        send_mail(
            f"Обратная связь",
            message=form.cleaned_data.get("text"),
            from_email=settings.NOREPLY_EMAIL,
            recipient_list=(*settings.ADMIN_EMAILS,),
            fail_silently=False,
        )
        return redirect("feedback:feedback")
    return render(request, "feedback/feedback.html", context=context)
