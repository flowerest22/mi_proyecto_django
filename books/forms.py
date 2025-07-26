# books/forms.py

from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'resena', 'portada', 'fecha_publicacion']
