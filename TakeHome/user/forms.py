from enum import unique
from django import forms

class loginForm(forms.Form):
    
    email = forms.EmailField(required=True)
    
    password = forms.CharField(widget=forms.PasswordInput())

    


class register(forms.Form):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())


    