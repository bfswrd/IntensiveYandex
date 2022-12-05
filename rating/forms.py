from django.forms.models import ModelForm

from rating.models import Rating


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ("rating",)
