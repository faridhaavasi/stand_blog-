from django.shortcuts import render, redirect

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
    return render(request ,'account/register.html', {})
