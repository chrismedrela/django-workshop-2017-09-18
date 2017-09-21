from django.conf.urls import include, url

import recipes.views

urlpatterns = [
    url(r'^recipe/(?P<slug>[-\w]+)/$', recipes.views.RecipeDetailView.as_view(), 
        name='recipes_recipe_detail'),
    url(r'^$', recipes.views.RecipeListView.as_view(),
        name='recipes_recipe_index'),
    url(r'^create/$', recipes.views.create,
        name='recipes_recipe_create'),
    url(r'^edit/(?P<slug>[-\w]+)/$', recipes.views.edit, 
        name='recipes_recipe_edit'),
]