from django import forms
from .models import Mascota
from . import models

class MascotaCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.MascotaCategoria
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }

class MascotaForm(forms.ModelForm):
    class Meta:
        model = models.Mascota
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "especie": forms.Select(attrs={"class": "form-control"}),
            "tamano": forms.Select(attrs={"class": "form-control"}),
            "edad": forms.NumberInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
        }