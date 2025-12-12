from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Books

# Create your views here.
@login_required(login_url='/admin')
def books(request):
    all_books = Books.objects.all()
    return render(request, "books/index.html", {'books' : all_books})