from django.shortcuts import render
from django.contrib.auth.decorators import login_required

book = {
        "name": "Think Big",
        "Author": "Ben Carson",
        "year": 2020,
        "Genre": "Motivation"
    }
# Create your views here.
@login_required
def books(request):
    return render(request, "books/index.html", {'books' : book})