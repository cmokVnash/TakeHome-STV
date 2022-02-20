from django import forms

class login(forms.Form):
    
    email = forms.EmailField(label='Email')
    
    password = forms.CharField(widget=forms.PasswordInput())

class register(forms.Form):
    email = forms.EmailField(label='Email')
    name = forms.CharField(label='Name')
    password = forms.CharField(widget=forms.PasswordInput())


    