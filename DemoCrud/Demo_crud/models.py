from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import MinValueValidator, MaxValueValidator


#Sobrescritura del usuario de Django:
class Usuario(AbstractUser):
    permission = models.CharField(max_length = 150, blank = True)
    identificacion = models.CharField(max_length = 20, blank = False)
    nombre = models.CharField(max_length = 15, blank = False)
    nombre2 = models.CharField(max_length = 15, blank = True)
    apellido = models.CharField(max_length = 15, blank = False)
    apellido2 = models.CharField(max_length = 15, blank = True)
    telefono = models.IntegerField(max_length = 10, blank = False)
    correo = models.EmailField(blank=False)
    ciudad = models.CharField(max_length=50, blank=False)
    departamento = models.CharField(max_length=50, blank=False)
    genero = models.CharField(max_length=20, blank=False)
    direccion = models.CharField(max_length=50, blank=False)


    #personalizacion
    password = None

    class Meta:
        db_table = "Usario"

class Rol(models.Model):
    IDRol = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=50, blank=False, unique=True)
    
    def __str__(self):
        return f"{str(self.id)} {self.titulo}"

    class Meta:
        db_table = "Rol"

class UsiarioRol(models.Model):
    id = models.OneToOneField(Usuario, primary_key=True,on_delete=models.CASCADE)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{str(self.id)} {str(self.id_rol)}"
    
    class Meta:
        db_table = "UsuarioRol"


class Vacante(models.Model):
    Nivel_selector = [
        ('tecnico', 'Técnico'),
        ('pregrado', 'Pregrado'),
        ('posgrado', 'Posgrado'),
        ('doctorado', 'Doctorado'),
        ('magister', 'Magíster'),
    ]
    
    cargo_selector = [
        ('analista ui/ux', 'Analista UI/UX'),
        ('desarrollador ui/ux', 'Desarrollador UI/UX'),
        ('analista back end', 'Analista Back-End'),
        ('analista comercial', 'Analista Comercial'),
        ('arquitecto y dueño de producto', 'Arquitecto y dueño de producto'),
        ('director de proyectos agiles', 'Director de Proyectos Ágiles'),
        ('lider de equipo y tecnologia', 'Lider de Equipo y Tecnología'),
        ('ingeniero de calidad', 'Ingeniero de Calidad'),
        
    ]

    rango_selector = [
        ('junior', 'Junior'),
        ('semi senior', 'Semi Senior'),
        ('Senior', 'Senior'),
    ]
    
    
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=100, blank=False, unique=True)
    cargo = models.CharField(max_length=50, choices=cargo_selector)
    rango = models.CharField(max_length=15, choices=rango_selector)
    nivel = models.CharField(max_length=10, choices=Nivel_selector)
    fechaInicio = models.DateField() #pendiente de personalizar en forms.py
    FechaFin = models.DateField() #pendiente de personalizar en forms.py

class VacanteUsuario(models.Model):
    id = models.OneToOneField(Vacante, primary_key=True on_delete=models.CASCADE)
    