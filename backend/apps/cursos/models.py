from django.db import models
from apps.autenticacion.models import Usuario
from apps.personas.models import Persona
from apps.maestros.models import TipoCurso, Comuna, Cargo, Rol, Rama, Alimentacion, Nivel

class Curso(models.Model):
    id = models.AutoField(primary_key=True, db_column='cur_id')
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, db_column='usu_id')
    tipo_curso = models.ForeignKey(TipoCurso, on_delete=models.PROTECT, db_column='tcu_id')
    responsable = models.ForeignKey(Persona, on_delete=models.PROTECT, db_column='per_id_responsable', related_name='cursos_responsable')
    cargo_responsable = models.ForeignKey(Cargo, on_delete=models.PROTECT, db_column='car_id_responsable')
    lugar_comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True, blank=True, db_column='com_id_lugar')
    fecha_hora = models.DateTimeField(auto_now_add=True, db_column='cur_fecha_hora')
    fecha_solicitud = models.DateTimeField(db_column='cur_fecha_solicitud')
    codigo = models.CharField(max_length=10, db_column='cur_codigo')
    descripcion = models.CharField(max_length=50, blank=True, db_column='cur_descripcion')
    observacion = models.CharField(max_length=255, blank=True, db_column='cur_observacion')
    administra = models.IntegerField(db_column='cur_administra')
    cuota_con_almuerzo = models.DecimalField(max_digits=21, decimal_places=6, db_column='cur_cuota_con_almuerzo')
    cuota_sin_almuerzo = models.DecimalField(max_digits=21, decimal_places=6, db_column='cur_cuota_sin_almuerzo')
    modalidad = models.IntegerField(db_column='cur_modalidad')
    lugar = models.CharField(max_length=100, blank=True, db_column='cur_lugar')
    estado = models.IntegerField(db_column='cur_estado')

    class Meta:
        db_table = 'curso'

class CursoCoordinador(models.Model):
    id = models.AutoField(primary_key=True, db_column='cuc_id')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, db_column='cur_id')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, db_column='car_id')
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='per_id')
    cargo_descripcion = models.CharField(max_length=100, blank=True, db_column='cuc_cargo')
    class Meta: db_table = 'curso_coordinador'

class CursoCuota(models.Model):
    id = models.AutoField(primary_key=True, db_column='cuu_id')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, db_column='cur_id')
    tipo = models.IntegerField(db_column='cuu_tipo')
    fecha = models.DateTimeField(db_column='cuu_fecha')
    valor = models.DecimalField(max_digits=21, decimal_places=6, db_column='cuu_valor')
    class Meta: db_table = 'curso_cuota'

class CursoFecha(models.Model):
    id = models.AutoField(primary_key=True, db_column='cuf_id')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, db_column='cur_id')
    fecha_inicio = models.DateTimeField(db_column='cuf_fecha_inicio')
    fecha_termino = models.DateTimeField(db_column='cuf_fecha_termino')
    tipo = models.IntegerField(db_column='cuf_tipo')
    class Meta: db_table = 'curso_fecha'

class CursoSeccion(models.Model):
    id = models.AutoField(primary_key=True, db_column='cus_id')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, db_column='cur_id')
    rama = models.ForeignKey(Rama, on_delete=models.SET_NULL, null=True, blank=True, db_column='ram_id')
    seccion = models.IntegerField(db_column='cus_seccion')
    cantidad_participante = models.IntegerField(db_column='cus_cant_participante')
    class Meta: db_table = 'curso_seccion'

class CursoFormador(models.Model):
    id = models.AutoField(primary_key=True, db_column='cuo_id')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, db_column='cur_id')
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='per_id')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, db_column='rol_id')
    curso_seccion = models.ForeignKey(CursoSeccion, on_delete=models.CASCADE, db_column='cus_id')
    director = models.BooleanField(db_column='cuo_director')
    class Meta: db_table = 'curso_formador'

class CursoAlimentacion(models.Model):
    id = models.AutoField(primary_key=True, db_column='cua_id')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, db_column='cur_id')
    alimentacion = models.ForeignKey(Alimentacion, on_delete=models.CASCADE, db_column='ali_id')
    fecha = models.DateTimeField(db_column='cua_fecha')
    tiempo = models.IntegerField(db_column='cua_tiempo')
    descripcion = models.CharField(max_length=100, db_column='cua_descripcion')
    cantidad_adicional = models.IntegerField(db_column='cua_cantidad_adicional')
    vigente = models.BooleanField(db_column='cua_vigente')
    class Meta: db_table = 'curso_alimentacion'

class PersonaCurso(models.Model):
    id = models.AutoField(primary_key=True, db_column='pec_id')
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='per_id')
    curso_seccion = models.ForeignKey(CursoSeccion, on_delete=models.CASCADE, db_column='cus_id')
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT, db_column='rol_id')
    alimentacion = models.ForeignKey(Alimentacion, on_delete=models.CASCADE, db_column='ali_id')
    nivel = models.ForeignKey(Nivel, on_delete=models.SET_NULL, null=True, blank=True, db_column='niv_id')
    observacion = models.TextField(blank=True, db_column='pec_observacion')
    registro = models.BooleanField(db_column='pec_registro')
    acreditado = models.BooleanField(db_column='pec_acreditado')
    class Meta: db_table = 'persona_curso'

class PersonaVehiculo(models.Model):
    id = models.AutoField(primary_key=True, db_column='pev_id')
    persona_curso = models.ForeignKey(PersonaCurso, on_delete=models.CASCADE, db_column='pec_id')
    marca = models.CharField(max_length=50, db_column='pev_marca')
    modelo = models.CharField(max_length=50, db_column='pev_modelo')
    patente = models.CharField(max_length=10, db_column='pev_patente')
    class Meta: db_table = 'persona_vehiculo'

class PersonaEstadoCurso(models.Model):
    id = models.AutoField(primary_key=True, db_column='peu_id')
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, db_column='usu_id')
    persona_curso = models.ForeignKey(PersonaCurso, on_delete=models.CASCADE, db_column='pec_id')
    fecha_hora = models.DateTimeField(auto_now_add=True, db_column='peu_fecha_hora')
    estado = models.IntegerField(db_column='peu_estado')
    vigente = models.BooleanField(db_column='peu_vigente')
    class Meta: db_table = 'persona_estado_curso'
