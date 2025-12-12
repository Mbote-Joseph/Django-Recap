from django.urls import path
from . import views
from books.views import BookCreateView, BookFormView

urlpatterns = [
    path('',views.BooksListView.as_view()),
    path('/<int:pk>',views.BookDetailsView.as_view()),
    path('/bookform', views.BookCreateView.as_view())
]
