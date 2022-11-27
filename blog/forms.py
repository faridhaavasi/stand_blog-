from django import forms

# contactus form

class Contactusform(forms.Form):
    name = forms.CharField(max_length=50, label='name')
    email = forms.EmailField(label='email')
    subject = forms.CharField(max_length=20, label='subject')
    text = forms.CharField(max_length=555, label='text')
