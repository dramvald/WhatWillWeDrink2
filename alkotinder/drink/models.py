from django.db import models
from django.contrib.postgres.fields import ArrayField


class Drink(models.Model):
    name_drink = models.CharField("Name drink", max_length=200)
    drink_url = models.TextField("Url drink img")
    instruction = models.TextField("Instruction")
    ingredients = ArrayField(
        models.CharField("Ingredients", max_length=300), blank=True
    )
    measures = ArrayField(models.CharField("Measures", max_length=300), blank=True)

    def __str__(self):
        return self.name_drink
