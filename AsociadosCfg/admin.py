from django.contrib import admin

# Register your models here.
from Nomina.models import Afiliado, Empresa
from Liquidacion.models import LiquidacionCabecera, LiquidacionDetalle
from AsociadosCfg.models import Localidad, Departamento, Provincia

class EmpresaAdmin(admin.ModelAdmin):
   list_display = ['codigo','razon_social', 'cuit']
   search_fields = ['codigo','razon_social', 'cuit']

class AfiliadoAdmin(admin.ModelAdmin):
   list_display = ['nombre', 'apellido', 'cuil']
   search_fields = ['nombre', 'apellido', 'cuil']
   list_filter = ['empresa']
   readonly_fields = ('created','updated')

class LiquidacionCabeceraAdmin(admin.ModelAdmin):
   list_display = ['periodo','empresa','numero','fecha','vencimiento']

class LiquidacionDetalleAdmin(admin.ModelAdmin):
   list_display = ['liquidacion','secuencia', 'concepto_descripcion', 'cantidad', 'precio_unitario']

class LocalidadAdmin(admin.ModelAdmin):
   list_display = ['descripcion']
   search_fields = ['descripcion']
   list_filter = ['provincia', 'departamento']

class DepartamentoAdmin(admin.ModelAdmin):
   list_display = ['descripcion']
   search_fields = ['descripcion']
   list_filter = ['provincia']

class ProvinciaAdmin(admin.ModelAdmin):
   list_display = ['descripcion']
   search_fields = ['descripcion']

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Afiliado, AfiliadoAdmin)
admin.site.register(LiquidacionCabecera, LiquidacionCabeceraAdmin)
admin.site.register(LiquidacionDetalle, LiquidacionDetalleAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Provincia, ProvinciaAdmin)