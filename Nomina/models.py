from django.db import models
from datetime import date
from django.db import connection

class Afiliado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cuil = models.CharField(max_length=11)
    dni = models.CharField(max_length=8)
    sexo = models.CharField(max_length=1)
    nro_afiliado = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    nacimiento = models.DateField()
    calle = models.CharField(max_length=50, blank=True, null=True)
    nro = models.CharField(max_length=10, blank=True, null=True)
    piso = models.CharField(max_length=10, blank=True, null=True)
    localidad = models.ForeignKey('AsociadosCfg.Localidad', on_delete=models.CASCADE, blank=True, null=True)
    estado = models.CharField(max_length=10)
    importe = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True) # el importe corresponde a este período facturado (nro del 1 al 12)
    facturado = models.DateField(blank=True, null=True) # fecha en que se procesó el cálculo y facturación
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def edad(self):
        hoy = date.today()
        e = hoy.year - self.nacimiento.year - ((hoy.month, hoy.day) < (self.nacimiento.month, self.nacimiento.day))
        return e

class Empresa(models.Model):
    codigo = models.IntegerField()
    razon_social = models.CharField(max_length=50)
    nombre_fantasia = models.CharField(max_length=50)
    rubro = models.CharField(max_length=50)
    cuit = models.CharField(max_length=11)
    tratamiento = models.CharField(max_length=50)

    def __str__(self):
        sc = str(self.codigo) + ' - ' + self.nombre_fantasia
        return sc