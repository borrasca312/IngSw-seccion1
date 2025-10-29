from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsTreasurerOrAdminOrReadOnly(BasePermission):
    """
    Permiso personalizado para permitir que solo los tesoreros o administradores
    puedan crear, actualizar o eliminar pagos.
    Los demás usuarios solo pueden ver (lectura).
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        return request.user and (request.user.is_staff or hasattr(request.user, 'is_treasurer') and request.user.is_treasurer)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
