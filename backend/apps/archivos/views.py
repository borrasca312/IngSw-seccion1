from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Import all models from the app
from .models import Archivo, ArchivoCurso, ArchivoPersona

# Import all serializers from the app
from .serializers import (
    ArchivoSerializer, ArchivoDetailSerializer,
    ArchivoCursoSerializer, ArchivoPersonaSerializer
)

class ArchivoViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Archivo model.
    Dynamically selects serializer based on the action.
    """
    queryset = Archivo.objects.select_related(
        'tipo_archivo', 'usuario_crea', 'usuario_modifica'
    ).all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ArchivoDetailSerializer
        return ArchivoSerializer

    def perform_create(self, serializer):
        # The user is now set within the serializer's create method
        # using the request context.
        serializer.save()

    def perform_update(self, serializer):
        # The user is now set within the serializer's update method
        # using the request context.
        serializer.save()

class ArchivoCursoViewSet(viewsets.ModelViewSet):
    queryset = ArchivoCurso.objects.select_related(
        'archivo', 'curso_seccion'
    ).all()
    serializer_class = ArchivoCursoSerializer
    permission_classes = [IsAuthenticated]

class ArchivoPersonaViewSet(viewsets.ModelViewSet):
    queryset = ArchivoPersona.objects.select_related(
        'archivo', 'persona', 'curso_seccion'
    ).all()
    serializer_class = ArchivoPersonaSerializer
    permission_classes = [IsAuthenticated]
