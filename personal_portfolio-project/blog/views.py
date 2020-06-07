from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog
from portfolio.models import Project


# Create your views here.
class BlogView(ListView):
    template_name = 'blog/all_blogs.html'
    model = Blog
    context_object_name = 'blogs'
    # The code bellow will grap latest 2 post from all other posts in batabase.
    queryset = Blog.objects.order_by('-date')[:2]

    def get_queryset(self):
        return Blog.objects.order_by('-date')[:2]

    def get_context_data(self, *, object_list=None, **kwargs):
        """With This I can get objects from multiple models"""
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context

