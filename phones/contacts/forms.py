from django import forms
from .models import PhoneNumber


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField(label='E-mail')


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['number']


class LoginForm(forms.Form):
    name = forms.CharField(max_length=100)
    pwd = forms.CharField(widget=forms.PasswordInput, max_length=100)