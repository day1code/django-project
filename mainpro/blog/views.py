from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    # print(blogs)
    return render(request, "blog_list.html", {'blogs': blogs})