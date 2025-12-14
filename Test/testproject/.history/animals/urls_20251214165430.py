from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnimalView.as_view(), name='animal.list'),
    path('/<int:pk>', views.AnimalDetailView.as_view()),
]
