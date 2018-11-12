from django.conf.urls import url,include
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
	path('contact/', views.contact, name="contact"),
    path('signup/', views.signup, name='signup'),
]

# Create your views here.
