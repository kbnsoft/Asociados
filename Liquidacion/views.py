from django.shortcuts import render, get_object_or_404
from .models import LiquidacionCabecera, LiquidacionDetalle
from django.core.paginator import Paginator
from Asociados.utils import IdEmpresaActiva

# Create your views here.
def liquidacion_list(request):    
    # Obtener la lista de liquidaciones
    liqs = LiquidacionCabecera.objects.filter(empresa__id = IdEmpresaActiva()).order_by("-fecha")[:12]
    
    # Configurar el paginador
    np = 20 # Definir el nro de liquidaciones por página
    paginator = Paginator(liqs, np)  # Show "np" liqs per page.
    # Obtener el número de página desde los parámetros GET
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    ru2 = page_obj.number + 2
    rd2 = page_obj.number - 2
    rd3 = page_obj.number - 3
    ru3 = page_obj.number + 3

    return render(request, "liquidacion_l.html", {"page_obj": page_obj,  
                                           "ru2":ru2,
                                           "rd2":rd2,
                                           "rd3":rd3,
                                           "ru3":ru3})

def liquidacion_read(request, liquidacion_id):
    lC = get_object_or_404(LiquidacionCabecera, id=liquidacion_id)
    lD = LiquidacionDetalle.objects.filter(liquidacion_id = liquidacion_id).order_by("secuencia")
    return render(request, 'liquidacion_r.html', {'cabecera': lC, 'detalle': lD})