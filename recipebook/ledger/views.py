from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'