
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Question(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions', null=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # favorited
    
    def __str__(self):
            return f"{self.title}"

class Answer(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_answers', null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_answers', null=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # accepted 
    # favorted

    def __str__(self):
        return f"{self.body}"