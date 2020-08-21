from datetime import datetime, timezone
from django.utils.timesince import timesince
from rest_framework import serializers
from reconocimientos.models import (Categoria, Mencion, Puntuacion, Proyecto)


class PuntuacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Puntuacion
        exclude = ('id',)

    def validate(self, data):
        if data['denominacion'] == data['descripcion']:
            raise serializers.ValidationError(
                'El titulo y la descripcion deben ser diferentes')
        return data

    def validate_valor(self, valor):
        if valor > 100 and valor < 0:
            raise serializers.ValidationError(
                'El valor de la puntuación debe estar entre 0 y 100.')
        return valor


class ProyectoSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    autor = serializers.StringRelatedField()

    class Meta:
        model = Proyecto
        exclude = ('id', 'creado', 'actualizado')

    def get_time_since_publication(self, obj):
        publication_date = obj.actualizado
        now = datetime.now(timezone.utc)
        time_delta = timesince(publication_date, now)
        return time_delta


class MencionSerializer(serializers.ModelSerializer):

    emisor = serializers.StringRelatedField()
    receptor = serializers.StringRelatedField()
    categoria = serializers.StringRelatedField()

    class Meta:
        model = Mencion
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
