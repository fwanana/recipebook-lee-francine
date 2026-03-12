from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Recipe, RecipeImage
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeForm, RecipeImageForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_form.html'


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = 'recipe_image_form.html'
