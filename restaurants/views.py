from django.shortcuts import render
from rest_framework import serializers, viewsets, permissions, status, generics

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.decorators import api_view, permission_classes, renderer_classes

# Create your views here.
from django.http import HttpResponse

from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny
from .serializers import *
from restaurants.models import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Authentication ModelViewSet
class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def get_queryset(self):
        qs = self.queryset.filter(owner=self.request.user)
        return qs
        
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

# ViewSets define the view behavior.
class EstablecimientoViewSet(viewsets.ModelViewSet):
    queryset = Establecimiento.objects.all()
    serializer_class = EstablecimientoSerializer

class ConductorCuponesViewSet(viewsets.ModelViewSet):
    serializer_class = ConductorCuponesSerializer
    queryset = Log_codigo.objects.all()

class UserProductsList(generics.ListCreateAPIView):
    serializer_class = ConductorCuponesSerializer
    def get_queryset(self):
        if self.kwargs['user_id']:
            return Log_codigo.objects.filter(id_usuario_genera=self.kwargs['user_id']).order_by('id')
        else:
            return Log_codigo.objects.all().order_by('id')

class UserProductsList2(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        user_count = Log_codigo.objects.filter(id_usuario_genera=self.kwargs['user_id']).order_by('id')
        content = {'user_count': user_count}
        return Response(content)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly])
@renderer_classes([JSONRenderer])
def establecimiento_list(request):
    """
    List all code
    """
    if request.method == 'GET':
        data = Establecimiento.objects.all()
        serializer = EstablecimientoSerializer(data, many=True)
        return Response(serializer.data)


@api_view(['POST'])
#@permission_classes([permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly])
@permission_classes([AllowAny])
@renderer_classes([JSONRenderer])
def conductor_create(request):
    """
    List all code
    """
    if request.method == 'POST':
        request.data["codigo_activacion"] = "1561"
        request.data["status"] = "activo"
        print(request.data)
        serializer = ConductorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    