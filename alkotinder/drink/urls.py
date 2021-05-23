from . import views
from django.urls import path

urlpatterns = [
    path("", views.get_random_drink, name="get_random_drink"),
    path("favorites/", views.favorites, name="favorites"),
    path("add_favorite_drink/", views.add_favorite_drink, name="add_favorite_drink"),
]
