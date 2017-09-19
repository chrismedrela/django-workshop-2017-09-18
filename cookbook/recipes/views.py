from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Recipe

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()

    return render_to_response('recipes/index.html', {'object_list': recipes})


def detail(request, slug):
    try:
        recipe = Recipe.objects.get(slug=slug)
    except Recipe.DoesNotExist:
        raise Http404
    t = loader.get_template('recipes/detail.html')
    c = {'object': recipe}
    return HttpResponse(t.render(c))
