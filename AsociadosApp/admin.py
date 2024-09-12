from django.contrib import admin

# Register your models here.
from AsociadosApp.models import Afiliado, Empresa

class AfiliadoAdmin(admin.ModelAdmin):
   list_display = ['apellido','nombre', 'cuil', 'importe', 'periodo', 'facturado']
   search_fields = ['apellido','nombre', 'cuil']
   readonly_fields = ('created','updated')

admin.site.register(Afiliado, AfiliadoAdmin)
admin.site.register(Empresa)