from django.shortcuts import render
from django.db import models

from .models import Notes
# Create your views here.


def list(request):
    all_notes = Notes.object.all()