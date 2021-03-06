"""questionbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from core import views as api_views


router = SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/', include(router.urls)),
    path('auth/users/', api_views.DjoserUserViewSet.as_view({'get': 'list'}), name='register-new-user'),
    path('auth/users/me', api_views.ProfileViewSet.as_view(), name='user-profile'),
    path('api/questions/', api_views.QuestionsViewSet.as_view(), name='questions-list'),
    path('api/questions/<int:pk>/', api_views.QuestionDetailViewSet.as_view(), name='questions-detail'),
    path('api/answers/new', api_views.CreateAnswersViewset.as_view(), name='answer-new'),
    path('api/answers/<int:pk>/', api_views.AnswersViewset.as_view(), name='answers-detail')
]
