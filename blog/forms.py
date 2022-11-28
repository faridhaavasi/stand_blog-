from django import forms

# contactus form

class Contactusform(forms.Form):
    email = forms.EmailField(label='email')
    subject = forms.CharField(max_length=20, label='subject')
    text = forms.CharField(max_length=555, label='text')
