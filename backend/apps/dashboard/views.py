from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.cursos.models import Curso
from apps.personas.models import Persona
from apps.pagos.models import PagoPersona
from django.db.models import Sum

class DashboardMetricsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cursos_activos = Curso.objects.filter(estado='Activo').count()
        participantes = Persona.objects.count() # This is a simplification. A more accurate count would be based on inscriptions.
        ingresos_totales = PagoPersona.objects.filter(PAP_TIPO=1).aggregate(Sum('PAP_VALOR'))['PAP_VALOR__sum'] or 0
        
        # This is a simplification. A more accurate calculation would be needed based on course costs and payments.
        pagos_pendientes = 0 

        metrics = {
            'cursos_activos': cursos_activos,
            'participantes': participantes,
            'ingresos_totales': ingresos_totales,
            'pagos_pendientes': pagos_pendientes,
        }
        return Response(metrics)
