from django.db import models

# Create your models here.

class Sugerencia(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    descripcion = models.TextField(null=True)
    
    def __str__(self):
        return f"Sugerencia: {self.nombre} - Edad: {self.edad}"