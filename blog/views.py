from django.shortcuts import render, get_object_or_404
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import PostForm


# Create your views here.

def index(request):
    latest_post_list = Post.objects.order_by('-date')
    return render(request, 'blog/index.html', {'latest_post_list': latest_post_list})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:index'))

    else:
        form = PostForm()        
        return render(request, 'blog/create.html', {'form' : form})

def detail(request, post_id):
    selected_post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'selected_post': selected_post})

def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:detail', args=(post.id,)))
    
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/update.html', {'form' : form})

def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('blog:index'))