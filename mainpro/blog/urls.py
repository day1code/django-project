from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('blog_list', views.blog_list, name="blog_list"),
] 
