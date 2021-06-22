from django.urls import path, include
from .views import SignUpView
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path("drink/", include("drink.urls")),
    path('signup/', SignUpView.as_view(), name='signup'),
]
