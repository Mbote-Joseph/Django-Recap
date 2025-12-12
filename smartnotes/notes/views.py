from django.shortcuts import render
from django.db import models
from django.template.context_processors import request
from django.http import Http404

from .models import Notes
# Create your views here.


def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def note_details(request, pk):
    try:
        note_detail = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note Doesn't exist")
    return render(request, 'notes/note_detail.html', {'note_detail': note_detail})