from django.shortcuts import get_list_or_404, get_object_or_404, render
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Question, Answer, User
from .serializers import AnswerSerializer, ListQuestionsSerializer, QuestionDetailSerializer, QuestionSerializer, UserSerializer
from .custom_permissions import IsAnswerOwnerOrReadOnly, IsQuestionOwnerOrReadOnly
# Create your views here.

class UserViewSet(DjoserUserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsQuestionOwnerOrReadOnly, IsAnswerOwnerOrReadOnly]


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
    permission_classes = [IsAuthenticated, IsQuestionOwnerOrReadOnly]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            serializer_class = QuestionDetailSerializer
        return serializer_class

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CreateAnswersViewset(CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer, **kwargs):
        question = get_object_or_404(Question, pk=self.kwargs.get('pk'))
        serializer.save(owner=self.request.user, question=question)
        
class SecondCreateAnswersViewset(CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)