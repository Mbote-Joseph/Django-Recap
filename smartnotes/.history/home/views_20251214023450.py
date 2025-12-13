from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = "home/login.html"
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    template_name = "home/logout.html"
    
    
    
# Create your views here.
# def home(request):
#     return HttpResponse('Hello, World!')

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home/welcome.html"
    login_url = "/login"

# def welcome(request):
#     return render(request, "home/welcome.html", {'today': datetime.today()})

class WelcomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {'today': datetime.today()}