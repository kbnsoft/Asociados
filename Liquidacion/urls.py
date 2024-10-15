from django.urls import path
from Liquidacion import views

urlpatterns = [
    path('liquidacion-list', views.liquidacion_list, name="LiquidacionList"),
    path('liquidacion-read/<int:liquidacion_id>/', views.liquidacion_read, name="LiquidacionRead"),
]
