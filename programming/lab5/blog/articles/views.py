from django.shortcuts import render
from django.http import Http404
from .models import Article

def archive(request):
    posts = Article.objects.all()           
    return render(request, "archive.html", {"posts": posts})

def get_article(request, article_id):
       try:
           post = Article.objects.get(id=article_id)
           return render(request, 'article.html', {'post': post})
       except Article.DoesNotExist:
           raise Http404("Статья не найдена")
       
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Article, ArticleForm

def create_post(request):
   if not request.user.is_authenticated:
       raise Http404("Доступ запрещен")

   if request.method == "POST":
       form = ArticleForm(request.POST)
       if form.is_valid():
           article = form.save(commit=False)
           article.author = request.user
           article.save()
           return redirect(reverse('get_article', kwargs={'article_id': article.id}))
   else:
       form = ArticleForm()

   return render(request, 'create_post.html', {'form': form})
   