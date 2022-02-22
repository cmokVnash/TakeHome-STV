from enum import unique
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User
class loginForm(forms.Form):
    
    email = forms.EmailField(required=True)
    
    password = forms.CharField(widget=forms.PasswordInput())

    


class signupForm(forms.ModelForm):

    

    email = forms.EmailField(required=True)
    name =  forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ["name", "password", "email"]

