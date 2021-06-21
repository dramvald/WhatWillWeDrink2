from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class AccountUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat password ', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'username', 'password1', 'password2',)


class AccountUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)
