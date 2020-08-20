from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from reconocimientos.models import Mencion, Puntuacion, Proyecto
from reconocimientos.api.serializers import (MencionSerializer,
                                             PuntuacionSerializer, ProyectoSerializer)


class PuntuacionListCreateAPIView(APIView):

    def get(self, request):
        puntuaciones = Puntuacion.objects.all()
        serializer = PuntuacionSerializer(puntuaciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PuntuacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PuntuacionDetailAPIView(APIView):

    def get_object(self, pk):
        puntuacion = get_object_or_404(Puntuacion, pk=pk)
        return puntuacion

    def get(self, request, pk):
        puntuacion = self.get_object(pk)
        serializer = PuntuacionSerializer(puntuacion)
        return Response(serializer.data)

    def put(self, request, pk):
        puntuacion = self.get_object(pk)
        serializer = PuntuacionSerializer(puntuacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        puntuacion = self.get_object(pk)
        puntuacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProyectoListCreateAPIView(APIView):

    def get(self, request):
        proyectos = Proyecto.objects.all()
        serializer = ProyectoSerializer(proyectos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProyectoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProyectoDetailAPIView(APIView):

    def get_object(self, pk):
        proyecto = get_object_or_404(Proyecto, pk=pk)
        return proyecto

    def get(self, request, pk):
        proyecto = self.get_object(pk)
        serializer = ProyectoSerializer(proyecto)
        return Response(serializer.data)

    def put(self, request, pk):
        proyecto = self.get_object(pk)
        serializer = ProyectoSerializer(proyecto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        proyecto = self.get_object(pk)
        proyecto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MencionCreateListAPIView(APIView):
    def get(self, request):
        menciones = Mencion.objects.all()
        serializer = MencionSerializer(menciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MencionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MencionDetailAPIView(APIView):

    def get_object(self, pk):
        mencion = get_object_or_404(Mencion, pk=pk)
        return mencion

    def get(self, request, pk):
        mencion = self.get_object(pk)
        serializer = MencionSerializer(mencion)
        return Response(serializer.data)

    def put(self, request, pk):
        mencion = self.get_object(pk)
        serializer = MencionSerializer(mencion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        mencion = self.get_object(pk)
        mencion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)