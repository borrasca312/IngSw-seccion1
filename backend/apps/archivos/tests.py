import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status

from apps.autenticacion.models import Usuario as User
from apps.cursos.models import Curso as Course

@pytest.fixture
def create_course(db):
    return Course.objects.create(title="Curso de Prueba", code="CP-01")
