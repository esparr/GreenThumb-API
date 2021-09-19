from django.shortcuts import get_list_or_404, get_object_or_404, render
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Question, Answer, User
from .serializers import AnswerSerializer, ListQuestionsSerializer, ProfileSerializer, QuestionDetailSerializer, QuestionSerializer, SecondAnswerSerializer, UserSerializer
from .custom_permissions import IsAnswerOwnerOrReadOnly, IsQuestionOwnerOrReadOnly
# Create your views here.

class UserViewSet(DjoserUserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(ListAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_class = [IsAuthenticated, IsQuestionOwnerOrReadOnly, IsAnswerOwnerOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(username=self.request.user)
        
class QuestionsViewSet(ListCreateAPIView):
    queryset = Question.objects.all().order_by("-created_at")
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            serializer_class = ListQuestionsSerializer
        return serializer_class
        
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class QuestionDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsQuestionOwnerOrReadOnly]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            serializer_class = QuestionDetailSerializer
        return serializer_class


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CreateAnswersViewset(CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer, **kwargs):
        question = get_object_or_404(Question, pk=self.kwargs.get('pk'))
        serializer.save(owner=self.request.user, question=question)


# SecondCreateAnswersViewset is a test to see if front end can pull pk to attach to question
class SecondCreateAnswersViewset(CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = SecondAnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)