from django.db import models


from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Purpose:
        Defines a profile model for handling users
        from django user model.

    Features:
        1) Has a foreign key  to django user.
    """
    user = models.ForeignKey(User, name="Usuario",unique=True)
    nomb_persona = models.CharField("Nombre",max_length=100)
    tlf_persona = models.CharField("Telefono",max_length=100)
    email_perso = models.EmailField("Email",max_length=100)

    class  Meta:

        verbose_name ='Perfil de Usuario'
        verbose_name_plural ='Perfil de Usuarios'

    def __unicode__(self):

         return u' Usuario - Nombre: %s  -Telefono: %s  -Email: %s' % (self.nomb_persona,self.tlf_persona, self.email_perso)
