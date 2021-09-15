from django.shortcuts import render
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Question, Answer, User
from .serializers import ListQuestionsSerializer, UserSerializer

# Create your views here.

class UserViewSet(DjoserUserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class QuestionsViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = ListQuestionsSerializer

    def get(self, request, format=None):
        answer_count = Answer.objects.count()
        content = {'answer_count': answer_count}
        return Response(content)
