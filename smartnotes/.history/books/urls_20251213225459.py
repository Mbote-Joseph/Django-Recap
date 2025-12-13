from django.urls import path
from . import views

urlpatterns = [
    path('',views.BooksListView.as_view(), name='books.list'),
    path('/<int:pk>',views.BookDetailsView.as_view(), name='book.details'),
    path('/bookform', views.BookCreateView.as_view(), name='book.create')
]
