from django.urls import path
# from reconocimientos.api.views import puntuacion_list_create_api_view, puntuacion_detail_api_view
from reconocimientos.api.views import (
    PuntuacionDetailAPIView, PuntuacionListCreateAPIView, ProyectoDetailAPIView, ProyectoListCreateAPIView)

urlpatterns = [
    # path('puntuaciones/', puntuacion_list_create_api_view, name='puntuacion-list'),
    # path('puntuaciones/<int:pk>', puntuacion_detail_api_view,
    #      name='puntuacion-detail')
    path('puntuaciones/', PuntuacionListCreateAPIView.as_view(),
         name='puntuacion-list'),
    path('puntuaciones/<int:pk>', PuntuacionDetailAPIView.as_view(),
         name='puntuacion-detail'),
    path('proyectos/', ProyectoListCreateAPIView.as_view(), name='proyecto-list'),
    path('proyectos/<int:pk>', ProyectoDetailAPIView.as_view(),
         name='proyecto-detail')
]
