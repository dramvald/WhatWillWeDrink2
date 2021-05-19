from . import views
from django.urls import path

urlpatterns = [
    path("", views.get_random_drink, name="get_random_drink"),
]
