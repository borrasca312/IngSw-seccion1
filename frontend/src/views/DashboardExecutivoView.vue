<template>
  <div class="executive-dashboard">
    <header class="dashboard-header">
      <h1>Dashboard Ejecutivo</h1>
      <div class="header-actions">
        <select v-model="selectedPeriod" @change="refreshData" class="period-selector">
          <option value="month">Este mes</option>
          <option value="quarter">Este trimestre</option>
          <option value="year">Este año</option>
        </select>
      </div>
    </header>

    <!-- KPIs Section -->
    <section class="kpis-section">
      <StatCard 
        title="Cursos Activos" 
        :value="dashboardData.cursosActivos" 
        icon="training"
        :iconBgColor="'#e8f5e8'"
      />
      <StatCard 
        title="Total Participantes" 
        :value="dashboardData.totalParticipantes" 
        icon="users"
        :iconBgColor="'#e3f2fd'"
      />
      <StatCard 
        title="Ingresos del Mes" 
        :value="formatCurrency(dashboardData.ingresosMes)" 
        icon="dollar-sign"
        :iconBgColor="'#fff3e0'"
      />
      <StatCard 
        title="Tasa de Completitud" 
        :value="`${dashboardData.tasaCompletitud}%`" 
        icon="check-circle"
        :iconBgColor="'#f3e5f5'"
      />
    </section>

    
    <section class="charts-section">
      <ChartCard title="Participantes por Rama" class="chart-large">
        <DoughnutChart :chart-data="participantesPorRamaChart" />
      </ChartCard>
      
      <ChartCard title="Ingresos Mensuales" class="chart-large">
        <LineChart :chart-data="ingresosMensualesChart" />
      </ChartCard>
    </section>

    
    <section class="courses-section">
      <div class="section-header">
        <h2>Cursos Activos</h2>
        <BaseButton variant="primary" @click="$router.push('/cursos')">
          Ver todos los cursos
        </BaseButton>
      </div>
      
      <DataTable
        :columns="cursosColumns"
        :items="cursosActivos"
        :pageSize="10"
        :actions="['view', 'edit']"
        @view="viewCurso"
        @edit="editCurso"
      >
        <template #cell(estado)="{ item }">
          <span :class="getEstadoClass(item.estado)">
            {{ item.estado }}
          </span>
        </template>
        <template #cell(participantes)="{ item }">
          <div class="participantes-info">
            <span>{{ item.participantes_actuales }}/{{ item.participantes_max }}</span>
            <div class="progress-bar">
              <div 
                class="progress-fill" 
                :style="{ width: `${(item.participantes_actuales / item.participantes_max) * 100}%` }"
              ></div>
            </div>
          </div>
        </template>
      </DataTable>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useDashboardStore } from '@/stores/dashboard';
import { getCursosActivos, type CursoActivo } from '@/services/executiveDashboard';
import StatCard from '@/components/shared/StatCard.vue';
import ChartCard from '@/components/shared/ChartCard.vue';
import DoughnutChart from '@/components/charts/DoughnutChart.vue';
import LineChart from '@/components/charts/LineChart.vue';
import DataTable from '@/components/shared/DataTable.vue';
import BaseButton from '@/components/shared/BaseButton.vue';

const router = useRouter();
const dashboardStore = useDashboardStore();

const selectedPeriod = ref('month');
const ingresosMensualesChart = computed(() => {
  const data = dashboardStore.executiveMetrics?.ingresosMensuales || [
    { mes: 'Ene', ingresos: 800000 },
    { mes: 'Feb', ingresos: 950000 },
    { mes: 'Mar', ingresos: 1100000 },
    { mes: 'Abr', ingresos: 1250000 },
    { mes: 'May', ingresos: 1180000 },
    { mes: 'Jun', ingresos: 1350000 }
  ];
  
  return {
    labels: data.map(item => item.mes),
    data: data.map(item => item.ingresos)
  };
});

const dashboardData = computed(() => {
  return dashboardStore.executiveMetrics || {
    cursosActivos: 0,
    totalParticipantes: 0,
    ingresosMes: 0,
    tasaCompletitud: 0
  };
});

const cursosActivos = ref<CursoActivo[]>([]);

const cursosColumns = [
  { key: 'nombre', label: 'Nombre del Curso' },
  { key: 'fecha_inicio', label: 'Fecha Inicio' },
  { key: 'fecha_fin', label: 'Fecha Fin' },
  { key: 'estado', label: 'Estado' },
  { key: 'participantes', label: 'Participantes' },
  { key: 'instructor', label: 'Instructor' }
];

const participantesPorRamaChart = computed(() => {
  const statsData = dashboardStore.stats?.participantes_por_rama;

  if (statsData && Array.isArray(statsData) && statsData.length > 0) {
    return {
      labels: statsData.map(item => item.nombre),
      datasets: [{
        backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16', '#FFA500', '#36A2EB'],
        data: statsData.map(item => item.num_participantes)
      }]
    };
  }

  return {
    labels: ['Lobatos', 'Scouts', 'Pioneros', 'Rovers'],
    datasets: [{
      backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
      data: [45, 78, 65, 57]
    }]
  };
});

const formatCurrency = (amount: number): string => {
  return new Intl.NumberFormat('es-CL', {
    style: 'currency',
    currency: 'CLP'
  }).format(amount);
};

const getEstadoClass = (estado: string): string => {
  const classes = {
    'Activo': 'estado-activo',
    'Finalizando': 'estado-finalizando',
    'Completado': 'estado-completado',
    'Cancelado': 'estado-cancelado'
  };
  return classes[estado as keyof typeof classes] || 'estado-default';
};

const viewCurso = (curso: any) => {
  router.push(`/cursos/${curso.id}`);
};

const editCurso = (curso: any) => {
  router.push(`/cursos/${curso.id}/edit`);
};

const refreshData = async () => {
  dashboardStore.fetchStats();
  dashboardStore.fetchExecutiveMetrics(selectedPeriod.value);
  cursosActivos.value = await getCursosActivos();
};



onMounted(async () => {
  dashboardStore.fetchStats();
  dashboardStore.fetchExecutiveMetrics(selectedPeriod.value);
  cursosActivos.value = await getCursosActivos();
});
</script>

<style scoped>
.executive-dashboard {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.dashboard-header h1 {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--color-heading);
}

.period-selector {
  padding: 0.5rem 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: white;
  font-size: 0.9rem;
}

.kpis-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.charts-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.chart-large {
  min-height: 350px;
}



.courses-section {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.section-header h2 {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--color-heading);
}

.estado-activo {
  background: #e8f5e8;
  color: #2e7d32;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
}

.estado-finalizando {
  background: #fff3e0;
  color: #f57c00;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
}

.estado-completado {
  background: #e3f2fd;
  color: #1976d2;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
}

.estado-cancelado {
  background: #ffebee;
  color: #d32f2f;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
}

.participantes-info {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.progress-bar {
  width: 80px;
  height: 6px;
  background: #f0f0f0;
  border-radius: 3px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: #41B883;
  transition: width 0.3s ease;
}

@media (max-width: 768px) {
  .charts-section {
    grid-template-columns: 1fr;
  }
  
  .kpis-section {
    grid-template-columns: 1fr;
  }
  
  .dashboard-header {
    flex-direction: column;
    gap: 1rem;
    align-items: flex-start;
  }
}
</style>