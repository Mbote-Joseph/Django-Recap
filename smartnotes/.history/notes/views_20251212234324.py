from django.shortcuts import render
from django.db import models
from django.template.context_processors import request
from django.http import Http404
from django.apps import apps
from django.views.generic import ListView, DetailView

from .models import Notes
# Create your views here.

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'

class PopularNotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'
    queryset = Notes.objects.filter(likes__gt = 3)

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = 'notes/note_detail.html'

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

# def note_details(request, pk):
#     try:
#         note_detail = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note Doesn't exist")
#     return render(request, 'notes/note_detail.html', {'note_detail': note_detail})