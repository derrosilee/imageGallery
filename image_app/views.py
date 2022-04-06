from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.

def home(request):
     return render(request, "image_app\home.html")
 
 

def index(request):
    batch1 = Batch1.objects.all()
    context = {
        "batch1": batch1
    }
    return render(request, "image_app/index.html", context)


def index2(request):
    batch2 = Batch2.objects.all()
    context = {
        "batch2": batch2
    }
    return render(request, "image_app/index2.html", context)


def index3(request):
    batch3 = Batch3.objects.all()
    context = {
        "batch3": batch3
    }
    return render(request, "image_app/index3.html", context)


def index4(request):
    batch4 = Batch4.objects.all()
    context = {
        "batch4": batch4
    }
    return render(request, "image_app/index4.html", context)


def index5(request):
    batch5 = Batch5.objects.all()
    context = {
        "batch5": batch5
    }
    return render(request, "image_app/index5.html", context)
