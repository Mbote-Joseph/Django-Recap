from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from books.forms import BookForm

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


class BookDetailsView(DetailView):
    model = Books
    context_object_name = "book"
    template_name = "books/book.html"

# def book_detail(request, pk):
#     try:
#         book_detail = Books.objects.get(pk=pk)
#     except Books.DoesNotExist:
#         raise Http404("Book Doesn't Exist")
#     return render(request, "books/book.html", {'book_detail' : book_detail})


class BookCreateView(CreateView):
    model = Books
    form_class = BookForm
    template_name = 'books/form.html' # Create this template in your templates folder
    success_url = '/books' # Change to your success URL name
    # Optional: Override http_method_names if you only want 'get' and 'post'
    http_method_names = ['get', 'post', 'head', 'options']
    
    
class BookUpdateView(UpdateView):
    model = Books
    form_class = BookForm
    template_name = 'books/form.html' 
    success_url = '/books'
    http_method_names = ['get', 'post', 'head', 'options']