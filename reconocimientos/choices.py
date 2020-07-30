from reconocimientos.models import Categoria, Puntuacion, Proyecto
from django.template.defaultfilters import lower, upper

"""
    Con esta lógica se obtienen los valores que hay en la base de datos para
    categorías, proyectos y puntuaciones, de forma tal que se puedan comparar
    luego cuando se generen nuevas menciones.
"""

n_categorias = Categoria.objects.all().values()
n_puntuaciones = Puntuacion.objects.all().values()
n_proyectos = Proyecto.objects.all().values()

categorias = {}
puntuaciones = {}
proyectos = {}

for c in n_categorias:
    categorias[c['nombre']] = c['id']


for p in n_puntuaciones:
    puntuacion = lower(p['denominacion'])
    puntuaciones[puntuacion] = p['id']
    puntuacion = upper(p['denominacion'])
    puntuaciones[puntuacion] = p['id']

puntuaciones[''] = 6

for p in n_proyectos:
    proyectos[p['nombre']] = p['id']
