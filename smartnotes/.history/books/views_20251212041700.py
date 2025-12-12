from django.shortcuts import render

books = [
    {
        "name": "Think Big",
        "Author": "Ben Carson",
        "year": 2020,
        "Genre": "Motivation"
    },
    {
        "name": "Blessed Hands",
        "Author": "Ben Carson",
        "year": 2021,
        "Genre": "Guide"
    }
]
# Create your views here.
def books(request):
    return render('', "books/index.html", {})