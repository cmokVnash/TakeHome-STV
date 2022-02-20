from django import forms

class loginForm(forms.Form):
    
    email = forms.EmailField(required=True)
    
    password = forms.CharField(widget=forms.PasswordInput())

    


class register(forms.Form):
    email = forms.EmailField(label='Email')
    name = forms.CharField(label='Name')
    password = forms.CharField(widget=forms.PasswordInput())


    