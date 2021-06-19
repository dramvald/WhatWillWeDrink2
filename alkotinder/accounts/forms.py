from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class AccountUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'username',)


class AccountUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)
