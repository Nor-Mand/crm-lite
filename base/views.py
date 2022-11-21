from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from . import forms


def Home(request):
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
                return redirect('leads:kanban-opportunity')
            else:
                message = 'Username or Password Incorrect.'
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'base.html', context)

