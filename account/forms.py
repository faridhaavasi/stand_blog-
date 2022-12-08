from django import forms
from django.contrib.auth.models import User
from django.core.validators import ValidationError
from django.contrib.auth import authenticate
class loginform(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'input100',
               'placeholder': 'username',
               }
        ))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(
        attrs={
            'class': 'input100',
            'placeholder': 'password'
             }

        ))

    def clean_passwoord(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('password')

        else:
            raise ValidationError('username or password invalid ')



class editform(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')