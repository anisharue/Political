from django.urls import path
from django.views.generic import ListView, DetailView
from .models import Post

app_name = 'blog'

urlpatterns = [
    path('', (ListView.as_view(
        queryset=Post.objects.all().order_by("-date")[:25],
        template_name="blog.html",
    )), name='blog-home'),
    path('<int:pk>/', (DetailView.as_view(
        model=Post,
        template_name='post.html'
    )), name='post-detail'),
]