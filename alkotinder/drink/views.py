from django.shortcuts import render
from django.core.cache import cache
from django.views.generic import TemplateView

from .models import Drink
from django.http import HttpResponseRedirect
from drink.cocktail_db.api_client import CocktailDBApiClient


def get_random_drink(request):
    """
    Эта функция выводит случайный коктейль на главную страницу сайта.
    Переменной cocktail_db_api_client присваивается класс, в результате выполнения которого
    мы получаем случайный напиток со всеми необходимыми данными. Далее добавляем его в кэш.
    """
    cocktail_db_api_client = CocktailDBApiClient()
    random_drink = cocktail_db_api_client.get_random_drink()

    cache.set("random_drink", random_drink)  # сохраняем данные со страницы в кэш
    return render(request, "get_random_drink.html", context=random_drink)


def list_favorite_drinks(request):
    """Выводим список сохраненных напитков на отдельную страницу."""
    drink_list = Drink.objects.order_by("-id")
    return render(request, "favorites.html", {"drink_list": drink_list})


def add_favorite_drink(request):
    """Сохраняем напиток, функция привязана к кнопке на старице случайных напитков. Данные напитка, ранее сохраненные
    в кэш, сохраняются в базу данных."""
    random_drink = cache.get("random_drink")

    name_drink = random_drink["name"]
    drink_url = random_drink["img_url"]
    instruction = random_drink["instruction"]
    ingredients = random_drink["ingredients"]
    measures = random_drink["measures"]
    drink_objects = Drink(
        name_drink=name_drink,
        drink_url=drink_url,
        instruction=instruction,
        ingredients=ingredients,
        measures=measures,
    )
    drink_objects.save()
    return HttpResponseRedirect("/drink")


def show_favorite_drink(request, drink_id):
    """Выбираем напиток на странице любимых напитков и открываем по нему всю информацию на отдельной странице."""
    drink = Drink.objects.get(id=drink_id)
    return render(request, "show_favorites_drink.html", {"drink": drink})


def delete_favorite_drink(request, drink_id):
    """Для удаления напитка на странице любимых напитков и на станице выбранного, из любимых напитков ,напитка."""
    drink = Drink.objects.get(id=drink_id)
    drink.delete()
    return HttpResponseRedirect("/favorites")
