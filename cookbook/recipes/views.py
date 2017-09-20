from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Recipe

import logging

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    # raise AssertionError  # first debugging way
    # print('recipes =', recipes)
    # print('request =', request)
    # print('locals() = ', locals())
    logger.debug('recipes = {}'.format(recipes))
    logger.debug('request = {}'.format(request))
    logger.debug('locals() = {}'.format(locals()))
    return render(request, 'recipes/index.html', {'object_list': recipes})


def detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    # import ipdb; ipdb.set_trace()
    return render(request, 'recipes/detail.html', {'object': recipe})
