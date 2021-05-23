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


def add_favorite_drink(request):
    random_drink = cache.get("random_drink")

    name_drink = random_drink["name"]
    url = random_drink["img_url"]
    instr = random_drink["instruction"]
    ingr = random_drink["ingredients"]
    meas = random_drink["measures"]
    drink_obj = Drink(
        name_drink=name_drink,
        drink_url=url,
        instruction=instr,
        ingredients=ingr,
        measures=meas,
    )
    drink_obj.save()
    return HttpResponseRedirect("/")
