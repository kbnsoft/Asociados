from django.urls import path
from AsociadosApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('dashboards', views.dashboards, name="Dashboards"),
    path('nomina', views.nomina, name="Nomina"),
    path('facturacion', views.facturacion, name="Facturacion"),
    path('contacto', views.contacto, name="Contacto"),
]
