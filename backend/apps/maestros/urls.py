from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "maestros"

router = DefaultRouter()

# Registering all the ViewSets from views.py
router.register(r'regiones', views.RegionViewSet, basename='region')
router.register(r'provincias', views.ProvinciaViewSet, basename='provincia')
router.register(r'comunas', views.ComunaViewSet, basename='comuna')
router.register(r'zonas', views.ZonaViewSet, basename='zona')
router.register(r'distritos', views.DistritoViewSet, basename='distrito')
router.register(r'grupos', views.GrupoViewSet, basename='grupo')
router.register(r'ramas', views.RamaViewSet, basename='rama')
router.register(r'niveles', views.NivelViewSet, basename='nivel')
router.register(r'estados-civiles', views.EstadoCivilViewSet, basename='estadocivil')
router.register(r'cargos', views.CargoViewSet, basename='cargo')
router.register(r'tipos-archivo', views.TipoArchivoViewSet, basename='tipoarchivo')
router.register(r'tipos-curso', views.TipoCursoViewSet, basename='tipocurso')
router.register(r'alimentaciones', views.AlimentacionViewSet, basename='alimentacion')
router.register(r'roles', views.RolViewSet, basename='rol')

urlpatterns = [
    path('', include(router.urls)),
]
