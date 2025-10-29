from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Import all models from the app
from .models import (
    Proveedor, ComprobantePago, PagoPersona, PagoComprobante,
    PagoCambioPersona, Prepago
)

# Import all serializers from the app
from .serializers import (
    ProveedorSerializer, ComprobantePagoSerializer, ComprobantePagoDetailSerializer,
    PagoPersonaSerializer, PagoPersonaDetailSerializer, PagoComprobanteSerializer,
    PagoCambioPersonaSerializer, PrepagoSerializer
)

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated]

class PagoPersonaViewSet(viewsets.ModelViewSet):
    queryset = PagoPersona.objects.select_related('usuario', 'persona', 'curso').all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PagoPersonaDetailSerializer
        return PagoPersonaSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class ComprobantePagoViewSet(viewsets.ModelViewSet):
    queryset = ComprobantePago.objects.select_related('usuario', 'proveedor').all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ComprobantePagoDetailSerializer
        return ComprobantePagoSerializer

    def perform_create(self, serializer):
        # The user is now set within the serializer's create method
        # using the request context.
        serializer.save()

class PagoComprobanteViewSet(viewsets.ModelViewSet):
    queryset = PagoComprobante.objects.select_related('pago', 'comprobante').all()
    serializer_class = PagoComprobanteSerializer
    permission_classes = [IsAuthenticated]

class PagoCambioPersonaViewSet(viewsets.ModelViewSet):
    queryset = PagoCambioPersona.objects.select_related('usuario', 'pago_persona', 'persona_nueva').all()
    serializer_class = PagoCambioPersonaSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class PrepagoViewSet(viewsets.ModelViewSet):
    queryset = Prepago.objects.select_related('persona', 'pago_persona').all()
    serializer_class = PrepagoSerializer
    permission_classes = [IsAuthenticated]
