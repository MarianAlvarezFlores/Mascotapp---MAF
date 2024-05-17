from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Mascota
from .forms import MascotaForm

def home(request):
    return render(request, 'mascota/home.html')

class MascotaList(ListView): 
    model = Mascota 
    template_name = 'mascota/mascota_list.html' 
    context_object_name = 'mascotas'

class MascotaDetail(DetailView):
    model = Mascota
    context_object_name = 'mascota'
    template_name = 'mascota/detalle_mascota.html'

class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/crear_mascota.html'
    success_url = reverse_lazy('lista_mascotas')

class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/actualizar_mascota.html'

    def get_success_url(self):
        return reverse_lazy('detalle_mascota', kwargs={'mascota_id': self.get_object().pk})

class MascotaDelete(LoginRequiredMixin, DeleteView):
    model = Mascota
    template_name = 'mascota/confirmar_eliminacion.html'
    success_url = reverse_lazy('lista_mascotas')