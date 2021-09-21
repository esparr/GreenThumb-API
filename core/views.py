from django.shortcuts import get_list_or_404, get_object_or_404, render
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Question, Answer, User
from .serializers import AnswerSerializer, ListQuestionsSerializer, ProfileSerializer, QuestionDetailSerializer, QuestionSerializer, SecondAnswerSerializer, UserSerializer
from .custom_permissions import IsQuestionOwnerOrReadOnly
from django.contrib.postgres.search import SearchVector
# Create your views here.

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
    permission_classes = [IsAuthenticatedOrReadOnly, IsQuestionOwnerOrReadOnly]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            serializer_class = QuestionDetailSerializer
        return serializer_class

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