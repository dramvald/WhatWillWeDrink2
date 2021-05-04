from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('drinks/', views.drinks, name='drinks'),
]