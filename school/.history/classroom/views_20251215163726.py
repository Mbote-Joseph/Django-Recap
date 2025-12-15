from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
# Create your views here.

class ClassRoomView(TemplateView):
    template_name = "classroom/classroom.html"
    extra_context = {
        'title': 'Classroom Page'
    }