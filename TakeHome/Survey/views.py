from django.shortcuts import render
from .serializers import QuestionSerializer,AnswerSerializer,SurveySerializer
# Create your views here.
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView

class questionView(APIView):

    def get(request):
        pass

    def post(request):
        pass



