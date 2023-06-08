from unittest.util import _MAX_LENGTH
from django.db import models

class Evento(models.Model):
    nombreEvento = models.CharField(max_length=30)
    descripcionEvento = models.TextField(max_length=150)
    fechaInicioEvento = models.DateField()
    fechaFinEvento = models.DateField()
    horaInicioEvento = models.TimeField()
    horaFinEvento = models.TimeField()
    lugarEvento = models.TextField()
    fotoPromoEvento = models.TextField()
    capacidadGeneral = models.IntegerField()
    capacidadVip = models.IntegerField()
    capacidadSuperVip = models.IntegerField()
    
    

    def __str__(self):
        return self.nombreEvento

class boleta(models.Model):
    codigoBoleta = models.CharField(max_length=50)
    tipoBoleta = models.CharField(max_length=15)
    precioBoleta = models.DecimalField(max_digits=5, decimal_places=2)
    beneficiosBoleta = models.TextField()
    estadoBoleta = models.CharField(max_length=15)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.codigoBoleta



# Create your models here.
