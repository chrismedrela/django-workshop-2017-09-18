from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from .models import Recipe

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    t = loader.get_template('recipes/index.html')
    
    # create context with recipes
    
    # render the template
    
    # wrap the result in HttpResponse
    
    # return the HttpResponse
