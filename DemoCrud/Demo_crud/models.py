from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import MinValueValidator, MaxValueValidator




#Sobrescritura del usuario de Django:

# tabla usuario

# campo: descripcion, estandar(ley o aplicable), tipo de dato, longitud, vacia?, restricciones 
# identificacion: campo de identificacion, numero entero segun CO, integer, longitud 20, no vacia, unico
# nombre:nombre usuario,ninguno, varchar, longitud 15, no vacia, (no palabras prohibidas,longitud 2)
# nombre2:segundo nombre del usuario,ninguno, varchar, longitud 15, opcional, (no palabras prohibidas,longitud 2)
# apellido: apellido del usuario, ninguno, varchar, longitud 15, no vacia, (no palabras prohibidas,longitud 2)
# apellido2: segundo apellido del usuario, ninguno, varchar, longitud 15, opcional, (no palabras prohibidas,longitud 2)
# edad: edad del usuario, (mayor a 18, cedula), varchar, longitud =2, no vacia, menor a 100
# telefono: telefono de contacto, numero valido de CO, integer, longitud = 10, no vacia, ninguna
# correo: correo del usuario, depende del proveedor de email, varchar, lM 3 menor = a 30, no vacia, no palabras prohibidas
# ciudad: ciudad de residencia, ciudad valida CO, varchar, l 50, no vacia, (no palabras prohibidas, acorde a DEPARTAMENTO)
# departamento: departamento de residencia, departamento valido CO, varchar, l 50, no vacia, (no palabras prohibidas, acorde a CO)
# genero: preferencia de genero,ninguno, varchar, l 20, no vacia, no palabras prohibidas
# direccion: direccion donde reside, ninguno, varchar, l 50, no vacia, no palabras prohibidas

# is_staff: 
   # is_active = None
    # last_login: registro de ultimo login, 
class Usuario(AbstractUser):
    permission = models.CharField(max_length = 150, blank = True)
    identificacion = models.IntegerField(max_length = 20, blank = False)
    nombre = models.CharField(max_length = 15, blank = False)
    nombre2 = models.CharField(max_length = 15, blank = True)
    apellido = models.CharField(max_length = 15, blank = False)
    apellido2 = models.CharField(max_length = 15, blank = True)
    edad = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)], blank=False)
    telefono = models.IntegerField(max_length = 10, blank = False)
    correo = models.EmailField(blank=False, unique=True)
    ciudad = models.CharField(max_length=50, blank=False)
    departamento = models.CharField(max_length=50, blank=False)
    genero = models.CharField(max_length=20, blank=False)
    direccion = models.CharField(max_length=50, blank=False)


    #personalizacion
    password = None

    class Meta:
        db_table = "Usario"


# tabla rol
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
    total = models.IntegerField(max_length=3, blank=False)
    fechaInicio = models.DateField() #pendiente de personalizar en forms.py
    FechaFin = models.DateField() #pendiente de personalizar en forms.py

class VacanteUsuario(models.Model):
    id = models.OneToOneField(Vacante, primary_key=True on_delete=models.CASCADE)
    id_usuario = models.OneToOneField(Usuario, primary_key=True on_delete=models.CASCADE)
    UNIQUE(id, id_usuario)
    
