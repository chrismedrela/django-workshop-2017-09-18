from django.shortcuts import render

from django.http import HttpResponse, Http404

from django.template import loader

from .models import Recipe

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    t = loader.get_template('recipes/index.html')
    
    c = {'object_list': recipes}  # create context with recipes
    response = t.render(c)  # render the template
    http_response = HttpResponse(response)  # wrap the result in HttpResponse
    return http_response  # return the HttpResponse


def detail(request, slug):
    try:
        recipe = Recipe.objects.get(slug=slug)
    except Recipe.DoesNotExist:
        raise Http404
    t = loader.get_template('recipes/detail.html')
    c = {'object': recipe}
    return HttpResponse(t.render(c))
