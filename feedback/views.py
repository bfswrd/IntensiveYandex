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
        send_mail(
            f"Обратная связь",
            message=form.cleaned_data.get('text'),
            from_email=settings.ADMIN_EMAIL,
            recipient_list=(settings.ADMIN_EMAIL,),
            fail_silently=False,
        )
        Feedback.objects.create(**form.cleaned_data).save()
        return redirect("feedback:feedback")
    return render(request, "feedback/feedback.html", context=context)
