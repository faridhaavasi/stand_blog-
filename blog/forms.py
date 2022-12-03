from django import forms
from django.core.validators import ValidationError
# contactus form

class Contactusform(forms.Form):
    email = forms.EmailField(label='email')
    subject = forms.CharField(max_length=20, label='subject')
    text = forms.CharField(max_length=555, label='text')

    def clean(self):
        email = self.cleaned_data.get('email')
        if '@gmail.com' in email:
            raise ValidationError('gmail.com is con not in email', code='gmail error')

    def clean_text(self):
        subject = self.cleaned_data.get('subject')
        text = self.cleaned_data.get('text')
        if text == subject:
            raise ValidationError('text = subject ', code='text error')



