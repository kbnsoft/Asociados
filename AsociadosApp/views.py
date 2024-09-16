from django.shortcuts import render, HttpResponse
from .models import Afiliado, Empresa, ResumenHistorico
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, "home.html")

def dashboards(request):
    h = ResumenHistorico.objects.filter(empresa__id = 1)
    return render(request, "dashboards.html", {"resumen_hitorico":h})

def nomina(request):
    afiliados = Afiliado.objects.filter(empresa__id = 1)
    return render(request, "nomina.html", {"afiliados":afiliados})

def facturacion(request):
    return render(request, "facturacion.html")

def contacto(request):
    return HttpResponse("Contacto")