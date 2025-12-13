from django.urls import path
from . import views

urlpatterns = [
    path('',views.BooksListView.as_view(), name='books.list'),
    path('/<int:pk>',views.BookDetailsView.as_view(), name='book.details'),
    path('/bookform', views.BookCreateView.as_view(), name='book.create'),
    path('/<int:pk>/edit', views.BookUpdateView.as_view(), name='book.edit'),
    path('/<int:pk>/delete', views.BookDeleteView.as_view(), name='book.delete')
]
