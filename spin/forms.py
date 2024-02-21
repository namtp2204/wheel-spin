
from django import forms
from .models import SpinCode

class SpinCodeForm(forms.ModelForm):
    class Meta:
        model = SpinCode  
        fields = ['code']
        widgets = {
            'code': forms.TextInput(attrs={'placeholder': 'Lucky code'}),
        }
