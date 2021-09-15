from django.shortcuts import render
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Question, Answer, User
from .serializers import ListQuestionsSerializer
from django.db.models import Count

# Create your views here.

# class UserViewSet(DjoserUserViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class QuestionsViewSet(ModelViewSet):
    queryset = Question.objects.all().order_by("-created_at")
    serializer_class = ListQuestionsSerializer
