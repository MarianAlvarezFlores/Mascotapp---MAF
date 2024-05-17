from django.urls import path
from . import views

app_name = 'adopcion'

urlpatterns = [
    path('', views.lista_adopciones, name='lista_adopciones'),
]