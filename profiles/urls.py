from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginv, name='loginv'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logoutv, name='logoutv'),
]
