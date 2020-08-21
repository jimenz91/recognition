from django.urls import path
from reconocimientos.api.views import (CategoriaDetailAPIView, CategoriaCreateListAPIView,
                                       MencionCreateListAPIView, MencionDetailAPIView,
                                       PuntuacionDetailAPIView, PuntuacionListCreateAPIView,
                                       ProyectoDetailAPIView, ProyectoListCreateAPIView)

urlpatterns = [
    path('puntuaciones/', PuntuacionListCreateAPIView.as_view(),
         name='puntuacion-list'),
    path('puntuaciones/<int:pk>', PuntuacionDetailAPIView.as_view(),
         name='puntuacion-detail'),
    path('proyectos/', ProyectoListCreateAPIView.as_view(),
         name='proyecto-list'),
    path('proyectos/<int:pk>', ProyectoDetailAPIView.as_view(),
         name='proyecto-detail'),
    path('menciones/', MencionCreateListAPIView.as_view(),
         name='mencion-list'),
    path('menciones/<int:pk>', MencionDetailAPIView.as_view(),
         name='mencion-detail'),
    path('categorias/', CategoriaCreateListAPIView.as_view(),
         name='categoria-list'),
    path('categorias/<int:pk>', CategoriaDetailAPIView.as_view(),
         name='categoria-detail'),
]
