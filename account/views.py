from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_user(request):
    if request.user.is_authenticated is True:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'account/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('/')

def register(request):
    context = {
        'errors': [],
    }
    if request.user.is_authenticated is True:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            context['errors'].append('passwords is not match')
            return render(request, 'account/register.html', context)
        user = User.objects.create(username=username, password=password1)
        login(request, user)

    return render(request, 'account/register.html', {})
