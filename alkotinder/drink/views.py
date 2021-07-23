from django.shortcuts import render
from django.core.cache import cache
from django.views.generic import TemplateView

from .models import Drink, FavoriteDrink
from accounts.models import User

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


def list_favorite_drinks(request, user_id):
    """Выводим список сохраненных напитков на отдельную страницу."""
    # drink_list = Drink.objects.order_by("-id")
    # favorite_drink_list = FavoriteDrink.objects.order_by("-id")
    # check_favorite_drink_list = FavoriteDrink.objects.filter(user__id=user_id)
    user_object = User.objects.get(id=user_id)
    favorite_drink_list = user_object.favoritedrink_set.order_by('-id')

    return render(request, "favorites.html", {"favorite_drink_list": favorite_drink_list})


def add_favorite_drink(request, user_id):
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

    # drink_objects_id = drink_objects.id                                   # беру id напитка
    # get_drink = Drink.objects.get(id=drink_objects_id)                    # беру напиток по id
    user_object = User.objects.get(id=user_id)                            # беру пользователя
    favorite_drink_object = user_object.favoritedrink_set.create()        # создаю для пользователя поле, для связи с напитком
    drink_objects.favoritedrink_set.add(favorite_drink_object, bulk=False)    # добавляю напиток к созданному полю в модели FavoriteDrink
    return HttpResponseRedirect("/drink")


def show_favorite_drink(request, drink_id):
    """Выбираем напиток на странице любимых напитков и открываем по нему всю информацию на отдельной странице."""
    drink = Drink.objects.get(id=drink_id)
    return render(request, "show_favorites_drink.html", {"drink": drink})


def delete_favorite_drink(request, drink_id):
    """Для удаления напитка на странице любимых напитков и на станице выбранного, из любимых напитков ,напитка."""
    drink = Drink.objects.get(id=drink_id)
    drink.delete()
    return HttpResponseRedirect("/drink/favorites")
