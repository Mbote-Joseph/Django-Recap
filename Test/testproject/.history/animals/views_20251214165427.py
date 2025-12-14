from django.shortcuts import render
from django.views.generic import ListView, DetailView

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