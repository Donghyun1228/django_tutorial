from django.shortcuts import render
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    return HttpResponse("Dooboo blog")