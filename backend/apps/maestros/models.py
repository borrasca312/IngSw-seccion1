from django.db import models

class Region(models.Model):
    id = models.AutoField(primary_key=True, db_column='reg_id')
    descripcion = models.CharField(max_length=100, db_column='reg_descripcion')
    vigente = models.BooleanField(default=True, db_column='reg_vigente')
    class Meta: db_table = 'region'

class Provincia(models.Model):
    id = models.AutoField(primary_key=True, db_column='pro_id')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, db_column='reg_id', related_name='provincias')
    descripcion = models.CharField(max_length=100, db_column='pro_descripcion')
    vigente = models.BooleanField(default=True, db_column='pro_vigente')
    class Meta: db_table = 'provincia'

class Comuna(models.Model):
    id = models.AutoField(primary_key=True, db_column='com_id')
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, db_column='pro_id', related_name='comunas')
    descripcion = models.CharField(max_length=100, db_column='com_descripcion')
    vigente = models.BooleanField(default=True, db_column='com_vigente')
    class Meta: db_table = 'comuna'

class Zona(models.Model):
    id = models.AutoField(primary_key=True, db_column='zon_id')
    descripcion = models.CharField(max_length=100, db_column='zon_descripcion')
    unilateral = models.BooleanField(db_column='zon_unilateral')
    vigente = models.BooleanField(default=True, db_column='zon_vigente')
    class Meta: db_table = 'zona'

class Distrito(models.Model):
    id = models.AutoField(primary_key=True, db_column='dis_id')
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, db_column='zon_id', related_name='distritos')
    descripcion = models.CharField(max_length=100, db_column='dis_descripcion')
    vigente = models.BooleanField(default=True, db_column='dis_vigente')
    class Meta: db_table = 'distrito'

class Grupo(models.Model):
    id = models.AutoField(primary_key=True, db_column='gru_id')
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE, db_column='dis_id', related_name='grupos')
    descripcion = models.CharField(max_length=100, db_column='gru_descripcion')
    vigente = models.BooleanField(default=True, db_column='gru_vigente')
    class Meta: db_table = 'grupo'

class Rama(models.Model):
    id = models.AutoField(primary_key=True, db_column='ram_id')
    descripcion = models.CharField(max_length=50, db_column='ram_descripcion')
    vigente = models.BooleanField(default=True, db_column='ram_vigente')
    class Meta: db_table = 'rama'

class Nivel(models.Model):
    id = models.AutoField(primary_key=True, db_column='niv_id')
    descripcion = models.CharField(max_length=50, db_column='niv_descripcion')
    orden = models.IntegerField(db_column='niv_orden')
    vigente = models.BooleanField(default=True, db_column='niv_vigente')
    class Meta: db_table = 'nivel'

class EstadoCivil(models.Model):
    id = models.AutoField(primary_key=True, db_column='esc_id')
    descripcion = models.CharField(max_length=50, db_column='esc_descripcion')
    vigente = models.BooleanField(default=True, db_column='esc_vigente')
    class Meta: db_table = 'estado_civil'

class Cargo(models.Model):
    id = models.AutoField(primary_key=True, db_column='car_id')
    descripcion = models.CharField(max_length=100, db_column='car_descripcion')
    vigente = models.BooleanField(default=True, db_column='car_vigente')
    class Meta: db_table = 'cargo'

class TipoArchivo(models.Model):
    id = models.AutoField(primary_key=True, db_column='tar_id')
    descripcion = models.CharField(max_length=50, db_column='tar_descripcion')
    vigente = models.BooleanField(default=True, db_column='tar_vigente')
    class Meta: db_table = 'tipo_archivo'

class TipoCurso(models.Model):
    id = models.AutoField(primary_key=True, db_column='tcu_id')
    descripcion = models.CharField(max_length=100, db_column='tcu_descripcion')
    tipo = models.IntegerField(db_column='tcu_tipo')
    cantidad_participante = models.IntegerField(null=True, blank=True, db_column='tcu_cant_participante')
    vigente = models.BooleanField(default=True, db_column='tcu_vigente')
    class Meta: db_table = 'tipo_curso'

class Alimentacion(models.Model):
    id = models.AutoField(primary_key=True, db_column='ali_id')
    descripcion = models.CharField(max_length=100, db_column='ali_descripcion')
    tipo = models.IntegerField(db_column='ali_tipo')
    vigente = models.BooleanField(default=True, db_column='ali_vigente')
    class Meta: db_table = 'alimentacion'

class Rol(models.Model):
    id = models.AutoField(primary_key=True, db_column='rol_id')
    descripcion = models.CharField(max_length=50, db_column='rol_descripcion')
    tipo = models.IntegerField(db_column='rol_tipo')
    vigente = models.BooleanField(default=True, db_column='rol_vigente')
    class Meta: db_table = 'rol'

class ConceptoContable(models.Model):
    id = models.AutoField(primary_key=True, db_column='coc_id')
    descripcion = models.CharField(max_length=50, db_column='coc_descripcion')
    vigente = models.BooleanField(default=True, db_column='coc_vigente')
    class Meta: db_table = 'concepto_contable'

class TipoRendicion(models.Model):
    id = models.AutoField(primary_key=True, db_column='tre_id')
    descripcion = models.CharField(max_length=50, db_column='tre_descripcion')
    vigente = models.BooleanField(default=True, db_column='tre_vigente')
    class Meta: db_table = 'tipo_rendicion'

class TipoDoctoRendicion(models.Model):
    id = models.AutoField(primary_key=True, db_column='tdr_id')
    descripcion = models.CharField(max_length=50, db_column='tdr_descripcion')
    vigente = models.BooleanField(default=True, db_column='tdr_vigente')
    class Meta: db_table = 'tipo_docto_rendicion'

class TipoMateriales(models.Model):
    id = models.AutoField(primary_key=True, db_column='tma_id')
    descripcion = models.CharField(max_length=100, db_column='tma_descripcion')
    vigente = models.BooleanField(default=True, db_column='tma_vigente')
    class Meta: db_table = 'tipo_materiales'
