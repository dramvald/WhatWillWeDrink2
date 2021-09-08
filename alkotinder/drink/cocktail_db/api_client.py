import requests
from queue import PriorityQueue


class CocktailDBApiClient:
    RANDOM_DRINK_API_URL = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    ALCOHOL = 'Alcoholic'

    def get_random_drink(self):
        """
        Делам запрос на сервер по адресу req_url.
        Преобразуем строку json в объект python типа dict.
        """
        data = requests.get(self.RANDOM_DRINK_API_URL).json()
        drink = data["drinks"][0]

        name = drink["strDrink"]
        instruction = drink["strInstructions"]
        img_url = drink["strDrinkThumb"]

        ingredients = self._get_values_of_keys_sorted_by_index(drink, "strIngredient")
        measures = self._get_values_of_keys_sorted_by_index(drink, "strMeasure")

        if self.ALCOHOL == drink['strAlcoholic']:
            is_alcoholic = True
        else:
            is_alcoholic = False

        return {
            "name": name,
            "img_url": img_url,
            "instruction": instruction,
            "ingredients": list(filter(None, ingredients)),
            "measures": list(filter(None, measures)),
            "is_alcoholic": is_alcoholic,
        }

    def _get_values_of_keys_sorted_by_index(self, drink, name):
        """Эта функция позволяет автоматически найти и записать данные искомых значений"""
        pq = PriorityQueue()
        for key, value in drink.items():
            if isinstance(key, str) and key.startswith(name):
                if value:
                    pq.put((int(key[-1]), value))
        return [i[1] for i in pq.queue]
