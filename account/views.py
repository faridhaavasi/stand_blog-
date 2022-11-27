from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate ,login, logout

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(User, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_app:home')
    return render(request, 'account/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home_app:home')