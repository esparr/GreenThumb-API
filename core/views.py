from django.shortcuts import render
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Question, Answer, User
from .serializers import ListQuestionsSerializer, QuestionDetailSerializer, QuestionSerializer, UserSerializer
from .custom_permissions import IsQuestionOwnerOrReadOnly, IsAnswerOwnerOrReadOnly

# Create your views here.

class UserViewSet(DjoserUserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuestionsViewSet(ModelViewSet):
    queryset = Question.objects.all().order_by("-created_at")
    serializer_class = QuestionSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            serializer_class = ListQuestionsSerializer
        return serializer_class
        
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class QuestionDetailViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsQuestionOwnerOrReadOnly]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            serializer_class = QuestionDetailSerializer
        return serializer_class

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(reader=self.request.user)

    def perform_create(self, serializer):
        serializer.save(reader=self.request.user)


# questions_list = QuestionsViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })

# questions_detail = QuestionDetailViewSet.as_view({
#     'get': 'retrieve',
#     'post': 'create',
#     'put': 'update',
#     'delete': 'destroy',
# })