from core.models import Question, Answer, User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")

class AnswerNumberSerializer(serializers.ModelSerializer):
     class Meta:
        model = Answer
        fields = ("answer_count",)

class ListQuestionsSerializer(serializers.ModelSerializer):
    question_answers = AnswerNumberSerializer(many=True, read_only=False)
    class Meta:
        model = Answer
        fields = (
            "pk",
            "title",
            "owner",
            "created_at",
            "answer",
        )