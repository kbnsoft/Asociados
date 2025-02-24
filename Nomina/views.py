from django.shortcuts import render, redirect, get_object_or_404
from .models import Afiliado, Empresa
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import AfiliadoForm
from Asociados.utils import IdEmpresaActiva, PeriodoCarga

# Create your views here.
def afiliado_list(request):    
    # Obtener la lista de afiliados
    afiliados = Afiliado.objects.filter(empresa__id = IdEmpresaActiva()).order_by("apellido", "nombre")
    
    # Filtrar la lista de afiliados (búsquedas)
    q = request.GET.get('q')  # Obtener el parámetro 'q' de la búsqueda
    if q:
        afiliados = afiliados.filter(Q(nombre__icontains=q) | Q(apellido__icontains=q)).order_by("apellido","nombre")

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

    return render(request, "nomina/afiliado_l.html", {"page_obj": page_obj, 
                                           "query":q, 
                                           "total_nomina": afiliados.count, 
                                           "ru2":ru2,
                                           "rd2":rd2,
                                           "rd3":rd3,
                                           "ru3":ru3,
                                           "periodo_carga": PeriodoCarga()})

def afiliado_create(request):
    if PeriodoCarga() == False:
        return redirect("AfiliadoList")  # Redirect to the Afiliados list por que no está abierto el periodo de carga
    else:
        if request.method == "POST":
            form = AfiliadoForm(request.POST)        
            if form.is_valid():            
                # Crear el objeto pero no guardarlo aún en la base de datos
                afi = form.save(commit=False)
                # Establecer un valor predeterminado para la Empresa
                afi.empresa = Empresa.objects.get(id=IdEmpresaActiva())
                afi.estado = "Alta"
                afi.save()  # Save the Afiliado to the database
                return redirect("AfiliadoList") 
            else:
                # Handle the form errors
                print(form.errors)
        elif request.method == "GET":      
            form = AfiliadoForm()
        
        return render(request, 'nomina/afiliado_c.html', {'form': form})

def afiliado_update(request, afiliado_id):
    afi = get_object_or_404(Afiliado, id=afiliado_id)
    if request.method == 'POST':
        form = AfiliadoForm(request.POST, instance=afi)
        if form.is_valid():
            afi = form.save(commit=False)
            if afi.estado != "Alta":
                #si es un afiliado que se da de alta, el estado queda en "Alta"
                afi.estado = "Modif." 
            afi.save()
            return redirect("AfiliadoList")
    else:
        form = AfiliadoForm(instance=afi)
        if PeriodoCarga() == False:
            for field in form.fields.values():
                field.widget.attrs['disabled'] = 'disabled'
        
    return render(request, 'nomina/afiliado_u.html', {'form': form, 'PeriodoCarga':PeriodoCarga()})


def afiliado_read(request, afiliado_id):
    afi = get_object_or_404(Afiliado, id=afiliado_id)
    form = AfiliadoForm(instance=afi)
    return render(request, 'nomina/afiliado_r.html', {'form': form})

def afiliado_baja(request, afiliado_id):
    if PeriodoCarga() == False:
        return redirect("AfiliadoList")  # Redirect to the Afiliados list por que no está abierto el periodo de carga
    else:
        afi = get_object_or_404(Afiliado, id=afiliado_id)
        afi.estado = "Baja" 
        afi.save()
        return redirect("AfiliadoList")