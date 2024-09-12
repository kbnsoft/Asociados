from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def dashboards(request):
    return render(request, "dashboards.html")

def nomina(request):
    return render(request, "nomina.html")

def facturacion(request):
    return render(request, "facturacion.html")

def contacto(request):
    return HttpResponse("Contacto")