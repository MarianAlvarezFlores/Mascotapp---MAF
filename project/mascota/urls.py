from django.urls import path
from . import views

app_name = 'mascota'

urlpatterns = [
    path('', views.lista_mascotas, name='lista_mascotas'),
    path('<int:mascota_id>/', views.detalle_mascota, name='detalle_mascota'),
  
]