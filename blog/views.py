from django.shortcuts import render
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post


# Create your views here.

def index(request):
    latest_post_list = Post.objects.order_by('-date')
    return render(request, 'blog/index.html', {'latest_post_list': latest_post_list})

def create(request):
    return HttpResponse('Post Create')

def detail(request, post_id):
    selected_post = Post.objects.get(pk=post_id)
    return render(request, 'blog/detail.html', {'selected_post': selected_post})
    
def update(request):
    return HttpResponse('Post Update')

def delete(request):
    return HttpResponse('Post Delete')