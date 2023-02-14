from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from . import forms


def home(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
                return redirect('crm:reports-view')
            else:
                message = 'Username or Password Incorrect.'
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'home.html', context)

