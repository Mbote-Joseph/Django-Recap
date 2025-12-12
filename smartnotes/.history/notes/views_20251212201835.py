from django.shortcuts import render
from django.db import models
from django.template.context_processors import request

from .models import Notes
# Create your views here.


def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def note_details(request, pk):
    note_detail = Notes.objects.get(pk=pk)
    return render(request, 'notes/notes_list.html', {'note_detail': note_detail})