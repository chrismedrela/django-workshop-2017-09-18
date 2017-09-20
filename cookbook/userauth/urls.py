from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^login/$', auth_views.login,
        {'template_name': 'userauth/login.html'},
        name='userauth_login'),
    url(r'^logout/$', auth_views.logout,
        {'next_page': reverse_lazy('recipes_recipe_index')},  # TODO
        name='userauth_logout'),
    url(r'^password-change/$', auth_views.password_change,
        {'template_name': 'userauth/password_change_form.html',
         'post_change_redirect': 'userauth_password_change_done'},
        name='userauth_password_change'),
    url(r'^password-change-done/$', auth_views.password_change_done,
        {'template_name': 'userauth/password_change_done.html'},
        name='userauth_password_change_done'),
]