import logging

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.template.defaultfilters import slugify
from django.views.generic import DetailView, ListView

from .forms import RecipeForm
from .models import Recipe

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'object_list': recipes})


def detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    # import ipdb; ipdb.set_trace()
    return render(request, 'recipes/detail.html', {'object': recipe})


class RecipeListView(ListView):
    template_name = 'recipes/index.html'

    def get_queryset(self):
        recipes = Recipe.objects.all()
        logger.debug('Recipes count: %d' % recipes.count())
        return recipes


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

class RecipeCreateView(CreateView):
    template_name = 'recipes/form.html'
    form_class = RecipeForm
    model = Recipe

    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.slug = slugify(recipe.title)
        recipe.save()
        form.save_m2m()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create'] = True
        return context


@login_required
def create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.slug = slugify(recipe.title)
            recipe.save()
            form.save_m2m()
            return redirect(recipe)
    else:
        form = RecipeForm()
    context = {'form': form, 'create': True}
    return render(request, 'recipes/form.html', context)


@login_required
def edit(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if (request.user != recipe.author) and (not request.user.is_staff): 
        raise PermissionDenied

    if request.method == "POST":
        form = RecipeForm(instance=recipe, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(recipe)
    else:
        form = RecipeForm(instance=recipe)
    
    context = {'form': form, 'object': recipe, 'create': False}
    return render(request, 'recipes/form.html', context)
