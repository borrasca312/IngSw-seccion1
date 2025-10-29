from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Import all models from the app
from .models import (
    Curso, CursoCoordinador, CursoCuota, CursoFecha, CursoSeccion,
    CursoFormador, CursoAlimentacion, PersonaCurso, PersonaVehiculo,
    PersonaEstadoCurso
)

# Import all serializers from the app
from .serializers import (
    CursoSerializer, CursoDetailSerializer,
    CursoCoordinadorSerializer, CursoCuotaSerializer, CursoFechaSerializer,
    CursoSeccionSerializer, CursoFormadorSerializer, CursoAlimentacionSerializer,
    PersonaCursoSerializer, PersonaCursoDetailSerializer,
    PersonaVehiculoSerializer, PersonaEstadoCursoSerializer
)

class CursoViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Curso model.
    Dynamically selects serializer based on the action.
    - CursoDetailSerializer for read operations ('list', 'retrieve').
    - CursoSerializer for write operations ('create', 'update', 'partial_update').
    """
    queryset = Curso.objects.all().order_by('-fecha_solicitud')
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CursoDetailSerializer
        return CursoSerializer

    def perform_create(self, serializer):
        # The user is now set within the serializer's create method
        # using the request context.
        serializer.save()

class CursoCoordinadorViewSet(viewsets.ModelViewSet):
    queryset = CursoCoordinador.objects.all()
    serializer_class = CursoCoordinadorSerializer
    permission_classes = [IsAuthenticated]

class CursoCuotaViewSet(viewsets.ModelViewSet):
    queryset = CursoCuota.objects.all()
    serializer_class = CursoCuotaSerializer
    permission_classes = [IsAuthenticated]

class CursoFechaViewSet(viewsets.ModelViewSet):
    queryset = CursoFecha.objects.all()
    serializer_class = CursoFechaSerializer
    permission_classes = [IsAuthenticated]

class CursoSeccionViewSet(viewsets.ModelViewSet):
    queryset = CursoSeccion.objects.all()
    serializer_class = CursoSeccionSerializer
    permission_classes = [IsAuthenticated]

class CursoFormadorViewSet(viewsets.ModelViewSet):
    queryset = CursoFormador.objects.all()
    serializer_class = CursoFormadorSerializer
    permission_classes = [IsAuthenticated]

class CursoAlimentacionViewSet(viewsets.ModelViewSet):
    queryset = CursoAlimentacion.objects.all()
    serializer_class = CursoAlimentacionSerializer
    permission_classes = [IsAuthenticated]

class PersonaCursoViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the PersonaCurso model.
    Uses PersonaCursoDetailSerializer for read operations.
    """
    queryset = PersonaCurso.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PersonaCursoDetailSerializer
        return PersonaCursoSerializer

class PersonaVehiculoViewSet(viewsets.ModelViewSet):
    queryset = PersonaVehiculo.objects.all()
    serializer_class = PersonaVehiculoSerializer
    permission_classes = [IsAuthenticated]

class PersonaEstadoCursoViewSet(viewsets.ModelViewSet):
    queryset = PersonaEstadoCurso.objects.all()
    serializer_class = PersonaEstadoCursoSerializer
    permission_classes = [IsAuthenticated]
