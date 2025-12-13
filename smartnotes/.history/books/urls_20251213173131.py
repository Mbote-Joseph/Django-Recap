from django.urls import path
from . import views

urlpatterns = [
    path('',views.BooksListView.as_view(), name='books_list'),
    path('/<int:pk>',views.BookDetailsView.as_view(), name='book_details'),
    path('/bookform', views.BookCreateView.as_view())
]
