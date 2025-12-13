from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Animal
# Create your views here.

class HomeView(TemplateView):
    model = Animal
    context_object_name = "animals"
    template_name = "animals/animals.html"
    extra_context = {
        "title": " Animal Page"
    }
    