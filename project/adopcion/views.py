from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Adopcion

def lista_adopciones(request):
    adopciones = Adopcion.objects.all()
    return render(request, 'adopcion/lista_adopciones.html', {'adopciones': adopciones})