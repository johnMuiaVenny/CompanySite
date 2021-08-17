from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = CONTACT
        fields = '__all__'


class MyProfile(forms.ModelForm):
    class Meta:
        model = PROFILE
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'Email':forms.EmailInput(attrs={'class':'form-control', 'style':"border-radius: 6px; border:2px solid skyblue; disabled"}),
            'FName':forms.TextInput(attrs={'class':'form-control', 'style':"border-radius: 6px; border:2px solid skyblue;"}),
            'LName':forms.TextInput(attrs={'class':'form-control', 'style':"border-radius: 6px; border:2px solid skyblue;"}),
            'Image':forms.FileInput(attrs={'class':'form-control', 'style':"border-radius: 6px; border:2px solid skyblue;"}),
        }

