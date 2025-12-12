from django.urls import path
from . import views

urlpatterns = [
    path('',views.books),
    path('/<int:pk>',views.book_detail)
]
