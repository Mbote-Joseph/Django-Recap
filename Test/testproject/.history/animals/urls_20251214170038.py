from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnimalView.as_view(), name='animal.list'),
    path('/<int:pk>', views.AnimalDetailView.as_view()),
    path('/add', views.AnimalCreateView.as_view(), name='animal.add'),
    path('/<int:pk>/edit', views.AnimalUpdateView.as_view(), name='animal.edit'),
    path('/<int:pk>/delete', views.AnimalDeleteView.as_view(), name='animal.delete')
]
