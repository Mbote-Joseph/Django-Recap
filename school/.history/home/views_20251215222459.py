from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q

from classroom.models import ClassRoom

# Create your views here.
class HomeView(TemplateView):
    template_name = "home/home.html"
    extra_context = {
        'title': 'Home Page'
    } 
    
def global_search(request):
    query = request.GET.get('q')
    
    classrooms = ClassRoom.objects.filter(
        Q(name__icontains=query) |
        Q(stream__icontains=query) |
        Q(focus__icontains=query)
    ) if query else []
    
    context = {
        'query': query,
        'classrooms': classrooms,
    }
    
    return render(request, 'home/results.html', context)