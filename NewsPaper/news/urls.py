from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.PostsHome.as_view(), name='posts'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('create/', NewsCreate.as_view(), name='news_create')
]