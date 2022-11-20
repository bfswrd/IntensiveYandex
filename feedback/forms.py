from django import forms

from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control-my"

    class Meta:
        model = Feedback
        fields = (Feedback.text.field.name,)
        help_texts = {
            Feedback.text.field.name: Feedback.text.field.help_text,
        }
        labels = {
            Feedback.text.field.name: Feedback.text.field.verbose_name,
        }
