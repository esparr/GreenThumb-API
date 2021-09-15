from core.models import Question, Answer, User
from rest_framework import serializers

class AnswerNumberSerializer(serializers.ModelSerializer):
     class Meta:
        model = Answer
        fields = ("date", "note",)

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