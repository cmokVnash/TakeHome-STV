from django.contrib import admin
from .models import Survey,Question,Answer
# Register your models here.


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class SurveyAdmin(admin.ModelAdmin):
    inlines = [ QuestionInline, ]


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline,]

admin.site.register(Survey,SurveyAdmin)
admin.site.register(Question,QuestionAdmin)



#admin.site.register([Survey,Question,Answer,SurveyAdmin])