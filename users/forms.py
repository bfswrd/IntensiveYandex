from django import forms

from users.models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повторите пароль",
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", "birthday", "first_name",
                  "last_name")
        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date",
                                               'id': 'datetimepicker12'})
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password1"] != cd["password2"]:
            raise forms.ValidationError("Passwords don\'t match.")
        return cd["password2"]

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "birthday", "first_name",)
        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date",
                                               'id': 'datetimepicker12'})
        }

    def clean_email(self):
        return self.data["email"]
