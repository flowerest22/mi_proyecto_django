from django.urls import path
from .views import CustomLoginView, RegisterView  # Importamos también RegisterView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),  # URL para registro
]
