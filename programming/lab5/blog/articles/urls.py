from django.urls import path
from . import views
from .views import archive, get_article, create_post

urlpatterns = [
    path('', views.archive, name='archive'),
    path('article/<int:article_id>/', get_article, name='get_article'),
    path('article/new/', create_post, name='create_post'),
]