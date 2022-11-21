from django import forms

from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = (Feedback.text.field.name,)
        help_texts = {
            Feedback.text.field.name: Feedback.text.field.help_text,
        }
        labels = {
            Feedback.text.field.name: Feedback.text.field.verbose_name,
        }
        widgets = {
            Feedback.text.field.name: forms.Textarea(
                attrs={"class": "form-control-my",}
            ),
        }
