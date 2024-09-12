from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
def validar_periodo(value):
    if (value < 1) or (value > 12):
        raise ValidationError(
            _("Por favor ingresar un número entre 1 y 12"),
            params={"value": value},
        )
    

class Afiliado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cuil = models.CharField(max_length=11)
    nro_afiliado = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    nacimiento = models.DateField()
    importe = models.FloatField(blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True, validators=[validar_periodo]) # el importe corresponde a este período facturado (nro del 1 al 12)
    facturado = models.DateField(blank=True, null=True) # fecha en que se procesó el cálculo y facturación
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


class Empresa(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=100)


