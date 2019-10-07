# serializers.py
from rest_framework import serializers

from .models import *

# Serializers define the API representation.
class EstablecimientoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Establecimiento
        fields = ('id', 'logotipo', 'tipo_establecimiento', 'tipo_comida', 'descripcion', 'recomendacion', 'foto_1', 'foto_2','foto_3',
            'foto_4','foto_5','foto_6', 'foto_7', 'foto_8', 'foto_9', 'foto_10', 'descuento_popeyes', 'pago_conductores', 'telefono', 
            'horario_lunes', 'horario_martes', 'horario_miercoles', 'horario_jueves', 'horario_viernes', 'horario_sabado', 'horario_domingo',
            'marcador_mapa'
        )
    
    """
    def create(self, validated_data):
        # Create and return a new `Establecimiento` instance, given the validated data.
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #Update and return an existing `Establecimiento` instance, given the validated data.
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
    """

class ConductorCuponesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.CharField(read_only=True)
    #id_usuario_genera = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Log_codigo
        fields = ('id', 'fecha_creacion', 'codigo_generado', 'id_establecimiento', 'id_usuario_genera', 'status', 
            'id_usuario_recibe', 'cantidad_cuenta'
        )
    
    """
    def create(self, validated_data):
        # Create and return a new `Establecimiento` instance, given the validated data.
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #Update and return an existing `Establecimiento` instance, given the validated data.
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
    """

class ConductorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Conductor
        fields = ('id', 'nombre', 'apellidos', 'correo_electronico', 'telefono', 'contrasena', 'id_tipo_usuario',
            'codigo_activacion','fecha_inicio','tipo_compania', 'pais', 'estado', 'ciudad', 'status'
        )