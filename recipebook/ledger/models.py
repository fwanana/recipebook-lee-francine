from datetime import datetime
from django.db import models
#from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

class Recipe(models.Model):
    name = models.CharField(max_length=50)

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=3)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
