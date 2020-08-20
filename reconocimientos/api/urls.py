from django.urls import path
from reconocimientos.api.views import (
    PuntuacionDetailAPIView, PuntuacionListCreateAPIView, ProyectoDetailAPIView, ProyectoListCreateAPIView)

urlpatterns = [
    path('puntuaciones/', PuntuacionListCreateAPIView.as_view(),
         name='puntuacion-list'),
    path('puntuaciones/<int:pk>', PuntuacionDetailAPIView.as_view(),
         name='puntuacion-detail'),
    path('proyectos/', ProyectoListCreateAPIView.as_view(), name='proyecto-list'),
    path('proyectos/<int:pk>', ProyectoDetailAPIView.as_view(),
         name='proyecto-detail')
]
