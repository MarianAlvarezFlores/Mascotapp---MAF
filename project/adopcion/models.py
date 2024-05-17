from django.db import models

from django.db import models
from django.utils import timezone
from mascota.models import Mascota
from django.contrib.auth.models import User

class Adopcion(models.Model):
    adoptante = models.ForeignKey(User, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha_adopcion = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-fecha_adopcion",)