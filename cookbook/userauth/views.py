from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

def register(request, 
             template_name='userauth/register.html', 
             next_page_name='/'):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(next_page_name))
    else:  # GET method
        form = UserCreationForm()
    return render(request, template_name, {'form': form})