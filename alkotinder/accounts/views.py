from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import AccountUserCreationForm, AccountAuthenticationForm
from django.contrib.auth.views import LoginView


class SignUpView(CreateView):
    """Добавляем view для регистрации пользователя."""

    form_class = AccountUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class LogInView(LoginView):
    """Добавляем view для входа пользователя на сайт."""

    form_class = AccountAuthenticationForm
    template_name = "registration/login.html"
