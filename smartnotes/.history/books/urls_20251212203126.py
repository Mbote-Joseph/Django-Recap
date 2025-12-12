from django.urls import path
from . import views
from books.views import book_detail

urlpatterns = [
    path('',views.books),
    path('/<int:pk>',views.book_detail)
]
