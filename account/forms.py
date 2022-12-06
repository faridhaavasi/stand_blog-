from django import forms
from django.contrib.auth.models import User

class loginform(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30)

