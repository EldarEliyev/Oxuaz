from django.shortcuts import render
from.models import Article

def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

def article_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'article_detail.html', {'article': article})


