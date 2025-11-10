import { defineStore } from 'pinia';
import apiClient from '@/services/api';

interface ExecutiveMetrics {
  cursosActivos: number;
  totalParticipantes: number;
  ingresosMes: number;
  tasaCompletitud: number;
  participantesPorRama: Array<{ nombre: string; num_participantes: number }>;
  ingresosMensuales: Array<{ mes: string; ingresos: number }>;
}

export const useDashboardStore = defineStore('dashboard', {
  state: () => ({
    stats: null as any | null,
    executiveMetrics: null as ExecutiveMetrics | null,
    loading: false,
    error: null as string | null,
  }),

  actions: {
    async fetchStats() {
      this.loading = true;
      this.error = null;
      try {
        const response = await apiClient.get('/cursos/dashboard-stats/');
        this.stats = response.data;
      } catch (error: any) {
        this.error = error.message || 'Error al cargar las estadísticas.';
      } finally {
        this.loading = false;
      }
    },

    async fetchExecutiveMetrics(period: string = 'month') {
      this.loading = true;
      this.error = null;
      try {
        const response = await apiClient.get(`/dashboard/executive-metrics/?period=${period}`);
        this.executiveMetrics = response.data;
      } catch (error: any) {
        this.error = error.message || 'Error al cargar métricas ejecutivas.';
        
        //Datos de desarrollo
        this.executiveMetrics = {
          cursosActivos: 12,
          totalParticipantes: 245,
          ingresosMes: 1250000,
          tasaCompletitud: 87,
          participantesPorRama: [
            { nombre: 'Lobatos', num_participantes: 45 },
            { nombre: 'Scouts', num_participantes: 78 },
            { nombre: 'Pioneros', num_participantes: 65 },
            { nombre: 'Rovers', num_participantes: 57 }
          ],
          ingresosMensuales: [
            { mes: 'Enero', ingresos: 800000 },
            { mes: 'Febrero', ingresos: 950000 },
            { mes: 'Marzo', ingresos: 1100000 },
            { mes: 'Abril', ingresos: 1250000 },
            { mes: 'Mayo', ingresos: 1180000 },
            { mes: 'Junio', ingresos: 1350000 }
          ]
        };
      } finally {
        this.loading = false;
      }
    },
  },
});
