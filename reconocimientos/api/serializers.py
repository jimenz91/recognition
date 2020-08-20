from datetime import datetime, timezone
from django.utils.timesince import timesince
from rest_framework import serializers
from reconocimientos.models import Puntuacion, Proyecto


class PuntuacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Puntuacion
        # fields = ('__all__')
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
        exclude = ('id',)

    def get_time_since_publication(self, obj):
        publication_date = obj.actualizado
        now = datetime.now(timezone.utc)
        time_delta = timesince(publication_date, now)
        return time_delta


# class PuntuacionSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     denominacion = serializers.CharField()
#     descripcion = serializers.CharField()
#     valor = serializers.IntegerField()

#     def create(self, validated_data):
#         return Puntuacion.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.denominacion = validated_data.get(
#             'denominacion', instance.denominacion)
#         instance.descripcion = validated_data.get(
#             'descripcion', instance.descripcion)
#         instance.valor = validated_data.get(
#             'valor', instance.valor)
#         return instance

#     def validate(self, data):
#         if data['denominacion'] == data['descripcion']:
#             raise serializers.ValidationError(
#                 'El titulo y la descripcion deben ser diferentes')
#         return data

#     def validate_valor(self, valor):
#         if valor > 100 and valor < 0:
#             raise serializers.ValidationError(
#                 'El valor de la puntuación debe estar entre 0 y 100.')
#         return valor