from django.shortcuts import redirect,render, get_object_or_404
from django.core import serializers
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
from django.core.exceptions import ValidationError

import json

###SURVEY

@api_view(['GET'])
def SurveyList(request):
    
    survey_list = Survey.objects.values()
    
    #list_data = serializers.serialize('json',list(context),fields=('name'))

    return Response({'data-set': survey_list})

@api_view(['GET'])
def SurveyRetrieve(request,pk):
    survey = Survey.objects.get(pk=pk)
    serializer = SurveySerializer(survey)

    return Response({'data' : serializer.data})

@api_view(['POST'])
def SurveyCreate(request):

    survey = Survey()
    
    user = request.user
        
    if not user.is_authenticated:
        return Response({'message' : 'user not admin'})
        
    serializer = SurveySerializer(survey, data=request.POST)
    if not serializer.is_valid():
         return Response({'message' : 'invalid serializer'})
       
    serializer.save(user=user)

    return Response(serializer.data)    


###QUESTIONS



@api_view(['GET'])
def QuestionList(request,pk):
    
    survey = Survey.objects.get(pk=pk)

    Question_list = Question.objects.values()
    
    #list_data = serializers.serialize('json',list(context),fields=('name'))

    return Response({'data-set': Question_list})

@api_view(['GET'])
def QuestionRetrieve(request,survey_id,ques_id):
    
    survey = Survey.objects.get(pk=survey_id)

    

    question = Question.objects.filter(survey_id=survey_id).values()
    
    serializer = QuestionSerializer({'data-set': question})

    return Response({'dataset' : question})

@api_view(['POST'])
def QuestionCreate(request,pk):

    question = Question()
    
    user = request.user
    
    survey = Survey.objects.get(pk=pk)
    
    
    # return Response(data)

    if not user.is_authenticated:
        return Response({'message' : 'user not admin'})
        
    serializer = QuestionSerializer(question, data=request.POST)
    if not serializer.is_valid():
        #  return Response({'message' : 'invalid serializer'})
        raise ValidationError(serializer.errors)
       
    serializer.save(survey=survey)

    return Response(serializer.data) 