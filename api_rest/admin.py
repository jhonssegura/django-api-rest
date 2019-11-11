# -*- coding: utf-8 -*-
from django.contrib import admin
from api_rest.models import Estudiante, Profesor, Materia

class EstudianteAdmin(admin.ModelAdmin):
	model = Estudiante
	list_display = ['CodigoEstudiante', 'PrimerNombreEstudiante', 'SegundoNombreEstudiante', 'ApellidoPaternoEstudiante', 'ApellidoMaternoEstudiante', 'Activo', 'UsuarioCreacion', 'FechaCreacion', 'UsuarioModificacion', 'FechaModificacion']

class ProfesorAdmin(admin.ModelAdmin):
    model = Profesor
    list_display = ['CodigoProfesor', 'PrimerNombreProfesor', 'SegundoNombreProfesor', 'ApellidoPaternoProfesor', 'ApellidoMaternoProfesor', 'Activo', 'UsuarioCreacion', 'FechaCreacion', 'UsuarioModificacion', 'FechaModificacion']

class MateriaAdmin(admin.ModelAdmin):
    model = Materia
    list_display = ['CodigoMateria', 'NombreMateria', 'Activo', 'UsuarioCreacion', 'FechaCreacion', 'UsuarioModificacion', 'FechaModificacion']

admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Materia, MateriaAdmin)

