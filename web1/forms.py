from web1.models import mails
from django.core import validators
from django import forms
from .models import mails


class SendingEmail(forms.ModelForm):
    class Meta:
        model = mails
        fields = ['name','email','c_number', 'message']

        widgets = {
            'Name': forms.TextInput(attrs={'class':'form-control'}),
            'Email': forms.EmailInput(attrs={'class':'form-control'}),
            'Phone Number': forms.NumberInput(attrs={'class':'form-control'}),
            'Message': forms.Textarea(attrs={'class':'form-control'}),
        }
