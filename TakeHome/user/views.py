from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import loginForm,signupForm
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
from django.contrib.auth.hashers import make_password

def home(request):
    return render(request=request, template_name='home.html')


@api_view(['GET'])
def dashBoard(request):
    return render(request=request, template_name='adminPortal.html')

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
                return redirect('http://127.0.0.1:8000/adminPortal')
            
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")

    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

@api_view(['GET'])
def logout(request):
    user = request.user
    if request.method == 'GET':
        if user.is_authenticated == True:
            auth.logout(request)
            request.session.flush()
            messages.success(request, ('You have are logged out now'))
            
            return redirect('http://127.0.0.1:8000')
        
        else:
            return Response({'message' : 'already logged out'})
    return Response({'message' : user.is_authenticated})

@api_view(['GET','POST'])
def signup(request):
    
    if request.method == 'POST':
        form = signupForm(request.POST)
        
        if form.is_valid():
            
                sign_up = form.save()
                sign_up.password = make_password(form.cleaned_data['password'])
                sign_up.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password')
                # user = auth.authenticate(username=username, password=raw_password)
                # auth.login(request, user)
                return redirect('http://127.0.0.1:8000')
            
    else:
        form = signupForm()
    return render(request, 'signup.html', {'form': form})




##############

@api_view(['POST'])
def loginApi(request):
    
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
        
            auth.login(request, user)
                
            return Response({'message': 'Login Successful'})
            
        else:
             return Response('message', 'invalid data')

    return Response({'message' : 'something'})

@api_view(['GET'])
def logoutApi(request):
    

    
    auth.logout(request)
            
            
    return Response({'message' : 'logged out'})
        
        # else:
        #     return Response({'message' : 'already logged out'})

@api_view(['POST'])
def signupApi(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        
        password = make_password(password)
        user = User(name=username,password=password)
        user.save()
        
        serializer = UserSerializer(user)

    return Response({'message' : serializer.data})


def hello(request):
    return HttpResponse('Hello World')


