from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return HttpResponse('Hello, World!')

class HomeView(TemplateView):
    template_name = "home/welcome.html"

# def welcome(request):
#     return render(request, "home/welcome.html", {'today': datetime.today()})

class WelcomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {'today': datetime.today()}