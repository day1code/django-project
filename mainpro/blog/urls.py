from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name="index"),
    path('blog_list', views.blog_list, name="blog_list"),
    path('blog_create/', views.blog_create, name="blog_create"),
    path('<int:blog_id>/edit/', views.blog_edit, name="blog_edit"),
] 
