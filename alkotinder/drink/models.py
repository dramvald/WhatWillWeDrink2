from django.db import models
from django.contrib.postgres.fields import ArrayField

from accounts.models import User


class Drink(models.Model):
    name = models.CharField("Name drink", max_length=200)
    drink_url = models.TextField("Url drink img")
    instruction = models.TextField("Instruction")
    ingredients = ArrayField(
        models.CharField("Ingredients", max_length=300), blank=True
    )
    measures = ArrayField(models.CharField("Measures", max_length=300), blank=True)
    is_alcoholic = models.BooleanField()

    def __str__(self):
        return self.name


class FavoriteDrink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, null=True)
