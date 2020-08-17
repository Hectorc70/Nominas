from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy


class PersonalUsuario(BaseUserManager):
    """ 
    Administrador de modelo de usuario personalizado donde el Numero de control
    es el identificador único para la autenticación en lugar de los nombres de usuario 
    """ 

    def create_user(self, control, password, **extra_fields):
        """
        Crea y guarda un usuario con el numero de control 
        y la contraseña proporcionados.
        """
        if not control:
            raise ValueError(ugettext_lazy('No existe Numero de control'))
        control = self.normalize_email(control)
        user = self.model(control=control, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, control, password, **extra_fields):
        """
        crea y guarda un SuperUser pasandole
        numero de control y contraseña.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(ugettext_lazy('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(ugettext_lazy('Superuser must have is_superuser=True.'))
        return self.create_user(control, password, **extra_fields)