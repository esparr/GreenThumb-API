from core.models import Question, Answer, User
from rest_framework import serializers
from django.db.models import Count


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("username", "email")

class AnswerNumberSerializer(serializers.ModelSerializer):
    answer_count = serializers.SerializerMethodField('get_count')
    class Meta:
        model = Answer
        fields = ("answer_count")
    
    def get_count(self, obj):    
        return Question.objects.annotate(number_of_answers=Count('answer'))

class ListQuestionsSerializer(serializers.ModelSerializer):
    answer_count = AnswerNumberSerializer(many=True, read_only=True)
    owner = serializers.SlugRelatedField(read_only=True, slug_field="username")
    class Meta:
        model = Question
        fields = (
            "pk",
            "title",
            "owner",
            "created_at",
            "answer",
        )