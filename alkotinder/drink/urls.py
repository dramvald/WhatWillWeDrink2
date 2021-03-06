from . import views
from django.urls import path

urlpatterns = [
    path("", views.get_random_drink, name="get_random_drink"),
    path("favorites/", views.list_favorite_drinks, name="list_favorite_drinks"),
    path("add_favorite_drink/", views.add_favorite_drink, name="add_favorite_drink"),
    path("<int:drink_id>/", views.show_favorite_drink, name="show_favorite_drink"),
    path(
        "delete/<int:drink_id>/",
        views.delete_favorite_drink,
        name="delete_favorite_drink",
    ),
]
