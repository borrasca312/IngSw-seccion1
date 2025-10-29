from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Import all models from the app
from .models import (
    Region, Provincia, Comuna, Zona, Distrito, Grupo, Rama, Nivel,
    EstadoCivil, Cargo, TipoArchivo, TipoCurso, Alimentacion, Rol
)

# Import all serializers from the app
from .serializers import (
    RegionSerializer, ProvinciaSerializer, ComunaSerializer, ZonaSerializer,
    DistritoSerializer, GrupoSerializer, RamaSerializer, NivelSerializer,
    EstadoCivilSerializer, CargoSerializer, TipoArchivoSerializer,
    TipoCursoSerializer, AlimentacionSerializer, RolSerializer
)

# ==============================================================================
# Base ViewSet for Read-Only or Standard CRUD operations on Catalogs
# ==============================================================================

class BaseMaestroViewSet(viewsets.ModelViewSet):
    """Base ViewSet to apply common settings like permissions."""
    permission_classes = [IsAuthenticated]

# ==============================================================================
# ViewSets for Maestros
# ==============================================================================

class RegionViewSet(BaseMaestroViewSet):
    queryset = Region.objects.prefetch_related('provincia_set__comuna_set').all()
    serializer_class = RegionSerializer

class ProvinciaViewSet(BaseMaestroViewSet):
    queryset = Provincia.objects.prefetch_related('comuna_set').all()
    serializer_class = ProvinciaSerializer

class ComunaViewSet(BaseMaestroViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

class ZonaViewSet(BaseMaestroViewSet):
    queryset = Zona.objects.prefetch_related('distrito_set__grupo_set').all()
    serializer_class = ZonaSerializer

class DistritoViewSet(BaseMaestroViewSet):
    queryset = Distrito.objects.prefetch_related('grupo_set').all()
    serializer_class = DistritoSerializer

class GrupoViewSet(BaseMaestroViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

class RamaViewSet(BaseMaestroViewSet):
    queryset = Rama.objects.all()
    serializer_class = RamaSerializer

class NivelViewSet(BaseMaestroViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer

class EstadoCivilViewSet(BaseMaestroViewSet):
    queryset = EstadoCivil.objects.all()
    serializer_class = EstadoCivilSerializer

class CargoViewSet(BaseMaestroViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class TipoArchivoViewSet(BaseMaestroViewSet):
    queryset = TipoArchivo.objects.all()
    serializer_class = TipoArchivoSerializer

class TipoCursoViewSet(BaseMaestroViewSet):
    queryset = TipoCurso.objects.all()
    serializer_class = TipoCursoSerializer

class AlimentacionViewSet(BaseMaestroViewSet):
    queryset = Alimentacion.objects.all()
    serializer_class = AlimentacionSerializer

class RolViewSet(BaseMaestroViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
