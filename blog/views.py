from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def index(request):
    context = {
        'blogs' : Blog.objects.all()
    }
    return render(request, 'blog/home.html', context)
