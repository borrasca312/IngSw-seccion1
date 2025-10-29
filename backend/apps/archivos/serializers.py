from rest_framework import serializers

# Import models from the current app
from .models import Archivo, ArchivoCurso, ArchivoPersona

# Import serializers from other apps
from apps.maestros.serializers import TipoArchivoSerializer
from apps.autenticacion.serializers import UsuarioSerializer
from apps.cursos.serializers import CursoSeccionSerializer
from apps.personas.serializers import PersonaSerializer

# ==============================================================================
# Main Serializers for Archivos App
# ==============================================================================

class ArchivoSerializer(serializers.ModelSerializer):
    """Serializer for CREATE/UPDATE operations on Archivo."""
    class Meta:
        model = Archivo
        fields = '__all__'
        read_only_fields = ('usuario_crea', 'usuario_modifica', 'fecha_creacion', 'fecha_modificacion')

    def create(self, validated_data):
        if 'request' in self.context:
            validated_data['usuario_crea'] = self.context['request'].user
            validated_data['usuario_modifica'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'request' in self.context:
            validated_data['usuario_modifica'] = self.context['request'].user
        return super().update(instance, validated_data)

class ArchivoDetailSerializer(serializers.ModelSerializer):
    """Serializer for RETRIEVE operations on Archivo."""
    tipo_archivo = TipoArchivoSerializer(read_only=True)
    usuario_crea = UsuarioSerializer(read_only=True)
    usuario_modifica = UsuarioSerializer(read_only=True)

    class Meta:
        model = Archivo
        fields = '__all__'

class ArchivoCursoSerializer(serializers.ModelSerializer):
    """Serializer for the relationship between Archivo and Curso."""
    archivo = ArchivoDetailSerializer(read_only=True)
    curso_seccion = CursoSeccionSerializer(read_only=True)

    class Meta:
        model = ArchivoCurso
        fields = '__all__'

class ArchivoPersonaSerializer(serializers.ModelSerializer):
    """Serializer for the relationship between Archivo and Persona."""
    archivo = ArchivoDetailSerializer(read_only=True)
    persona = PersonaSerializer(read_only=True)
    curso_seccion = CursoSeccionSerializer(read_only=True)

    class Meta:
        model = ArchivoPersona
        fields = '__all__'
