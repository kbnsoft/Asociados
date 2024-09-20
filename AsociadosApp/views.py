from django.shortcuts import render, HttpResponse
from .models import Afiliado, Empresa, ResumenHistorico
from django.core.paginator import Paginator
from django.db.models import Q

def home(request):
    return render(request, "home.html")

def dashboards(request):
    afiliados = Afiliado.objects.filter(empresa__id = 1)
    return render(request, "dashboards.html", {"afiliados_activos":afiliados.count(),
                                               "afiliados_altas":afiliados.filter(estado='Alta').count(),
                                               "afiliados_bajas":afiliados.filter(estado='Baja').count(),
                                               "afiliados_modif":afiliados.filter(estado='Modif.').count()})

def nomina(request):
    # Obtener el id de la empresa
    id_empresa = 1 # ver cómo levantar el id de la empresa a la cual pertenece el usuario logueado
    
    # Obtener la lista de afiliados
    afiliados = Afiliado.objects.filter(empresa__id = id_empresa)
    
    # Filtrar la lista de afiliados (búsquedas)
    query = request.GET.get('q')  # Obtener el parámetro 'q' de la búsqueda
    if query:
        afiliados = afiliados.filter(Q(nombre__icontains=query) | Q(apellido__icontains=query))
    
    # Configurar el paginador
    np = 20 # Definir el nro de afiliados por página
    paginator = Paginator(afiliados, np)  # Show "np" afiliados per page.
    # Obtener el número de página desde los parámetros GET
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    ru2 = page_obj.number + 2
    rd2 = page_obj.number - 2
    rd3 = page_obj.number - 3
    ru3 = page_obj.number + 3
    return render(request, "nomina.html", {"page_obj": page_obj, 
                                           "query":query, 
                                           "total_nomina": afiliados.count, 
                                           "ru2":ru2,
                                           "rd2":rd2,
                                           "rd3":rd3,
                                           "ru3":ru3})

def facturacion(request):
    return render(request, "facturacion.html")

def contacto(request):
    return HttpResponse("Contacto")