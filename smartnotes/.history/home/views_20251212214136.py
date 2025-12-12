from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView

# Create your views here.
def home(request):
    return HttpResponse('Hello, World!')

# def welcome(request):
#     return render(request, "home/welcome.html", {'today': datetime.today()})

class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {'today': datetime.today()}