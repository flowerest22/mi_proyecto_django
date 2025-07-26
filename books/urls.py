from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('pages/', LibroListView.as_view(), name='libro-list'),
    path('pages/<int:pk>/', LibroDetailView.as_view(), name='libro-detail'),
    path('pages/create/', LibroCreateView.as_view(), name='libro-create'),
    path('pages/<int:pk>/edit/', LibroUpdateView.as_view(), name='libro-edit'),
    path('pages/<int:pk>/delete/', LibroDeleteView.as_view(), name='libro-delete'),
]