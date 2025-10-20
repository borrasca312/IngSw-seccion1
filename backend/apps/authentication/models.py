"""
Modelos de autenticación para SGICS - Sistema de Gestión Integral de Cursos Scout

Este módulo define el sistema de usuarios y roles basado en RBAC (Role-Based Access Control).
Extiende el modelo User de Django para incluir campos específicos del movimiento Scout.

Entidades principales:
- User: Usuario del sistema con datos Scout
- Role: Roles del sistema (Admin, Coordinador, Dirigente, etc.)
- RoleAssignment: Asignación de roles a usuarios con contexto

TODO: El equipo A debe completar:
- Validación completa de RUT chileno en utils.rut_validator
- Integración con grupos Scout regionales
- Permisos granulares por módulo del sistema
- Campos adicionales de perfil Scout (grupo, rama, cargo)
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import JSONField  # Requiere Django 3.1+ o PostgreSQL

# Opciones para ramas Scout
RAMAS_SCOUT = [
    ('lobatos', 'Lobatos'),
    ('scouts', 'Scouts'),
    ('caminantes', 'Caminantes'),
    ('rovers', 'Rovers'),
]

class User(AbstractUser):
    """
    Usuario extendido para el sistema Scout con campos específicos de la organización.
    """

    rut = models.CharField(
        max_length=12,
        unique=True,
        null=True,
        blank=True,
        verbose_name="RUT",
        help_text="RUT sin puntos y con guión (ej: 12345678-9)"
    )

    telefono = models.CharField(
        max_length=15,
        blank=True,
        verbose_name="Teléfono de contacto"
    )

    fecha_nacimiento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha de nacimiento"
    )

    rama = models.CharField(
        max_length=20,
        choices=RAMAS_SCOUT,
        blank=True,
        verbose_name="Rama Scout actual"
    )

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set',
        related_query_name='custom_user'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',
        related_query_name='custom_user'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        """Validación del RUT usando utilitario externo"""
        if self.rut:
            try:
                from utils.rut_validator import validar_rut
                if not validar_rut(self.rut):
                    raise ValidationError({'rut': 'RUT inválido'})
            except ImportError:
                raise ValidationError({'rut': 'No se pudo importar el validador de RUT'})

    class Meta:
        db_table = 'auth_user_extended'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return self.get_full_name() or self.username


class Role(models.Model):
    """
    Roles del sistema Scout
    """
    code = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    permissions = JSONField(blank=True, null=True, help_text="Permisos específicos del rol")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'auth_roles'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.name


class RoleAssignment(models.Model):
    """
    Asignación de roles con soporte para auditoría y alcance
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='role_assignments')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    scope_type = models.CharField(max_length=50, blank=True, null=True)
    scope_id = models.PositiveIntegerField(blank=True, null=True)
    assigned_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_roles')
    expires_at = models.DateTimeField(blank=True, null=True)

    assigned_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'auth_role_assignments'
        unique_together = ('user', 'role')

    def __str__(self):
        return f"{self.user.username} → {self.role.code}"

    @staticmethod
    def user_has_role(user, role_code):
        return RoleAssignment.objects.filter(user=user, role__code=role_code, is_active=True).exists()

    @staticmethod
    def get_user_roles(user):
        return Role.objects.filter(roleassignment__user=user, roleassignment__is_active=True)