from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView
from django import template
# Create your views here.
from classroom.forms import ClassroomForm
from classroom.models import ClassRoom

# class ClassRoomView(TemplateView):
#     template_name = "classroom/classroom.html"
#     extra_context = {
#         'title': 'Classroom Page'
#     }
    
class ClassroomListView(ListView):
    model = ClassRoom
    context_object_name = 'classrooms'
    template_name = 'classroom/classroom.html'
    extra_context = {
        'title': 'Classroom Page'
    }

class ClassRoomDetailsView(DetailView):
    model = ClassRoom
    context_object_name = 'classroom'
    template_name = 'classroom/classroomdetails.html'
    extra_context = {
        'title': 'Classroom Details'
    }
    
class ClassroomCreate(CreateView):
    model = ClassRoom
    form_class = ClassroomForm
    fields = "__all__"
    template_name = "classroom/classroomform.html"
    success_url = "/classroom"
    extra_context = {
        'title': "Classroom Data Form"
    }
    

class ClassroomEdit(UpdateView):
    model = ClassRoom
    fields = "__all__"
    # context_object_name = 'classroom'
    template_name = "classroom/classroomform.html"
    success_url = "/classroom"
    extra_context = {
        'title': "Classroom Data Form" 
    }
    
class ClassroomDelete(DeleteView):
    model = ClassRoom
    context_object_name = 'classroom'
    template_name = 'classroom/classroom_confirm_delete.html'
    extra_context = {
        'title': 'Classroom Delete Page'
    }
    success_url = "/classroom"