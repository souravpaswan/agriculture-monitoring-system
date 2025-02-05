"""
URL configuration for SAMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from sensor_data import views

urlpatterns = [
    path('', views.display_data,name='display_data'),
    path('start/', views.start_data, name='start_data'),
    path('stop/', views.stop_data, name='stop_data'),
    path('api/sensor-data/', views.sensor_data, name='sensor-data'),
]
