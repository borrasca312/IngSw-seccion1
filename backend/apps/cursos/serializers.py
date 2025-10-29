from rest_framework import serializers

# Import models from the current app
from .models import (
    Curso, CursoCoordinador, CursoCuota, CursoFecha, CursoSeccion,
    CursoFormador, CursoAlimentacion, PersonaCurso, PersonaVehiculo,
    PersonaEstadoCurso
)

# Import serializers from other apps
# Se asume que estos serializadores existen y son funcionales.
# Si no, se crearán/actualizarán en pasos posteriores.
from apps.maestros.serializers import (
    TipoCursoSerializer, CargoSerializer, RolSerializer, RamaSerializer,
    AlimentacionSerializer, NivelSerializer
)
from apps.personas.serializers import PersonaSerializer

# ==============================================================================
# Serializers for models related to PersonaCurso (Participant)
# ==============================================================================

class PersonaVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaVehiculo
        fields = '__all__'

class PersonaEstadoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaEstadoCurso
        fields = '__all__'

class PersonaCursoSerializer(serializers.ModelSerializer):
    """Serializer for CREATE/UPDATE operations on PersonaCurso."""
    class Meta:
        model = PersonaCurso
        fields = '__all__'

class PersonaCursoDetailSerializer(serializers.ModelSerializer):
    """Serializer for RETRIEVE operations on PersonaCurso."""
    persona = PersonaSerializer(read_only=True)
    rol = RolSerializer(read_only=True)
    alimentacion = AlimentacionSerializer(read_only=True)
    nivel = NivelSerializer(read_only=True)
    vehiculos = PersonaVehiculoSerializer(many=True, read_only=True, source='personavehiculo_set')
    estados = PersonaEstadoCursoSerializer(many=True, read_only=True, source='personaestadocurso_set')

    class Meta:
        model = PersonaCurso
        fields = '__all__'

class SimplePersonaCursoSerializer(serializers.ModelSerializer):
    """A minimal serializer for listing participants within a course view."""
    persona = PersonaSerializer(read_only=True)

    class Meta:
        model = PersonaCurso
        fields = ('id', 'persona', 'acreditado')

# ==============================================================================
# Serializers for models related to Curso
# ==============================================================================

class CursoCoordinadorSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer(read_only=True)
    cargo = CargoSerializer(read_only=True)
    class Meta:
        model = CursoCoordinador
        fields = '__all__'

class CursoCuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoCuota
        fields = '__all__'

class CursoFechaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoFecha
        fields = '__all__'

class CursoSeccionSerializer(serializers.ModelSerializer):
    rama = RamaSerializer(read_only=True)
    class Meta:
        model = CursoSeccion
        fields = '__all__'

class CursoFormadorSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer(read_only=True)
    rol = RolSerializer(read_only=True)
    class Meta:
        model = CursoFormador
        fields = '__all__'

class CursoAlimentacionSerializer(serializers.ModelSerializer):
    alimentacion = AlimentacionSerializer(read_only=True)
    class Meta:
        model = CursoAlimentacion
        fields = '__all__'

# ==============================================================================
# Main Serializers for Curso
# ==============================================================================

class CursoSerializer(serializers.ModelSerializer):
    """
    Serializer for LIST and CREATE/UPDATE operations on Curso.
    Uses primary keys for relationships to allow writing.
    """
    class Meta:
        model = Curso
        fields = '__all__'
        read_only_fields = ('usuario', 'fecha_hora')

    def create(self, validated_data):
        # Automatically set the creating user from the request context
        if 'request' in self.context:
            validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)

class CursoDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for RETRIEVE operations on Curso.
    Provides a full, nested, read-only representation.
    """
    tipo_curso = TipoCursoSerializer(read_only=True)
    responsable = PersonaSerializer(read_only=True)
    cargo_responsable = CargoSerializer(read_only=True)
    
    coordinadores = CursoCoordinadorSerializer(many=True, read_only=True, source='cursocoordinador_set')
    cuotas = CursoCuotaSerializer(many=True, read_only=True, source='cursocuota_set')
    fechas = CursoFechaSerializer(many=True, read_only=True, source='cursofecha_set')
    secciones = CursoSeccionSerializer(many=True, read_only=True, source='cursoseccion_set')
    formadores = CursoFormadorSerializer(many=True, read_only=True, source='cursoformador_set')
    alimentacion = CursoAlimentacionSerializer(many=True, read_only=True, source='cursoalimentacion_set')
    participantes = serializers.SerializerMethodField()
    total_participantes = serializers.SerializerMethodField()
    total_formadores = serializers.SerializerMethodField()
    monto_recaudado = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = [
            'id', 'tipo_curso', 'responsable', 'cargo_responsable', 'lugar_comuna',
            'fecha_hora', 'fecha_solicitud', 'codigo', 'descripcion', 'observacion',
            'administra', 'cuota_con_almuerzo', 'cuota_sin_almuerzo', 'modalidad',
            'lugar', 'estado', 'usuario',
            'coordinadores', 'cuotas', 'fechas', 'secciones', 'formadores',
            'alimentacion', 'participantes', 'total_participantes', 'total_formadores',
            'monto_recaudado'
        ]

    def get_participantes(self, obj):
        """Gathers all participants from all sections of the course."""
        secciones_ids = obj.cursoseccion_set.values_list('id', flat=True)
        participantes_qs = PersonaCurso.objects.filter(curso_seccion_id__in=secciones_ids)
        return SimplePersonaCursoSerializer(participantes_qs, many=True).data

    def get_total_participantes(self, obj):
        """Calculates the total number of participants in the course."""
        secciones_ids = obj.cursoseccion_set.values_list('id', flat=True)
        return PersonaCurso.objects.filter(curso_seccion_id__in=secciones_ids).count()

    def get_total_formadores(self, obj):
        """Calculates the total number of trainers in the course."""
        return obj.cursoformador_set.count()

    def get_monto_recaudado(self, obj):
        """Calculates the total amount of money raised from payments for the course."""
        from apps.pagos.models import PagoPersona
        from django.db.models import Sum
        
        total = PagoPersona.objects.filter(curso=obj).aggregate(total_valor=Sum('valor'))['total_valor']
        return total or 0.0
