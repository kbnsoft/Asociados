from django.urls import path
from Dashboards import views

urlpatterns = [
    path('dashboards', views.dashboards, name="Dashboards"),
]
