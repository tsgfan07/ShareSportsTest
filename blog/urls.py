from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from django.urls import path, re_path
from . forms import PostForm
from . import views

urlpatterns = [
    re_path('(?P<pk>\d+)/edit', views.post_edit, name="post_edit"),
	path('', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="blog/blog.html"), name='blog'),
	re_path('(?P<pk>\d+)', DetailView.as_view(model=Post, template_name='blog/post.html')),
	path('blog/new', views.post_new, name='post_new'),
	]
	

# Create your views here.
