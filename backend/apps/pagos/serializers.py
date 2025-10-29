from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

# Import models from the current app
from .models import (
    Proveedor, ComprobantePago, PagoPersona, PagoComprobante,
    PagoCambioPersona, Prepago
)

# Import serializers from other apps
from apps.personas.serializers import PersonaSerializer
from apps.cursos.serializers import CursoSerializer
from apps.autenticacion.serializers import UsuarioSerializer

# ==============================================================================
# Main Serializers for Pagos App
# ==============================================================================

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class PrepagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prepago
        fields = '__all__'

class PagoCambioPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagoCambioPersona
        fields = '__all__'
        read_only_fields = ('fecha_hora', 'usuario')

# --- PagoPersona Serializers ---

class PagoPersonaSerializer(serializers.ModelSerializer):
    """Serializer for CREATE/UPDATE operations on PagoPersona."""
    class Meta:
        model = PagoPersona
        fields = '__all__'
        read_only_fields = ('fecha_hora', 'usuario')

    def validate_valor(self, value):
        if value <= 0:
            raise ValidationError("El valor del pago debe ser mayor a 0.")
        return value

class PagoPersonaDetailSerializer(serializers.ModelSerializer):
    """Serializer for RETRIEVE operations on PagoPersona."""
    persona = PersonaSerializer(read_only=True)
    curso = CursoSerializer(read_only=True)
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = PagoPersona
        fields = '__all__'

# --- ComprobantePago Serializers ---

class PagoComprobanteSerializer(serializers.ModelSerializer):
    """Intermediate serializer for PagoComprobante relationship."""
    pago = PagoPersonaDetailSerializer(read_only=True)
    class Meta:
        model = PagoComprobante
        fields = ('pago',)

class ComprobantePagoSerializer(serializers.ModelSerializer):
    """Serializer for CREATE operations on ComprobantePago."""
    pagos_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        help_text="Lista de IDs de los pagos (PagoPersona) a asociar."
    )

    class Meta:
        model = ComprobantePago
        fields = '__all__'
        read_only_fields = ('fecha_hora', 'usuario', 'valor')

    @transaction.atomic
    def create(self, validated_data):
        pagos_ids = validated_data.pop('pagos_ids')
        
        if not pagos_ids:
            raise ValidationError({"pagos_ids": "Esta lista no puede estar vacía."})
        
        pagos = PagoPersona.objects.filter(id__in=pagos_ids)
        if len(pagos) != len(set(pagos_ids)):
            raise ValidationError({"pagos_ids": "Uno o más IDs de pago no son válidos."})

        # Check if any of the payments are already associated with another comprobante
        if PagoComprobante.objects.filter(pago__in=pagos).exists():
            raise ValidationError({"pagos_ids": "Uno o más pagos ya están asociados a otro comprobante."})

        total_valor = sum(pago.valor for pago in pagos)
        validated_data['valor'] = total_valor
        
        if 'request' in self.context:
            validated_data['usuario'] = self.context['request'].user

        comprobante = ComprobantePago.objects.create(**validated_data)

        PagoComprobante.objects.bulk_create(
            [PagoComprobante(pago=pago, comprobante=comprobante) for pago in pagos]
        )

        return comprobante

class ComprobantePagoDetailSerializer(serializers.ModelSerializer):
    """Serializer for RETRIEVE operations on ComprobantePago."""
    usuario = UsuarioSerializer(read_only=True)
    proveedor = ProveedorSerializer(read_only=True)
    pagos = serializers.SerializerMethodField()

    class Meta:
        model = ComprobantePago
        fields = '__all__'

    def get_pagos(self, obj):
        """Retrieve the full details of associated payments."""
        pagos_rel = PagoComprobante.objects.filter(comprobante=obj)
        pagos = [rel.pago for rel in pagos_rel]
        return PagoPersonaDetailSerializer(pagos, many=True).data
