from django.urls import path
from Nomina import views

urlpatterns = [
    path('afiliado-list', views.afiliado_list, name="AfiliadoList"),
    path('afiliado-create', views.afiliado_create, name="AfiliadoCreate"),
    path('afiliado-update/<int:afiliado_id>/', views.afiliado_update, name="AfiliadoUpdate"),
    path('afiliado-baja/<int:afiliado_id>/', views.afiliado_baja, name="AfiliadoBaja"),
]
