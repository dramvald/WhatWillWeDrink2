from django.urls import path
from .views import SignUpView, LogInView


urlpatterns = [
    path("", LogInView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
