from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
# Create your views here.
from classroom.models import ClassRoom

class ClassRoomView(TemplateView):
    template_name = "classroom/classroom.html"
    extra_context = {
        'title': 'Classroom Page'
    }
    
class Classroom(ListView):
    model = ClassRoom
    context_object_name = 'classroom'
    template_name = 'classroom/classroom.html'