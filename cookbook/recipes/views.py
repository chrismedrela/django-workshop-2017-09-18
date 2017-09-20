from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Recipe

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'object_list': recipes})


def detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, 'recipes/detail.html', {'object': recipe})
