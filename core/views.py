from rest_framework import permissions
from core.custom_permissions import IsAnswerOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.postgres.search import SearchVector
from .models import Question, Answer, User
from .serializers import AnswerSerializer, ListAnswerSerializer, ListQuestionsSerializer, ProfileSerializer, QuestionDetailSerializer, QuestionSerializer, UserSerializer



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
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            serializer_class = QuestionDetailSerializer
        if self.request.method == 'PUT':
            serializer_class = QuestionSerializer
        if self.request.method == 'PATCH':
            serializer_class = QuestionDetailSerializer
        return serializer_class
    
    def has_permissions(self):
        if self.request.method == 'PUT':
            permission_classes = [IsAuthenticated]
        if self.request.method == 'PATCH':
            permission_classes = [IsAuthenticated]
        if self.request.method == 'DELETE':
            permission_classes = [IsAuthenticated]
        return [permission(permission_classes) for permission in self.permission_classes]
    
    def partial_update(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk=self.kwargs.get('pk'))
        title = question.title
        favorited_by = question.favorited_by.add(self.request.user)
        kwargs['partial'] = True
        return self.update(request, title, favorited_by, *args, **kwargs,)

class CreateAnswersViewset(CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AnswersViewset(RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = ListAnswerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
