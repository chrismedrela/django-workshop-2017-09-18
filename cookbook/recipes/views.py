import logging

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.template.defaultfilters import slugify

from .forms import RecipeForm
from .models import Recipe

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


def create(request):
    pass

@login_required
def edit(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)  # get the right recipe from db
    if (request.user != recipe.author) and (not request.user.is_staff): 
        raise PermissionDenied

    form = RecipeForm(instance=recipe)  # create empty RecipeForm
    
    context = {'form': form, 'object': recipe, 'create': False}
    return render(request, 'recipes/form.html', context)  # render right template
