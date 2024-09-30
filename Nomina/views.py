from django.shortcuts import render, redirect
from .models import Afiliado, Empresa
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import AfiliadoForm
from .utils import PeriodoCarga, IdEmpresaActiva

# Create your views here.
def nomina(request):    
    # Obtener la lista de afiliados
    afiliados = Afiliado.objects.filter(empresa__id = IdEmpresaActiva()).order_by("nombre")
    
    # Filtrar la lista de afiliados (búsquedas)
    query = request.GET.get('q')  # Obtener el parámetro 'q' de la búsqueda
    if query:
        afiliados = afiliados.filter(Q(nombre__icontains=query) | Q(apellido__icontains=query)).order_by("nombre")
    
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

    # baja de afiliado
    if request.method == "POST":
        IdAfiliado = request.POST.get('IdAfiliado')
        op = request.POST.get('Operacion')
        if op == 'Baja':
            bA = Afiliado.objects.get(id=IdAfiliado)
            bA.estado = 'Baja'
            bA.save()

    return render(request, "nomina.html", {"page_obj": page_obj, 
                                           "query":query, 
                                           "total_nomina": afiliados.count, 
                                           "ru2":ru2,
                                           "rd2":rd2,
                                           "rd3":rd3,
                                           "ru3":ru3,
                                           "periodo_carga": PeriodoCarga()})

def CreateAfiliado(request):
    if PeriodoCarga() == False:
        return redirect("Nomina")  # Redirect to the Afiliados list por que no está abierto el periodo de carga
    else:
        if request.method == "POST":
            form = AfiliadoForm(request.POST)        
            if form.is_valid():            
                # Crear el objeto pero no guardarlo aún en la base de datos
                Afiliado = form.save(commit=False)
                # Establecer un valor predeterminado para la Empresa
                Afiliado.empresa = Empresa.objects.get(id=IdEmpresaActiva())
                Afiliado.estado = "Alta"
                Afiliado.save()  # Save the Afiliado to the database
                return redirect("Nomina")  # Redirect to the Afiliados list
            else:
                # Handle the form errors
                print(form.errors)
        elif request.method == "GET":      
            form = AfiliadoForm()
        
        return render(request, 'afiliado_c.html', {'form': form})

def ReadAfiliado(request):
    return render(request, "afiliado_r.html")

def UpdateAfiliado(request):
    return render(request, "afiliado_u.html")

def DeleteAfiliado(request):
    return render(request, "afiliado_d.html")




# VER !!!
def home(request):
    return render(request, "home.html")

def dashboards(request):
    afiliados = Afiliado.objects.filter(empresa__id = 1)
    
    if date.today().day > 10:
        prox_cierre = "10/" + str(date.today().month + 1) + "/" + str(date.today().year)
    else:
        prox_cierre = "10/" + str(date.today().month) + "/" + str(date.today().year)

    return render(request, "dashboards.html", {"afiliados_activos":afiliados.filter(estado='Activo').count(),
                                               "afiliados_altas":afiliados.filter(estado='Alta').count(),
                                               "afiliados_bajas":afiliados.filter(estado='Baja').count(),
                                               "afiliados_modif":afiliados.filter(estado='Modif.').count(),
                                               "prox_cierre":prox_cierre})


def facturacion(request):
    return render(request, "facturacion.html")

def contacto(request):
    return render(request, "contacto.html")