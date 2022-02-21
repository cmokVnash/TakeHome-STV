from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import loginForm
from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.decorators import api_view
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def home(request):
    return render(request=request, template_name='home.html')

@api_view(['GET'])
def l(request):
    user = request.user
    user = auth.authenticate(username='nash',password='nash')
    auth.login(request, user)
    if user.is_authenticated:
        x = user.is_customer
        x= str(x)
    else:
        x = 'false'
    context = {'extreme' : 'inHerName', 'user' : x}
    #form = loginForm(request, data=request.POST)
    

    #return render(request=request, template_name="login.html", context= context)
    return Response(x)






@api_view(['GET','POST'])
def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('http://127.0.0.1:8000')
            
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")

    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

@api_view()
def logout(request):
    user = request.user

    if user.is_authenticated == True:
        auth.logout(request)
        messages.success(request, ('You have are logged out now'))
        
        return redirect('http://127.0.0.1:8000')

@api_view(['GET','POST'])
def signup(request):
    user = request.user
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            if not user.is_authenticated:
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password')
                user = auth.authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('http://127.0.0.1:8000')
            else:
                 messages.error(request,"Invalid username or password.")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def hello(request):
    return HttpResponse('Hello World')


