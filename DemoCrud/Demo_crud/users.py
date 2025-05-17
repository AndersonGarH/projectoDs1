from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    
    #crear usuario de la libreria abstractbaseuser
    
    def create_user(self, email, name, name2, lastname1, lastname2, cd, password, phone, is_boss, edad, genero, ):
        if not email:
            raise ValueError('Users must have an email address')
        if not phone:
            raise ValueError('user musy have a valid phone')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
            is_boss=is_boss
            )   
 
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_rol(self, rolID, name):
        if not rolID:
            raise ValueError('todo usuario debe tener rol')



class User(AbstractBaseUser):
    # Campos personalizados y pendientes de modificar segun nuestro scheme
    is_boss = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email' # cual va a ser la PK
    REQUIRED_FIELDS = ['name', 'phone']