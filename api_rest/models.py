from django.db import models

class Estudiante(models.Model):
    CodigoEstudiante = models.CharField(max_length=20)
    PrimerNombreEstudiante = models.CharField(max_length=100)
    SegundoNombreEstudiante = models.CharField(max_length=100)
    ApellidoPaternoEstudiante = models.CharField(max_length=100)
    ApellidoMaternoEstudiante = models.CharField(max_length=100)
    Activo = models.BooleanField()
    UsuarioCreacion = models.CharField(db_column='UsuarioCreacion', max_length=100)  
    FechaCreacion = models.DateTimeField(db_column='FechaCreacion', auto_now_add=True) 
    UsuarioModificacion = models.CharField(db_column='UsuarioModificacion', max_length=100, blank=True, null=True) 
    FechaModificacion = models.DateTimeField(db_column='FechaModificacion', auto_now=True) 

    class Meta:
        db_table = 'Estudiante'

class Profesor(models.Model):
    CodigoProfesor = models.CharField(max_length=20)
    PrimerNombreProfesor = models.CharField(max_length=100)
    SegundoNombreProfesor = models.CharField(max_length=100)
    ApellidoPaternoProfesor = models.CharField(max_length=100)
    ApellidoMaternoProfesor = models.CharField(max_length=100)
    Activo = models.BooleanField()
    UsuarioCreacion = models.CharField(max_length=100)  
    FechaCreacion = models.DateTimeField(auto_now_add=True) 
    UsuarioModificacion = models.CharField(max_length=100, blank=True, null=True) 
    FechaModificacion = models.DateTimeField(auto_now=True) 
    
    class Meta:
        db_table = 'Profesor'

class Materia(models.Model):
    CodigoMateria = models.CharField(max_length=20)
    NombreMateria = models.CharField(max_length=100)
    Activo = models.BooleanField()
    UsuarioCreacion = models.CharField(db_column='UsuarioCreacion', max_length=100)  
    FechaCreacion = models.DateTimeField(db_column='FechaCreacion', auto_now_add=True) 
    UsuarioModificacion = models.CharField(db_column='UsuarioModificacion', max_length=100, blank=True, null=True) 
    FechaModificacion = models.DateTimeField(db_column='FechaModificacion', auto_now=True) 

    class Meta:
        db_table = 'Materia'


