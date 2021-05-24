from django.shortcuts import render
from django.core.cache import cache
from .models import Drink
from django.http import HttpResponseRedirect
from drink.cocktail_db.api_client import CocktailDBApiClient


def get_random_drink(request):
    cocktail_db_api_client = CocktailDBApiClient()
    random_drink = cocktail_db_api_client.get_random_drink()

    cache.set("random_drink", random_drink)

    return render(request, "get_random_drink.html", context=random_drink)


def list_favorite_drinks(request):
    drink_list = Drink.objects.all()
    return render(request, "favorites.html", {"drink_list": drink_list})


def add_favorite_drink(request):
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
    return HttpResponseRedirect("/")
