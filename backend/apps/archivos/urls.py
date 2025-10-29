from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "archivos"

router = DefaultRouter()

# Registering all the ViewSets from views.py
router.register(r'archivos', views.ArchivoViewSet, basename='archivo')
router.register(r'archivos-curso', views.ArchivoCursoViewSet, basename='archivocurso')
router.register(r'archivos-persona', views.ArchivoPersonaViewSet, basename='archivopersona')

urlpatterns = [
    path('', include(router.urls)),
]
