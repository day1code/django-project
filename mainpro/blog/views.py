from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog
from .form import BlogForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    # print(blogs)
    return render(request, "blog_list.html", {'blogs': blogs})

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES) # Include FILES for image uploads
        if form.is_valid():
            blog = form.save(commit = False)
            blog.user = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()  # Create a new form instance
           
    return render(request, "blog_form.html", {'form': form})

def blog_edit(request , blog_id):
    blog = get_object_or_404(Blog, pk=blog_id, user= request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES) # Include FILES for image uploads
        if form.is_valid():
            blog = form.save(commit = False)
            blog.user = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)  # Create a new form instance 
    return render(request, "blog_form.html", {'form': form})


