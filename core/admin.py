from core.models import User, Question, Answer
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

# Register your models here.


admin.site.register(User, UserAdmin)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'owner', 'created_at']
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['pk', 'body', 'question', 'owner', 'created_at']
    pass
