from django import forms
from .models import Ticket
from django.core.validators import ValidationError
# contactus form

class Contactusform(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'subject'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }





    def clean(self):
        email = self.cleaned_data.get('email')
        if '@gmail.com' in email:
            raise ValidationError('gmail.com is con not in email', code='gmail error')

    def clean_text(self):
        subject = self.cleaned_data.get('subject')
        text = self.cleaned_data.get('text')
        if text == subject:
            raise ValidationError('text = subject ', code='text error')



