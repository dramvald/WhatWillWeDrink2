from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import requests
from queue import PriorityQueue


ALCOHOL = 'Alcoholic'
RANDOM_DRINK_API_URL = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
INGREDIENT = 'strIngredient'
MEASURE = 'strMeasure'


def get_drink_date(RANDOM_DRINK_API_URL):
    """Делам запрос на сервер по адресу req_url.
    Преобразуем строку json в объект python типа dict."""
    data = requests.get(RANDOM_DRINK_API_URL).json()
    # Так как содержимое ключа drinks имеет тип list,
    # использую for для того чтобы пройтись по элементам списка,
    # которые являются словарями, и взять нужные данные.
    for item in data['drinks']:
        drink = item['strDrink']
        instruction = item['strInstructions']
        drink_img = item['strDrinkThumb']
        # Делаю проверку на алкогольный или без алкогольный напиток, и если он без алкогольный,
        # то отправляется снова запрос и проходит по циклу.
        if ALCOHOL != item['strAlcoholic']:
            return get_drink_date(RANDOM_DRINK_API_URL)
        else:
            return drink, instruction, drink_img, data['drinks'][0]


def sort_values(drink, property_name):
    """Эта функция позволяет автоматически найти и записать данные искомых значений"""
    pq = PriorityQueue()
    for key, value in drink.items():
        if isinstance(key, str) and key.startswith(property_name):
            if value is not None:
                # Уменьшаю список убирая элементы имеющие None.
                pq.put((int(key[-1]), value))
    return [i[1] for i in pq.queue]


def drinks(request):
    drink, instruction, drink_img, data_drinks = get_drink_date(RANDOM_DRINK_API_URL)
    ingredients = sort_values(data_drinks, INGREDIENT)
    measures = sort_values(data_drinks, MEASURE)
    context = {"drink": drink, "instruction": instruction, "drink_img": drink_img, "ingredients": ingredients,
               "measures": measures}
    return render(request, 'drink.html', context=context)


print(get_drink_date(RANDOM_DRINK_API_URL))
