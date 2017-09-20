from django.conf.urls import include, url

import recipes.views

urlpatterns = [
    url(r'^recipe/(?P<slug>[-\w]+)/$', recipes.views.detail, 
        name='recipes_recipe_detail'),
    url(r'^$', recipes.views.index,
        name='recipes_recipe_index'),
]