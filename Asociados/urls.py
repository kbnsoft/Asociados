"""
URL configuration for Asociados project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView  # Nico 14/11/2024

urlpatterns = [
    path('', include('public.urls')),  
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),  # Nico 15/11/2024 app personalizada para agragar sign up que no viene en las librerias estándares
    path("accounts/", include("django.contrib.auth.urls")), # Nico 14/11/2024
    path('Nomina/', include('Nomina.urls')),
    path('Liquidacion/', include('Liquidacion.urls')),
    path('Dashboards/', include('Dashboards.urls')),
]
