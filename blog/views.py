from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from .models import Post


def post_new(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date = timezone.now()
            post.save()
        return render(request, 'blog.html')
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
# Create your views here.

def post_edit(request, pk):

    post = get_object_or_404(Post, pk=pk)
    if True:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('blog/', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
