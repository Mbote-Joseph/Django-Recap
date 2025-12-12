from django.shortcuts import render
from django.contrib.auth.decorators import login_required

book = {
        "name": "Think Big",
        "Author": "Ben Carson",
        "year": 2020,
        "Genre": "Motivation"
    }
# Create your views here.
@login_required(login_url='/admin')
def books(request):
    return render(request, "books/index.html", {'books' : book})