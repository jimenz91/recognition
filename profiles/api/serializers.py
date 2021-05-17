from rest_framework import serializers
from profiles.models import User
from reconocimientos.models import Mencion
from reconocimientos.api.serializers import (
    CategoriaSerializer, ProyectoSerializer)


class UserSerializer(serializers.ModelSerializer):

    menciones = serializers.SerializerMethodField()
    proyectos = ProyectoSerializer(many=True, read_only=True)
    categorias = CategoriaSerializer(many=True, read_only=True)

    def get_menciones(self, obj):
        pk = obj.id
        menciones_usuario = Mencion.objects.filter(
            emisor=pk).order_by('-fecha_realización')[:10]
        menciones = []
        for item in menciones_usuario:
            menciones.append({
                'Receptor': str(item.receptor),
                'Categoria': str(item.categoria),
                'Puntuación': str(item.puntuacion),
                'Fecha': item.fecha_realización.strftime('%d-%m-%Y')
            })
        return menciones

    class Meta:
        model = User
        fields = ('id', 'username', 'categorias', 'proyectos',
                  'menciones', 'menciones_hechas', 'promedio_puntuaciones')
