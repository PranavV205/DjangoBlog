from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
    #views always need to return httpresponse or exception(render returns httpresponse in bg)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

