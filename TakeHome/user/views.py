from django.http import HttpResponse
from django.shortcuts import render
from .forms import login
from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

def hello(request):



    return HttpResponse('Hello World')

def index(request):
    loginForm = login()
    context ={'form' : loginForm}
    return render(request, 'test.html', context)

class usersList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]

    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        

        return Response(serializer.data)
