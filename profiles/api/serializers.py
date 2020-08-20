from rest_framework import serializers
from profiles.models import User
from reconocimientos.api.serializers import (
    CategoriaSerializer, MencionSerializer, ProyectoSerializer)


class UserSerializer(serializers.ModelSerializer):

    menciones = MencionSerializer(many=True, read_only=True)
    proyectos = ProyectoSerializer(many=True, read_only=True)
    categorias = CategoriaSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'categorias', 'proyectos',
                  'menciones', 'menciones_hechas', 'promedio_puntuaciones')
