from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog


# Create your views here.
class BlogView(ListView):
    template_name = 'blog/all_blogs.html'
    model = Blog
    context_object_name = 'blogs'
