from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from . import service


RANDOM_DRINK_API_URL = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
INGREDIENT = 'strIngredient'
MEASURE = 'strMeasure'


def drinks(request):
    """Эта функция нужна для отображения необходимой информации на странице drink.html. В нее поступают данные о
    названии коктеля, инструкции, игридиентах их количестве, и картинке самого котеля. После чего эта вся информация
    попадает на страницу."""
    drink, instruction, drink_img, data_drinks = service.get_drink_date(RANDOM_DRINK_API_URL)
    ingredients = service.sort_values(data_drinks, INGREDIENT)
    measures = service.sort_values(data_drinks, MEASURE)
    context = {"drink": drink, "instruction": instruction, "drink_img": drink_img, "ingredients": ingredients,
               "measures": measures}
    return render(request, 'drink.html', context=context)

