from django.db import models
from Nomina.models import Empresa, Afiliado

# Create your models here.
class LiquidacionCabecera(models.Model):
    comprobante = models.CharField(max_length=2)
    letra = models.CharField(max_length=1)
    sucursal = models.CharField(max_length=1)
    numero = models.CharField(max_length=10)
    fecha = models.DateField()
    tipo_deudor = models.CharField(max_length=6)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, null=True)
    condicion = models.CharField(max_length=6) #condición de pago
    moneda = models.CharField(max_length=5)
    estado = models.CharField(max_length=1)
    gravada = models.CharField(max_length=1)
    periodo = models.CharField(max_length=10)
    vencimiento = models.DateField()
    cantidad_afiliados = models.IntegerField()
    total_liquidado = models.DecimalField(max_digits=12, decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        sc = str(self.empresa.codigo) + ' - ' + self.empresa.nombre_fantasia + ' - ' + str(self.periodo)
        return sc

class LiquidacionDetalle(models.Model):
    secuencia = models.CharField(max_length=2)
    concepto_codigo = models.CharField(max_length=5)
    concepto_descripcion = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    liquidacion = models.ForeignKey('LiquidacionCabecera', on_delete=models.CASCADE, blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        sc = str(self.liquidacion.empresa.codigo) + ' - ' + self.secuencia + ' - ' + str(self.concepto_descripcion)
        return sc

    def subtotal(self):
        st = self.cantidad * self.precio_unitario
        return st