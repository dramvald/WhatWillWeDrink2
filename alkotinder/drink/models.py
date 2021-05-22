from django.db import models


class Drink(models.Model):
    name_drink = models.CharField("Name drink", max_length=200)
    drink_url = models.TextField("Url drink img")
    instruction = models.TextField("Instruction")
    ingredients = models.CharField("Ingredients", max_length=300)
    measures = models.CharField("Measures", max_length=300)
