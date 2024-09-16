from django.contrib import admin

# Register your models here.
from AsociadosApp.models import Afiliado, Empresa
from AsociadosCfg.models import Localidad, Departamento, Provincia

class EmpresaAdmin(admin.ModelAdmin):
   list_display = ['codigo','razon_social', 'cuit']
   search_fields = ['codigo','razon_social', 'cuit']

class AfiliadoAdmin(admin.ModelAdmin):
   list_display = ['apellido','nombre', 'cuil', 'importe', 'periodo', 'facturado']
   search_fields = ['apellido','nombre', 'cuil']
   list_filter = ['empresa']
   readonly_fields = ('created','updated')

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
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Provincia, ProvinciaAdmin)