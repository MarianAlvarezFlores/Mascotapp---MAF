from django.db import models

class Mascota(models.Model):
    ESPECIE_CHOICES = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
    ]
    TAMANO_CHOICES = [
        ('chico', 'Chico'),
        ('mediano', 'Mediano'),
        ('grande', 'Grande'),
    ]
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=5, choices=ESPECIE_CHOICES)
    tamano = models.CharField(max_length=8, choices=TAMANO_CHOICES)
    edad = models.IntegerField()
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='mascotas/', blank=True, null=True)
    fecha_agregada = models.DateField(auto_now_add=True)
    adoptada = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
