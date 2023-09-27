from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView


from .forms import PostForm, PostFilterForm
from .models import Post

menu = ["Главная страница", "Посты"]


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

        post_type = self.request.GET.get('post_type', None)
        if post_type:
            queryset = queryset.filter(post_type=post_type)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект формы.
        context['form'] = PostFilterForm(self.request.GET)
        return context


class NewsDetailView(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = "post"

    def get_queryset(self):
        post_type = self.kwargs['post_type']
        return Post.objects.filter(post_type=post_type)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news/news_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save()
        self.success_url = reverse(f'{self.kwargs["post_type"]}-detail', args=[self.object.pk])
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news/news_create.html'

    def get_queryset(self):
        return Post.objects.filter(post_type=self.kwargs['post_type'])

    def get_success_url(self):
        return reverse(f'{self.kwargs["post_type"]}-detail', args=[self.object.pk])


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'news/news_delete.html'

    def get_queryset(self):
        return Post.objects.filter(post_type=self.kwargs['post_type'])

    def get_success_url(self):
        return reverse("posts")
    
    
class PostsByType(ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "posts"
    paginate_by = 6
    post_type = None

    def get_queryset(self):
        return Post.objects.filter(post_type=self.post_type)