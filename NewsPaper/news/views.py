from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

from .models import Post

menu = ["Главная страница", "Посты"]

def index(request):
    return render(request, 'news/index.html', {'menu': menu, 'title': 'Главная страница'})

def posts(request):
    posts = Post.objects.order_by('-created')
    return render(request, 'news/posts.html', {'posts': posts})

class NewsDetailView(DetailView):
    model = Post
    template_name = 'news/details_view.html'
    context_object_name = 'post'

def post(request, post_id):
    return HttpResponse(f'Пост {post_id}')