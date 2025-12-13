from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Animal
# Create your views here.

class HomeView(TemplateView):
    model = Animal
    template_name = "animals/animals.html"
    extra_context = {
        "title": " Animal Page"
    }