from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/<int:pk>', views.perfil, name='perfil'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('empleados/', views.empleados, name='empleados'),
]
