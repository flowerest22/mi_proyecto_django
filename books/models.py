from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    resena = CKEditor5Field('Reseña', config_name='default')  # ✅ Campo con CKEditor
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)
    fecha_publicacion = models.DateField()
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
