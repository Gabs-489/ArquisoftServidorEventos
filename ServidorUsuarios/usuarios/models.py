from django.db import models
from django.contrib.postgres.fields import ArrayField

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)  
    celular = models.IntegerField(default=15)
    correo = models.CharField(max_length=200)
    cedula = models.CharField(max_length=12)  
    class Meta:
        abstract = True 

class Paciente(Usuario):
    edad = models.CharField(max_length=3)
    eventos = ArrayField(models.IntegerField(), blank=True, default=list)
    class Meta:
        abstract = True  