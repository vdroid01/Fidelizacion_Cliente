from django.db import models

# Create your models here.
class Empresa(models.Model):
    RRF = models.CharField(max_length=13)
    Nombre = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=10)
    Correo = models.CharField(max_length=50)
    Web = models.CharField(max_length=50)
    Descuento = models.DecimalField(max_digits=10, decimal_places=2)

    # Es el que muestra en nombre de objeto
    def __str__(self):
        return self.Nombre