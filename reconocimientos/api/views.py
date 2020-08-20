from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from reconocimientos.models import Puntuacion, Proyecto
from reconocimientos.api.serializers import (
    PuntuacionSerializer, ProyectoSerializer)


# @api_view(['GET', 'POST'])
# def puntuacion_list_create_api_view(request):
#     if request.method == 'GET':
#         puntuacions = Puntuacion.objects.all()
#         serializer = PuntuacionSerializer(puntuacions, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = PuntuacionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def puntuacion_detail_api_view(request, pk):
#     try:
#         puntuacion = Puntuacion.objects.get(pk=pk)
#     except Puntuacion.DoesNotExist:
#         return Response({
#             'error': {
#                 'code': 404,
#                 'message': 'Puntuacion no encontrado.'
#             }}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = PuntuacionSerializer(puntuacion)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = PuntuacionSerializer(puntuacion, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         puntuacion.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


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
