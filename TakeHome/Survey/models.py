from django.db import models
from user.models import User
# Create your models here.

#s
class Survey(models.Model):
    name = models.CharField(max_length=100)
    user = models.ManyToManyField(User,null=True,blank=True)
    
    def __self__(self):
        return self.name

class Question(models.Model):
    question = models.TextField()
    def_answer = models.TextField()
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __self__(self):
        return self.question



class Answer(models.Model):

    answer = models.TextField()
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
        
    def __self__(self):
        return self.answer