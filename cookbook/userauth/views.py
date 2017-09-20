from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User

import requests

def register(request, 
             template_name='userauth/register.html', 
             next_page_name='/'):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_mail(
                'A new user has registered',
                'Here is the message: {}'.format(user.username),
                'from@email.com',
                ['your@email.com'],
                fail_silently=False,
            )
            messages.success(request, 'Your account was created.')
            login(request, user)
            return HttpResponseRedirect(reverse(next_page_name))
    else:  # GET method
        form = UserCreationForm()
    return render(request, template_name, {'form': form})

def login_view(request, template_name):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
    
        try:
            r = requests.get('https://api.github.com/user', auth=(username, password))
        except Exception:
            messages.error(request, 'Sorry. :-(')
        else:
            password_is_correct = (r.status_code == 200)

            if password_is_correct:
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    user = User.objects.create_user(username=username, password=None)
                login(request, user)
                return HttpResponseRedirect(reverse('recipes_recipe_index'))
            else:
                messages.error(request, 'Invalid password')
                form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, template_name, {'form': form})
