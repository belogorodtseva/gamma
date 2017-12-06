from django import forms
from django.contrib.admin import widgets

class ContactForm(forms.Form):
    name= forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
