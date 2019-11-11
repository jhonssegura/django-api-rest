# -*- coding: utf-8 -*-	
# Llamados al contenido dentro de la aplicación api_rest
from api_rest.models import Estudiante, Profesor, Materia
# Llamados a herramientas del rest_framework
from rest_framework import serializers
from rest_framework.schemas import SchemaGenerator
from rest_framework_swagger import renderers

class EstudianteSerializer(serializers.Serializer):
    CodigoEstudiante = serializers.CharField(max_length=20)
    PrimerNombreEstudiante = serializers.CharField(max_length=20)
    SegundoNombreEstudiante = serializers.CharField(max_length=20)
    ApellidoPaternoEstudiante = serializers.CharField(max_length=20)
    ApellidoMaternoEstudiante = serializers.CharField(max_length=20)
    Activo = serializers.BooleanField()
    UsuarioCreacion = serializers.CharField(max_length=20)
    FechaCreacion = serializers.CharField(max_length=20)
    UsuarioModificacion = serializers.CharField(max_length=20)
    FechaModificacion = serializers.CharField(max_length=20)

class ProfesorSerializer(serializers.Serializer):
    CodigoProfesor = serializers.CharField(max_length=20)
    PrimerNombreProfesor = serializers.CharField(max_length=20)
    SegundoNombreProfesor = serializers.CharField(max_length=20)
    ApellidoPaternoProfesor = serializers.CharField(max_length=20)
    ApellidoMaternoProfesor = serializers.CharField(max_length=20)
    Activo = serializers.BooleanField()
    UsuarioCreacion =serializers.CharField(max_length=20)
    FechaCreacion = serializers.CharField(max_length=20)
    UsuarioModificacion = serializers.CharField(max_length=20)
    FechaModificacion = serializers.CharField(max_length=20)

class MateriaSerializer(serializers.Serializer):
    CodigoMateria = serializers.CharField(max_length=20)
    NombreMateria = serializers.CharField(max_length=20)
    Activo = serializers.BooleanField()
    UsuarioCreacion = serializers.CharField(max_length=20)
    FechaCreacion = serializers.CharField(max_length=20)
    UsuarioModificacion = serializers.CharField(max_length=20)
    FechaModificacion = serializers.CharField(max_length=20)


