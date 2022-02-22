from django.urls import path, include,re_path
from .views import Home, SurveyView, questionForm, questionPost, questionRetrieveView, surveyForm, adminPortal
from .viewsApi import QuestionCreate, QuestionList, QuestionRetrieve, SurveyCreate, SurveyList, SurveyRetrieve

urlpatterns = [
    
    path('',Home),

    path('adminPortal', adminPortal),

    #survey http urls
    path('survey/', surveyForm),
    path('survey/question', questionForm),
    path('survey/question/<int:pk>', questionRetrieveView),
    path('survey/question/<int:pk>/create', questionPost),
    
    #apiurls
        #SURVEY
    path('api/survey-list', SurveyList ),
    path('api/survey/<int:pk>', SurveyRetrieve),
    path('api/survey/create', SurveyCreate),

        #QUESTIONS

    re_path(r'^api/survey/(?P<survey_id>\d+)/questions/(?P<ques_id>\d+)', QuestionRetrieve ),
    path('api/survey/<int:pk>/questions', QuestionList),
    path('api/survey/<int:pk>/question-create', QuestionCreate),

    
]