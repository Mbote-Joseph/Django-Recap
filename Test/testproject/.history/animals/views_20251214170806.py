from django import forms
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from .models import Animal
# Create your views here.

class AnimalView(ListView):
    model = Animal
    context_object_name = "animals"
    template_name = "animals/animals.html"
    extra_context = {
        "title": " Animal Page"
    }
     
class AnimalDetailView(DetailView):
    model = Animal
    context_object_name = "animal"
    template_name = "animals/animal_detail.html"
    extra_context = {
        "title": " Animal Detail Page"
    }
    
class AnimalCreateView(CreateView):
    model = Animal
    fields = '__all__'
    template_name = "animals/animal_form.html"
    extra_context = {
        "title": " Create Animal Page"
    }
    success_url = '/animals'
    labels = {
        'name': 'Animal Name',
        'species': 'Animal Species',
        'age': 'Animal Age',
        'location': 'Animal Location',
    }
    widgets ={
        'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Animal Name'}),
        'species': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Animal Species'}),
        'age': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter Animal Age'}),
        'location': forms.Select(attrs={'class':'form-control', 'placeholder':'Select Animal Location'}),
    }
    
class AnimalUpdateView(UpdateView):
    model = Animal
    fields = '__all__'
    template_name = "animals/animal_form.html"
    extra_context = {
        "title": " Update Animal Page"
    }
    success_url = '/animals'
    labels = {
        'name': 'Animal Name',
        'species': 'Animal Species',
        'age': 'Animal Age',
        'location': 'Animal Location',
    }
    widgets ={
        'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Animal Name'}),
        'species': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Animal Species'}),
        'age': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter Animal Age'}),
        'location': forms.Select(attrs={'class':'form-control', 'placeholder':'Select Animal Location'}),
    }
    
class AnimalDeleteView(DeleteView):
    model = Animal
    context_object_name = "animal"
    template_name = "animals/animal_confirm_delete.html"
    extra_context = {
        "title": " Delete Animal Page"
    }
    success_url = '/animals'    