from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from .managers import PersonalUsuario

class Usuario(AbstractUser):
    username = None
    control = models.CharField(max_length=8, unique=True, primary_key=True)
    second_last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'control'
    REQUIRED_FIELDS = []

    objects = PersonalUsuario()
    
    def __str__(self):
        return "Control: %s Nombre: %s %s"%(self.control, 
                        self.first_name,
                        self.last_name
                        )

