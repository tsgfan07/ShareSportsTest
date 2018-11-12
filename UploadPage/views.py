from django.shortcuts import render, get_object_or_404
from .models import Article
from .upload_form import ArticleForm
from django import forms
from django.utils import timezone





# Create your views here.
def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.title  = form.cleaned_data['title']
            article.body = form.cleaned_data['body']
            article.image = form.cleaned_data['image']
            article.contact_email = form.cleaned_data['contact_email']
            article.contact_phone = form.cleaned_data['contact_phone']
            article.category = form.cleaned_data['status']
            article.location = form.cleaned_data['location']
            article.location = article.geo_location()
            article.location_latitude = article.location.latitude
            article.location_longitude = article.location.longitude
            article.date = timezone.now()
            article.save()
            #form.save_m2m()
            return render(request, 'personal/home.html')
    else:
        form = ArticleForm(request.POST, request.FILES)
        return render(request, 'UploadPage/article_edit.html', {'form': form})
# Create your views here.

def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.title = form.cleaned_data['title']
            article.body = form.cleaned_data['body']
            article.image = form.cleaned_data['image']
            article.contact_email = form.cleaned_data['contact_email']
            article.contact_phone = form.cleaned_data['contact_phone']
            #article.tags = form.cleaned_data['tags']
            article.date = timezone.now()
            article.save()
            #form.save_m2m()
            return render(request, 'personal/home.html')
    else:
        form = ArticleForm(request.POST, request.FILES, instance=article)
    return render(request, 'UploadPage/article_edit.html', {'form': form, 'pk': pk})


