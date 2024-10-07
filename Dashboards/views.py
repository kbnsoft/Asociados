from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, Avg, Min, Max, F
from Nomina.models import Afiliado, Empresa
from datetime import date
from Asociados.utils import IdEmpresaActiva, PeriodoCarga

def Dashboards(request):
    emp = get_object_or_404(Empresa, id = IdEmpresaActiva())
    hoy = date.today()
    emp_stats = emp.afiliado_set.annotate(
        age=(hoy.year - F('nacimiento__year'))
    ).aggregate(
        avg_age=Avg('age'),
        min_age=Min('age'),
        max_age=Max('age')
    )

    afis = Afiliado.objects.filter(empresa__id = IdEmpresaActiva())

    if PeriodoCarga():
        prox = "10/" + str(date.today().month) + "/" + str(date.today().year)
    else:
        prox = "10/" + str(date.today().month + 1) + "/" + str(date.today().year)

    return render(request, "dashboards.html", {"importe_total":(afis.aggregate(Sum('importe'))['importe__sum'] or 0), 
                                               "fecha_liquidacion":"01/" + str(date.today().month) + "/" + str(date.today().year),
                                               "afiliados_activos":afis.filter(estado='Activo').count(),
                                               "afiliados_altas":afis.filter(estado='Alta').count(),
                                               "afiliados_bajas":afis.filter(estado='Baja').count(),
                                               "afiliados_modif":afis.filter(estado='Modif.').count(),
                                               "prox_cierre":prox,
                                               "edad_avg":round(emp_stats['avg_age']),
                                               "edad_min":emp_stats['min_age'],
                                               "edad_max":emp_stats['max_age']})

