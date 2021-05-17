from django.db import models
from datetime import datetime
from django.conf import settings


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    puntuacion = models.ManyToManyField('Puntuacion', blank=True, default=4)
    descripcion = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre


class Puntuacion(models.Model):
    denominacion = models.CharField(max_length=255)
    valor = models.IntegerField()
    descripcion = models.TextField(max_length=300, blank=True)

    class Meta:
        verbose_name_plural = "Puntuaciones"

    def __str__(self):
        return self.denominacion


class Mencion(models.Model):
    emisor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='emisor'
    )
    receptor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='receptor'
    )
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    puntuacion = models.ForeignKey(Puntuacion, on_delete=models.CASCADE)
    fecha_realización = models.DateTimeField(
        default=datetime.now,
        editable=False
    )

    class Meta:
        verbose_name_plural = "Menciones"


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000, blank=True)
    codigo = models.CharField(max_length=20)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)
    dificultad = models.IntegerField()
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='autor_proyecto'
    )

    def __str__(self):
        return self.nombre
