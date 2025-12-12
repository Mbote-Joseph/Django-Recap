from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import ListView

from .models import Books

class BooksListView(LoginRequiredMixin, ListView):
    model = Books
    context_object_name = "books"
    login_url = "/admin"
    template_name = "books/index.html"

# Create your views here.
# @login_required(login_url='/admin')
# def books(request):
#     all_books = Books.objects.all()
#     return render(request, "books/index.html", {'books' : all_books})


def book_detail(request, pk):
    try:
        book_detail = Books.objects.get(pk=pk)
    except Books.DoesNotExist:
        raise Http404("Book Doesn't Exist")
    return render(request, "books/book.html", {'book_detail' : book_detail})

