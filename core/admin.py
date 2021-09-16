from core.models import User, Question, Answer
from django.contrib import admin

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created_at']
    pass

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['body', 'question', 'owner', 'created_at']
    pass