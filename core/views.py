from django.shortcuts import get_list_or_404, get_object_or_404, render
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Question, Answer, User
from .serializers import AnswerSerializer, FavoritedQuestionSerializer, ListQuestionsSerializer, ProfileSerializer, QuestionDetailSerializer, QuestionSerializer, SecondAnswerSerializer, UserSerializer
from .custom_permissions import IsQuestionOwnerOrReadOnly
from django.contrib.postgres.search import SearchVector


class UserViewSet(DjoserUserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(ListAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(username=self.request.user)


class QuestionsViewSet(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.query_params.get("search"):
            search_term = self.request.query_params.get("search")
            queryset = Question.objects.annotate(search=SearchVector('title', 'owner__username')).filter(search=search_term)
            return queryset
        return super().get_queryset()


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
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            serializer_class = QuestionDetailSerializer
        if self.request.method == 'PUT':
            serializer_class = QuestionSerializer
        if self.request.method == 'PATCH':
            serializer_class = QuestionDetailSerializer
        return serializer_class
    
    # def get_queryset(self):
    #     question = get_object_or_404(Question, pk=self.kwargs.get('pk'))
    #     if question.answers.count > 0:

    #     return super().get_queryset()
    
    def partial_update(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk=self.kwargs.get('pk'))
        title = question.title
        favorited_by = question.favorited_by.add(self.request.user)
        kwargs['partial'] = True
        return self.update(request, title, favorited_by, *args, **kwargs,)

class CreateAnswersViewset(CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = SecondAnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FavoritedQuestionViewset(UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = FavoritedQuestionSerializer