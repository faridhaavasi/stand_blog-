from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import loginform, editform, register_form
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')
    if request.method == 'POST':
        form = loginform(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(User, username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))

            login(request, user)
            return redirect('home_app:home')
    else:
        form = loginform()

    return render(request, 'account/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home_app:home')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')
    form = register_form()
    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            user = User.objects.create(username=username, password=password1)
            login(request, user)
            return redirect('home_app:home')

    return render(request, 'account/register.html', {'form': form})


def edit_user(request):
    user = request.user
    form = editform(instance=user)
    if request.method == 'POST':
        form = editform(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'account/edit_info_user.html', {'form': form})
