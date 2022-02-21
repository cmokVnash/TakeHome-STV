from rest_framework import serializers
from .models import Survey,Question,Answer

class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = ('__all__')#['user']

        # def set_user(self,request):
        #     self.user = request.user
        
        # def create(self, validated_data):
        #     validated_data['user_id'] = self.user.id
        #     return super().create(validated_data)
        

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('__all__')

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('__all__')

