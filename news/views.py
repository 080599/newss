from django.shortcuts import render, redirect
from .models import News

def index(request):
    news_list = News.objects.filter(published=True).order_by('-created_at')
    context = {'news_list': news_list}
    return render(request, 'news/index.html', context)

def news_detail(request, news_id):
    news = News.objects.get(pk=news_id)
    context = {'news': news}
    return render(request, 'news/news_detail.html', context)

def create_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        new_news = News(title=title, content=content)
        new_news.save()
        return redirect('news:index')
    else:
        return render(request, 'news/create_news.html')