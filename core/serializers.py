from django.utils.timezone import localtime
from core.models import Question, Answer, User
from rest_framework import serializers
from django.db.models import Count, fields


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")

class AnswerNumberSerializer(serializers.ModelSerializer):
    answer_count = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.DateTimeField(format='%b. %d, %Y at %I:%M %p', read_only=True)
    
    class Meta:
        model = Answer
        fields = ("answer_count",)

    def get_total_(self, obj):
        return Question.objects.annotate(number_of_answers=Count('answers'))

class ListAnswerSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(read_only=True, slug_field="username")
    created_at = serializers.DateTimeField(format='%b. %d, %Y at %I:%M %p', read_only=True)
    favorited_by = serializers.SlugRelatedField(many=True, read_only=True, slug_field="username")
    class Meta:
        model = Answer
        fields = (
            "pk",
            "body",
            "created_at",
            "accepted",
            "owner",
            "question",
            "favorited_by",
            )


class ListQuestionsSerializer(serializers.ModelSerializer):
    answer_count = serializers.SerializerMethodField('get_total_answers')
    owner = serializers.SlugRelatedField(read_only=True, slug_field="username")
    created_at = serializers.DateTimeField(format='%b. %d, %Y at %I:%M %p', read_only=True)
    favorited_by = serializers.SlugRelatedField(many=True, read_only=True, slug_field="username")

    def get_total_answers(self, obj):
        # answer_count = Question.objects.get(pk=obj.pk).answers.count()
        question = Question.objects.get(pk=obj.pk)
        answer_count = question.answers.aggregate(Count('id'))
        return answer_count

    class Meta:
        model = Question
        fields = (
            "pk",
            "title",
            "owner",
            "created_at",
            "favorited_by",
            "answer_count",
        )

class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(read_only=True, slug_field="username")
    created_at = serializers.DateTimeField(format='%b. %d, %Y at %I:%M %p', read_only=True)
    class Meta:
        model = Question
        fields = (
            "pk",
            "title",
            "body",
            "owner",
            "created_at",
        )

class QuestionDetailSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(read_only=True, slug_field="username")
    created_at = serializers.DateTimeField(format='%b. %d, %Y at %I:%M %p', read_only=True)
    answers = ListAnswerSerializer(many=True, read_only=True)
    favorited_by = serializers.SlugRelatedField(many=True, read_only=True, slug_field="username")
    class Meta:
        model = Question
        fields = (
            "pk",
            "title",
            "body",
            "owner",
            "created_at",
            "favorited_by",
            "answers",
        )

