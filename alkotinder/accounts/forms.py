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
    """Форма используется для страницы SignUp, заданы поля и их формат. Класс clean_email необходим для
    форматирование страницы email, а именно приведения всех букв к нижнему регистру используя метод lower()."""

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
        """Задаем использование модели User, и определяем поля формы в fields"""

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
    """Задаем использование модели User, и определяем поля формы в fields"""

    class Meta:
        model = User
        fields = ("email",)


class AccountAuthenticationForm(AuthenticationForm):
    """Форма предназначена исключительно для добавления функции clean_username, которая форматирует поле username
    и приводит все буквы к нижнему регистру используя метод lower()."""

    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))

    def clean_username(self):
        cleaned_username = self.cleaned_data["username"]
        return cleaned_username.lower()
