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


def favorites(request):
    drink_list = Drink.objects.all()
    return render(request, "favorites.html", {'drink_list': drink_list})


def add_favorite_drink(request):
    a = cache.get("random_drink")
    name_drink = a.name
    url = a.img_url
    instr = a.instruction
    ingr = a.ingredients
    meas = a.measures
    drink_obj = Drink(name_drink=name_drink, drink_url=url, instruction=instr,
                      ingredients=ingr, measures=meas)
    drink_obj.save()
    return HttpResponseRedirect()
