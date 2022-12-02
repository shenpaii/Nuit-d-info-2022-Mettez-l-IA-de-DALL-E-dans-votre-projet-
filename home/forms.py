from email.policy import default
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator


class ContactForm(forms.Form):

    email = forms.EmailField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    nom = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'},), required=False)

    sujet = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sujet'}), required=False)

    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'},))

    class Meta:
        model = None
        exclude = ()