from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse

def homepage(request):
    return render(request, 'home/homepage.html')

