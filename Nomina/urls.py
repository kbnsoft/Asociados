from django.urls import path
from Nomina import views

urlpatterns = [
    path('', views.nomina, name="Nomina"),
    path('afiliado-alta', views.AfiliadoAlta, name="AfiliadoAlta"),
    path('afiliado-modif/<int:afiliado_id>/', views.AfiliadoModif, name="AfiliadoModif"),
    path('afiliado-baja/<int:afiliado_id>/', views.AfiliadoBaja, name="AfiliadoBaja"),
    path('read-afiliado', views.ReadAfiliado, name="ReadAfiliado"),
    path('delete-afiliado', views.DeleteAfiliado, name="DeleteAfiliado"),
    path('home', views.home, name="Home"),
    path('facturacion', views.facturacion, name="Facturacion"),
    path('contacto', views.contacto, name="Contacto"),
]
