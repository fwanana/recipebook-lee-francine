from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

# Register your models here.


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
