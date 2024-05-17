from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_mascotas, name='lista_mascotas'),
    path('<int:mascota_id>/', views.detalle_mascota, name='detalle_mascota'),
  
]