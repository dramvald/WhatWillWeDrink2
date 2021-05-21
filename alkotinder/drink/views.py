from django.shortcuts import render
from django.core.cache import cache


from drink.cocktail_db.api_client import CocktailDBApiClient


def get_random_drink(request):
    cocktail_db_api_client = CocktailDBApiClient()
    random_drink = cocktail_db_api_client.get_random_drink()

    cache.set("random_drink", random_drink)

    return render(request, "get_random_drink.html", context=random_drink)


def favorites(request):
    return render(request, "favorites.html")
