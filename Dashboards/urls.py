from django.urls import path
from Dashboards import views

urlpatterns = [
    path('', views.Dashboards, name="Dashboards"),
]
