from django.db import models
from django.urls import reverse
from useraccounts.models import Profile


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:ingredient_detail', args=[self.pk])


class Recipe(models.Model):
    author = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="recipe")
    name = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[self.pk])


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="recipe")
    quantity = models.CharField(max_length=50)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients")
