# -*- coding: utf-8 -*- 
# Llamados a herramientas REST Framework
from rest_framework import status
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Llamados a herramientas Django
import django_filters.rest_framework
from django.contrib.auth.models import User
from django.shortcuts import render
# Llamados a la aplicación api_rest
from api_rest.serializers import EstudianteSerializer, ProfesorSerializer, MateriaSerializer
from api_rest.models import Estudiante, Profesor, Materia

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer