from django.shortcuts import render
from rest_framework import serializers, viewsets, permissions, status, generics
from rest_framework.response import Response

# Create your views here.
from django.http import HttpResponse
from restaurants.models import *

from .permissions import IsOwnerOrReadOnly
from .serializers import *

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
    
    