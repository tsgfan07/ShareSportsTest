from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, re_path
from django.views.generic import ListView, DetailView
from UploadPage.models import Article
from django.views.static import serve

urlpatterns = [
    path("", views.index, name="search_index"),
    re_path('(?P<pk>\d+)', DetailView.as_view(model=Article, template_name='SearchPage/article_post.html')),
    path('search', views.search, name="search"),
    path('categories', views.category_view, name="category_view")
    #re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# Create your views here.
