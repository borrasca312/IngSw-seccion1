from django.contrib import admin
from .models import Curso, CursoCoordinador, CursoCuota, CursoFecha, CursoSeccion, CursoFormador, CursoAlimentacion, PersonaCurso, PersonaVehiculo, PersonaEstadoCurso

admin.site.register(Curso)
admin.site.register(CursoCoordinador)
admin.site.register(CursoCuota)
admin.site.register(CursoFecha)
admin.site.register(CursoSeccion)
admin.site.register(CursoFormador)
admin.site.register(CursoAlimentacion)
admin.site.register(PersonaCurso)
admin.site.register(PersonaVehiculo)
admin.site.register(PersonaEstadoCurso)
