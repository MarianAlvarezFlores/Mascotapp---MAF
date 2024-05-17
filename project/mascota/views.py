from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota
from .forms import MascotaForm

def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascota/lista_mascotas.html', {'mascotas': mascotas})

def detalle_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, pk=mascota_id)
    return render(request, 'mascota/detalle_mascota.html', {'mascota': mascota})

def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'mascota/crear_mascota.html', {'form': form})

def actualizar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, pk=mascota_id)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('detalle_mascota', mascota_id=mascota_id)
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'mascota/actualizar_mascota.html', {'form': form})

def eliminar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, pk=mascota_id)
    if request.method == 'POST':
        mascota.delete()
        return redirect('lista_mascotas')
    return render(request, 'mascota/confirmar_eliminacion.html', {'mascota': mascota})