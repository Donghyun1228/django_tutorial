from django.shortcuts import render, get_object_or_404
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm


# Create your views here.

# request를 받아 index 페이지로 연결
def index(request):

    page = request.GET.get('page', '1')
    latest_post_list = Post.objects.order_by('-date')
    paginator = Paginator(latest_post_list, 10)
    page_object = paginator.get_page(page)

    return render(request, 'blog/index.html', {'latest_post_list': page_object})

# create 페이지로 연결 / form으로 받은 데이터 처리 
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:index'))

    else:
        form = PostForm()        
        return render(request, 'blog/create.html', {'form' : form})

# detail 페이지로 연결
def detail(request, post_id):
    selected_post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'selected_post': selected_post})

# update 페이지로 연결해서 해당 PostForm 표시 / form으로 받은 데이터 처리
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

# Post를 삭제하고 index 페이지로 연결
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('blog:index'))
