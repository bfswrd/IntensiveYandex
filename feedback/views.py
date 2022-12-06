from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import FormView
from django.shortcuts import redirect

from feedback import forms
from feedback.models import Feedback


class FeedbackView(FormView):
    form_class = forms.FeedbackForm
    model = Feedback
    template_name = "feedback/feedback.html"

    def get(self, request, *args: str, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args: str, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        Feedback.objects.create(**form.cleaned_data)
        self.send_mail(form.cleaned_data)
        return redirect("feedback:feedback")

    def form_invalid(self, form):
        return super().form_invalid(form)

    def send_mail(self, valid_data):
        send_mail(
            f"Обратная связь",
            message=valid_data.get("text"),
            from_email=settings.NOREPLY_EMAIL,
            recipient_list=(*settings.ADMIN_EMAILS,),
            fail_silently=False,
        )

