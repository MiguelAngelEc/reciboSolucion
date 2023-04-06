from django.db import models

# Create your models here.
class cliente(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=254, unique=True)
    
    def __str__(self):
        texto = "{0}({1})"
        return texto.format(self.nombre, self.codigo)