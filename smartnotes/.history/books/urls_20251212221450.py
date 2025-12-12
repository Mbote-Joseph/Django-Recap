from django.urls import path
from . import views

urlpatterns = [
    path('',views.BooksListView.as_view()),
    path('/<int:pk>',views.BookDetailsView.as_view())
]
