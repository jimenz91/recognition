from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    menciones_hechas = models.IntegerField(default=4, editable=False)
    promedio_puntuaciones = models.IntegerField(
        editable=False,
        default=0,
        blank=True,
        null=True
    )
    categorias = models.ManyToManyField('reconocimientos.Categoria',
                                        blank=True)
    menciones = models.ManyToManyField('reconocimientos.Mencion',
                                       blank=True, editable=False)
    proyectos = models.ManyToManyField('reconocimientos.Proyecto', blank=True)
    es_mvp_mes = models.BooleanField(default=False)

    def __str__(self):
        return (self.first_name+" "+self.last_name)
