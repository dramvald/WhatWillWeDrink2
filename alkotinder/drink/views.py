from django.shortcuts import render
from . import service
from django.core.cache import cache


RANDOM_DRINK_API_URL = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
INGREDIENT = 'strIngredient'
MEASURE = 'strMeasure'


def drinks(request):
    """Эта функция нужна для отображения необходимой информации на странице drink.html. В нее поступают данные о
    названии коктеля, инструкции, игридиентах их количестве, и картинке самого котеля. После чего эта вся информация
    попадает на страницу."""
    drink, instruction, drink_img, data_drinks = service.get_drink_data(RANDOM_DRINK_API_URL)
    ingredients = service.sort_values(data_drinks, INGREDIENT)
    measures = service.sort_values(data_drinks, MEASURE)
    context = cache.get('context')
    if not context:
        context = {"drink": drink, "instruction": instruction, "drink_img": drink_img, "ingredients": ingredients,
                   "measures": measures}
        cache.set('context', context, 30)
    return render(request, 'drink.html', context=context)

