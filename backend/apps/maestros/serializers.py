from rest_framework import serializers
from .models import (
    Region, Provincia, Comuna, Zona, Distrito, Grupo, Rama, Nivel,
    EstadoCivil, Cargo, TipoArchivo, TipoCurso, Alimentacion, Rol
)

# ==============================================================================
# Basic Catalog Serializers (no nesting)
# ==============================================================================

class RamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rama
        fields = '__all__'

class NivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = '__all__'

class EstadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivil
        fields = '__all__'

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class TipoArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoArchivo
        fields = '__all__'

class TipoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCurso
        fields = '__all__'

class AlimentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentacion
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

# ==============================================================================
# Hierarchical Serializers (with nesting for read-only context)
# ==============================================================================

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'

class DistritoSerializer(serializers.ModelSerializer):
    grupos = GrupoSerializer(many=True, read_only=True, source='grupo_set')
    class Meta:
        model = Distrito
        fields = '__all__'

class ZonaSerializer(serializers.ModelSerializer):
    distritos = DistritoSerializer(many=True, read_only=True, source='distrito_set')
    class Meta:
        model = Zona
        fields = '__all__'

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'

class ProvinciaSerializer(serializers.ModelSerializer):
    comunas = ComunaSerializer(many=True, read_only=True, source='comuna_set')
    class Meta:
        model = Provincia
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    provincias = ProvinciaSerializer(many=True, read_only=True, source='provincia_set')
    class Meta:
        model = Region
        fields = '__all__'
