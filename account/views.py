from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'account/login.html', {})