from django.shortcuts import redirect,render, get_object_or_404
# Create your views here.
# rest_framework imports
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import generics
# Serializers and model imports
from .serializers import QuestionSerializer, SurveySerializer,AnswerSerializer,SurveySerializer
from .models import Question,Answer,Survey


@api_view(['GET'])
def Home(request):
    
    return render(request=request,context={'Message':"Welcome"},template_name='home.html')

class SurveyView(APIView):

    
    
    def get(self, request):
        
        survey = Survey.objects.get(pk=1)
        serializer = SurveySerializer(survey)
        return Response({'serializer': serializer.data}, template_name='survey.html')

    def retrieve(self,request):
        survey = get_object_or_404(Survey)
        serializer = SurveySerializer(survey)
        return Response({'serializer': serializer.data}, template_name='survey.html')

    def post(self,request):
        survey = Survey()

        user = request.user
        

        if not user.is_authenticated:
            return Response({'message' : 'user not admin'})
        
        serializer = SurveySerializer(survey, data=request.POST)
        if not serializer.is_valid():
            return Response({'message' : 'invalid serializer'})
       
        serializer.save(user=user)

        return Response([serializer.data])
        




################
#QUESTION VIEWS#
################

@api_view(['GET'])
def questionForm(request):
    question = Question()
    serializer = QuestionSerializer(question)

    return render(request=request, context={'serializer' : serializer}, template_name='question.html')

@api_view(['GET'])
def questionRetrieveView(request,pk):
    key = pk
    return render(request=request, context={'message' : key}, template_name='question.html')

@api_view(['POST'])
def questionPost(request,pk):
    
    user = request.user

    if not user.is_authenticated:
        raise Exception("You do not have permission to add question")

    serializer = QuestionSerializer(request,data = request.POST)

    if not serializer.is_valid():
        raise Exception("Invalid Serializer")

    get_survey = Survey.objects.get(pk=pk)

    serializer.save(survey=get_survey)
    
    return render(request=request, context={'message' : serializer.data}, template_name='question.html')



    
        
   







