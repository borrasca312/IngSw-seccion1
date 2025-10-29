from django.db import models
from django.utils import timezone
from apps.autenticacion.models import Usuario
from apps.personas.models import Persona
from apps.cursos.models import Curso, PersonaCurso
from apps.maestros.models import ConceptoContable

class PagoPersona(models.Model):
    id = models.AutoField(primary_key=True, db_column='pap_id')
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT, db_column='per_id')
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, db_column='cur_id')
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, db_column='usu_id')
    fecha_hora = models.DateTimeField(default=timezone.now, db_column='pap_fecha_hora')
    tipo = models.IntegerField(db_column='pap_tipo')
    valor = models.DecimalField(max_digits=21, decimal_places=6, db_column='pap_valor')
    observacion = models.CharField(max_length=100, null=True, blank=True, db_column='pap_observacion')

    class Meta:
        db_table = 'pago_persona'

class PagoCambioPersona(models.Model):
    id = models.AutoField(primary_key=True, db_column='pcp_id')
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT, db_column='per_id')
    pago_persona = models.ForeignKey(PagoPersona, on_delete=models.PROTECT, db_column='pap_id')
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, db_column='usu_id')
    fecha_hora = models.DateTimeField(default=timezone.now, db_column='pcp_fecha_hora')

    class Meta:
        db_table = 'pago_cambio_persona'

class Prepago(models.Model):
    id = models.AutoField(primary_key=True, db_column='ppa_id')
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT, db_column='per_id')
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, db_column='cur_id')
    pago_persona = models.ForeignKey(PagoPersona, on_delete=models.SET_NULL, null=True, blank=True, db_column='pap_id')
    valor = models.DecimalField(max_digits=21, decimal_places=6, db_column='ppa_valor')
    observacion = models.TextField(null=True, blank=True, db_column='ppa_observacion')
    vigente = models.BooleanField(db_column='ppa_vigente')

    class Meta:
        db_table = 'prepago'

class ComprobantePago(models.Model):
    id = models.AutoField(primary_key=True, db_column='cpa_id')
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, db_column='usu_id')
    persona_curso = models.ForeignKey(PersonaCurso, on_delete=models.PROTECT, db_column='pec_id')
    concepto_contable = models.ForeignKey(ConceptoContable, on_delete=models.PROTECT, db_column='coc_id')
    fecha_hora = models.DateTimeField(default=timezone.now, db_column='cpa_fecha_hora')
    fecha = models.DateField(db_column='cpa_fecha')
    numero = models.IntegerField(db_column='cpa_numero')
    valor = models.DecimalField(max_digits=21, decimal_places=6, db_column='cpa_valor')

    class Meta:
        db_table = 'comprobante_pago'

class PagoComprobante(models.Model):
    id = models.AutoField(primary_key=True, db_column='pco_id')
    pago_persona = models.ForeignKey(PagoPersona, on_delete=models.CASCADE, db_column='pap_id')
    comprobante_pago = models.ForeignKey(ComprobantePago, on_delete=models.CASCADE, db_column='cpa_id')

    class Meta:
        db_table = 'pago_comprobante'

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True, db_column='prv_id')
    descripcion = models.CharField(max_length=100, db_column='prv_descripcion')
    celular1 = models.CharField(max_length=15, db_column='prv_celular1')
    celular2 = models.CharField(max_length=15, null=True, blank=True, db_column='prv_celular2')
    direccion = models.CharField(max_length=100, db_column='prv_direccion')
    observacion = models.TextField(null=True, blank=True, db_column='prv_observacion')
    vigente = models.BooleanField(default=True, db_column='prv_vigente')

    class Meta:
        db_table = 'proveedor'
