from django.contrib.auth.models import AbstractUser
from django.db import models

class Perfil(models.Model):
    id = models.AutoField(primary_key=True, db_column='pel_id')
    descripcion = models.CharField(max_length=50, db_column='pel_descripcion')
    vigente = models.BooleanField(default=True, db_column='pel_vigente')

    class Meta:
        db_table = 'perfil'

class Aplicacion(models.Model):
    id = models.AutoField(primary_key=True, db_column='apl_id')
    descripcion = models.CharField(max_length=50, db_column='apl_descripcion')
    vigente = models.BooleanField(default=True, db_column='apl_vigente')

    class Meta:
        db_table = 'aplicacion'

class PerfilAplicacion(models.Model):
    id = models.AutoField(primary_key=True, db_column='pea_id')
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, db_column='pel_id')
    aplicacion = models.ForeignKey(Aplicacion, on_delete=models.CASCADE, db_column='apl_id')
    ingresar = models.BooleanField(db_column='pea_ingresar')
    modificar = models.BooleanField(db_column='pea_modificar')
    eliminar = models.BooleanField(db_column='pea_eliminar')
    consultar = models.BooleanField(db_column='pea_consultar')

    class Meta:
        db_table = 'perfil_aplicacion'

class Usuario(AbstractUser):
    id = models.AutoField(primary_key=True, db_column='usu_id')
    perfil = models.ForeignKey(Perfil, on_delete=models.SET_NULL, null=True, db_column='pel_id')
    ruta_foto = models.CharField(max_length=255, blank=True, null=True, db_column='usu_ruta_foto')
    vigente = models.BooleanField(default=True, db_column='usu_vigente')

    # Remove the fields that are already in AbstractUser
    # username, password, first_name, last_name, email, is_staff, is_active, date_joined
    
    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username
