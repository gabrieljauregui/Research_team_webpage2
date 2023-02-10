from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import MyUser
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm


class MyUserCreationForm(UserCreationForm):
    username = forms.CharField()
    first_name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    last_name = forms.CharField(max_length=50)
    job = forms.CharField(max_length=100)
    educational_achievement = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    objectives = forms.CharField(widget=forms.Textarea)

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = UserCreationForm.Meta.fields + (
            "email",
            "first_name",
            "age",
            "last_name",
            "job",

            "educational_achievement",
            "description",
            "objectives",
        )


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = MyUser
        fields = (
            "username",
            "first_name",
            "age",
            "last_name",
            "job",
            "educational_achievement",
            "description",
            "objectives",
        )

class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))

"""

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"class": "form-control"})


def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")



"""
