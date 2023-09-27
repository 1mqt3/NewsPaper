from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.PostsHome.as_view(), name='posts'),
    path('n/', views.PostsByType.as_view(post_type='n'), name='n_list'),
    path('p/', views.PostsByType.as_view(post_type='p'), name='p_list'),
    path('<str:post_type>/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path("<str:post_type>/create/", PostCreateView.as_view(), name="post_create"),
    path("<str:post_type>/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("<str:post_type>/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]