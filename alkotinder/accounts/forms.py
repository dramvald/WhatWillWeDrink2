from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
    UsernameField,
)
from .models import User


# class AccountEmailField(forms.EmailField):
#    def clean(self, value):
#       return value.lower()


class AccountUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="E-mail", widget=forms.EmailInput(attrs={"class": "form-input"})
    )
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
    password2 = forms.CharField(
        label="Repeat password ",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
    )

    class Meta(UserCreationForm):
        model = User
        fields = (
            "email",
            "password1",
            "password2",
        )

    def clean_email(self):
        # super().clean_email()
        cleaned_email = self.cleaned_data["email"]
        return cleaned_email.lower()


class AccountUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)


class AccountAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))

    def clean_username(self):
        cleaned_username = self.cleaned_data["username"]
        return cleaned_username.lower()
