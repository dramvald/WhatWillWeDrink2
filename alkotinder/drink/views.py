from django.shortcuts import render
from django.core.cache import cache
from django.views.generic import TemplateView

from .models import Drink, FavoriteDrink
from accounts.models import User
from django.urls import reverse

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
    """Выводим список сохраненных напитков на отдельную страницу. Также здесь осуществляется поиск
    по имени напитка."""
    search = request.GET.get("search", "")  # Получаю значение GET параметра search.
    user = request.user  # request.user.id атрибут представляет id текущего пользователя

    is_alcoholic = request.GET.get("is_alcoholic", "")
    favorite_drink_list = user.favoritedrink_set.order_by("-id").filter(
        drink__name__icontains=search
    )  # фильтр по названию напитка
    if is_alcoholic:
        favorite_drink_list = favorite_drink_list.filter(drink__is_alcoholic=is_alcoholic)

    return render(
        request, "favorites.html", {"favorite_drink_list": favorite_drink_list, "is_alcoholic": is_alcoholic, "search": search}
    )


def add_favorite_drink(request):
    """Сохраняем напиток, функция привязана к кнопке на старице случайных напитков. Данные напитка, ранее сохраненные
    в кэш, сохраняются в базу данных."""
    random_drink = cache.get("random_drink")

    name = random_drink["name"]
    drink_url = random_drink["img_url"]
    instruction = random_drink["instruction"]
    ingredients = random_drink["ingredients"]
    measures = random_drink["measures"]
    is_alcoholic = random_drink["is_alcoholic"]
    drink = Drink(
        name=name,
        drink_url=drink_url,
        instruction=instruction,
        ingredients=ingredients,
        measures=measures,
        is_alcoholic=is_alcoholic,
    )
    drink.save()

    FavoriteDrink.objects.create(
        user=request.user, drink=drink
    )   # создаю в FavoriteDrink объект с двумя полями
        # request.user атрибут представляет текущего пользователя
    return HttpResponseRedirect(reverse("get_random_drink"))


def show_favorite_drink(request, drink_id):
    """Выбираем напиток на странице любимых напитков и открываем по нему всю информацию на отдельной странице."""
    drink = Drink.objects.get(id=drink_id)
    return render(request, "show_favorites_drink.html", {"drink": drink})


def delete_favorite_drink(request, drink_id):
    """Для удаления напитка на странице любимых напитков и на станице выбранного, из любимых напитков ,напитка."""
    drink = Drink.objects.get(id=drink_id)
    drink.delete()
    return HttpResponseRedirect(reverse("list_favorite_drinks"))
