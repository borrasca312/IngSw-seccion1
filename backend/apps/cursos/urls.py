from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "cursos"

router = DefaultRouter()

# Registering all the ViewSets from views.py
router.register(r'cursos', views.CursoViewSet, basename='curso')
router.register(r'coordinadores', views.CursoCoordinadorViewSet, basename='cursocoordinador')
router.register(r'cuotas', views.CursoCuotaViewSet, basename='cursocuota')
router.register(r'fechas', views.CursoFechaViewSet, basename='cursofecha')
router.register(r'secciones', views.CursoSeccionViewSet, basename='cursoseccion')
router.register(r'formadores', views.CursoFormadorViewSet, basename='cursoformador')
router.register(r'alimentacion', views.CursoAlimentacionViewSet, basename='cursoalimentacion')
router.register(r'participantes', views.PersonaCursoViewSet, basename='personacurso')
router.register(r'vehiculos', views.PersonaVehiculoViewSet, basename='personavehiculo')
router.register(r'estados-participante', views.PersonaEstadoCursoViewSet, basename='personaestadocurso')

urlpatterns = [
    path('', include(router.urls)),
]
