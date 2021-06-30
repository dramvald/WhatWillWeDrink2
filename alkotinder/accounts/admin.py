from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import AccountUserChangeForm, AccountUserCreationForm
from .models import User


class AccountUserAdmin(UserAdmin):
    add_form = AccountUserCreationForm
    form = AccountUserChangeForm
    model = User

    list_display = [
        "email",
    ]
    fieldsets = (('Personal info', {'fields': ('email', 'first_name', 'last_name')}),)     # Для страницы изменения
                                                                                           # личной информации пользователя
    ordering = ('email',)                                                        # Для упорядочения по полю email


admin.site.register(User, AccountUserAdmin)

# Register your models here.
