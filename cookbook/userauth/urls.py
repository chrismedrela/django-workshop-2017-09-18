from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

from django.views.generic import TemplateView

import userauth.views

auth_views.login

urlpatterns = [
    url(r'^login/$', userauth.views.login_view,
        {'template_name': 'userauth/login.html'},
        name='userauth_login'),
    url(r'^logout/$', auth_views.logout,
        {'next_page': 'recipes_recipe_index'},
        name='userauth_logout'),
    url(r'^password-change/$', auth_views.password_change,
        {'template_name': 'userauth/password_change_form.html',
         'post_change_redirect': 'userauth_password_change_done'},
        name='userauth_password_change'),
    url(r'^password-change-done/$', auth_views.password_change_done,
        {'template_name': 'userauth/password_change_done.html'},
        name='userauth_password_change_done'),

    url(r'^register/$', userauth.views.register,
        {'next_page_name': 'userauth_register_done'},
        name='userauth_register'),
    url(r'^welcome/$',
        TemplateView.as_view(template_name='userauth/register_done.html'),
        name='userauth_register_done'),
]