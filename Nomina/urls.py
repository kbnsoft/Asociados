from django.urls import path
from Nomina import views

urlpatterns = [
    path('', views.nomina, name="Nomina"),
    path('afiliado-alta', views.AfiliadoAlta, name="AfiliadoAlta"),
    path('read-afiliado', views.ReadAfiliado, name="ReadAfiliado"),
    path('update-afiliado', views.UpdateAfiliado, name="UpadateAfiliado"),
    path('delete-afiliado', views.DeleteAfiliado, name="DeleteAfiliado"),
    path('home', views.home, name="Home"),
    path('dashboards', views.dashboards, name="Dashboards"),
    path('nomina', views.nomina, name="Nomina"),
    path('facturacion', views.facturacion, name="Facturacion"),
    path('contacto', views.contacto, name="Contacto"),
]
