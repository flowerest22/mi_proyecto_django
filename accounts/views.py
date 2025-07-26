# accounts/views.py
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Después de registrarse, redirige al login
    template_name = 'accounts/register.html'
