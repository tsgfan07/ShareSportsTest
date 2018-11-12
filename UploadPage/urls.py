from django.conf.urls import url,include
from . import views
from django.urls import path, re_path
from .models import Article
urlpatterns = [
    #path('', views.index, name="index"),
    re_path('edit/(?P<pk>\d+)', views.article_edit, name="article_edit"),
	#re_path('(?P<pk>\d+)', DetailView.as_view(model=Article, template_name='SearchPage/article_post.html')),
	path('', views.article_new, name='article_new'),
]

# Create your views here.
