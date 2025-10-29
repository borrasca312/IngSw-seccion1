from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "pagos"

router = DefaultRouter()

# Registering all the ViewSets from views.py
router.register(r'proveedores', views.ProveedorViewSet, basename='proveedor')
router.register(r'pagos-persona', views.PagoPersonaViewSet, basename='pagopersona')
router.register(r'comprobantes', views.ComprobantePagoViewSet, basename='comprobantepago')
router.register(r'pagos-comprobantes', views.PagoComprobanteViewSet, basename='pagocomprobante')
router.register(r'cambios-persona', views.PagoCambioPersonaViewSet, basename='pagocambiopersona')
router.register(r'prepagos', views.PrepagoViewSet, basename='prepago')

urlpatterns = [
    path('', include(router.urls)),
]
