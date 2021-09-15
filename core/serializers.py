from core.models import Question, Answer, User
from rest_framework import serializers
from django.db.models import Count


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("username", "email")

class AnswerNumberSerializer(serializers.ModelSerializer):
    answer_count = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Answer
        fields = ("answer_count",)
    
    def get_total_(self, obj):    
        return Question.objects.annotate(number_of_answers=Count('answers'))

class ListQuestionsSerializer(serializers.ModelSerializer):
    answer_count = serializers.SerializerMethodField('get_total_answers')
    owner = serializers.SlugRelatedField(read_only=True, slug_field="username")

    def get_total_answers(self, obj):
        answer_count = Question.objects.get(pk=obj.pk).answers.count()
        return answer_count

    
    class Meta:
        model = Question
        fields = (
            "pk",
            "title",
            "owner",
            "created_at",
            "answer_count",
        )

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "pk",
            "title",
            "body",
            "owner",
            "created_at",
        )