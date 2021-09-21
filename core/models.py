
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class User(AbstractUser):
    
    USER_CREATE_PASSWORD_RETYPE = True
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username
    pass

class Tag(models.Model):
    insert = models.CharField(max_length=32)

class Question(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions', null=True)
    title = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    favorited_by = models.ManyToManyField(User, related_name="fav_questions", blank=True)
    tags = models.ManyToManyField(Tag, related_name='questions', blank=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
            return f"{self.title}"

class Answer(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers', null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', null=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    favorited_by = models.ManyToManyField(User, related_name="fav_answers", blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.body}"
