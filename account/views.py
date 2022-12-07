from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import loginform
from django.contrib.auth import authenticate ,login, logout

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')
    if request.method == 'POST':
        form = loginform(data=request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))

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
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user = User.objects.create(username=username, password=password1)
        if username and password1:
            login(request, user)
            return redirect('home_app:home')

    return render(request, 'account/register.html')


