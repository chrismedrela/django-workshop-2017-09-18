from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render


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