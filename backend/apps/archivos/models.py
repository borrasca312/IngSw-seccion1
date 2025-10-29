from django.db import models
from apps.autenticacion.models import Usuario
from apps.personas.models import Persona
from apps.cursos.models import CursoSeccion
from apps.maestros.models import TipoArchivo

class Archivo(models.Model):
    id = models.AutoField(primary_key=True, db_column='arc_id')
    tipo_archivo = models.ForeignKey(TipoArchivo, on_delete=models.PROTECT, db_column='tar_id')
    usuario_crea = models.ForeignKey(Usuario, on_delete=models.PROTECT, db_column='usu_id_crea', related_name='archivos_creados')
    usuario_modifica = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, db_column='usu_id_modifica', related_name='archivos_modificados')
    fecha_hora = models.DateTimeField(auto_now_add=True, db_column='arc_fecha_hora')
    descripcion = models.CharField(max_length=100, db_column='arc_descripcion')
    ruta = models.TextField(db_column='arc_ruta')
    vigente = models.BooleanField(default=True, db_column='arc_vigente')
    class Meta: db_table = 'archivo'

class ArchivoCurso(models.Model):
    id = models.AutoField(primary_key=True, db_column='aru_id')
    archivo = models.ForeignKey(Archivo, on_delete=models.CASCADE, db_column='arc_id')
    curso_seccion = models.ForeignKey(CursoSeccion, on_delete=models.CASCADE, db_column='cus_id')
    class Meta: db_table = 'archivo_curso'

class ArchivoPersona(models.Model):
    id = models.AutoField(primary_key=True, db_column='arp_id')
    archivo = models.ForeignKey(Archivo, on_delete=models.CASCADE, db_column='arc_id')
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='per_id')
    curso_seccion = models.ForeignKey(CursoSeccion, on_delete=models.CASCADE, db_column='cus_id')
    class Meta: db_table = 'archivo_persona'
