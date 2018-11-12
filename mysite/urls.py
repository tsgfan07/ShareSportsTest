"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from django.urls import include
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


urlpatterns = [
	path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('', include('personal.urls')),
	path('blog/', include('blog.urls')),
    path('SearchPage/', include('SearchPage.urls')),
    path('UploadPage/', include('UploadPage.urls')),
    path('media/', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    path('login/', auth_views.LoginView.as_view(template_name="register/login.html"), name='login'), #login and
    path('logout/', auth_views.LogoutView.as_view(template_name='personal/home.html'), name='logout'),
    #path('signup/', auth_views.SignupView.as_view(template_name="register/login.html"), name='signup')#logout
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)