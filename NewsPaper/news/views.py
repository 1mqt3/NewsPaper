from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .filters import PostFilter
from .forms import PostForm

from .models import Post

menu = ["Главная страница", "Посты"]


# def index(request):
#     return render(request, 'news/index.html', {'menu': menu, 'title': 'Главная страница'})


class PostsHome(ListView):
    paginate_by = 3
    model = Post
    template_name = 'news/posts.html'
    context_object_name = 'posts'
    order_by = 'created'

    # Переопределяем функцию получения списка постов
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class NewsDetailView(DetailView):
    model = Post
    template_name = 'news/details_view.html'
    context_object_name = 'post'


# def post(request, post_id):
#     return HttpResponse(f'Пост {post_id}')


# def create_post(request):
#     form = PostForm()
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/posts/')
#     return render(request, 'news/news_create.html', {'form': form})


class NewsCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news/news_create.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.success_url = reverse('news-detail', args=[self.object.pk])
        return response


class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news/news_create.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('posts')