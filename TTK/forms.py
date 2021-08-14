from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = CONTACT
        fields = '__all__'
