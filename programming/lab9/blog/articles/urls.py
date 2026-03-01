from django.urls import path
from . import views
from .views import archive, get_article, create_post, register,user_login,user_logout

urlpatterns = [
    path('', views.archive, name='archive'),
    path('article/<int:article_id>/', get_article, name='get_article'),
    path('article/new/', create_post, name='create_post'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]