from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Project


# Create your views here.
class HomePage(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'portfolio/home.html'
