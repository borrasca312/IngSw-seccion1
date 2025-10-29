<template>
  <MainLayout>
    <div class="cursos-view">
      <div class="header">
        <h1>Cursos</h1>
        <Button label="+ Nuevo Curso" @click="goToNewCurso" />
      </div>
      <p>Gestiona todos los cursos de formación Scout</p>

      <div v-if="cursoStore.error" class="error-message">{{ cursoStore.error }}</div>
      <DataTable :value="cursoStore.cursos" :loading="cursoStore.isLoading" responsiveLayout="scroll">
        <template #empty> No se encontraron cursos. </template>
        <template #loading> Cargando cursos... </template>
        <Column field="codigo" header="Código"></Column>
        <Column field="descripcion" header="Nombre del Curso"></Column>
        <Column field="tipo_curso.descripcion" header="Categoría"></Column>
        <Column field="modalidad" header="Modalidad"></Column>
        <Column header="Fechas">
          <template #body="slotProps">
            {{ formatFechas(slotProps.data.fechas) }}
          </template>
        </Column>
        <Column field="total_participantes" header="Participantes"></Column>
        <Column field="cuota_con_almuerzo" header="Precio (Bs.)"></Column>
        <Column field="estado" header="Estado">
          <template #body="slotProps">
            <Tag :value="getEstadoText(slotProps.data.estado)" :severity="getEstadoSeverity(slotProps.data.estado)" />
          </template>
        </Column>
        <Column header="Acciones">
          <template #body="slotProps">
            <Button icon="pi pi-pencil" class="p-button-rounded p-button-text" @click="editCurso(slotProps.data.id)" />
            <Button icon="pi pi-trash" class="p-button-rounded p-button-text p-button-danger" @click="deleteCurso(slotProps.data.id)" />
          </template>
        </Column>
      </DataTable>
    </div>
  </MainLayout>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useCursoStore } from '@/stores/curso';
import MainLayout from '@/components/layout/MainLayout.vue';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';
import Tag from 'primevue/tag';

const router = useRouter();
const cursoStore = useCursoStore();

onMounted(() => {
  cursoStore.fetchCursos();
});

const goToNewCurso = () => {
  router.push({ name: 'Cursos.New' });
};

const editCurso = (id: number) => {
  router.push({ name: 'Cursos.Edit', params: { id } });
};

const deleteCurso = (id: number) => {
  // Implement delete logic, possibly with a confirmation dialog
  console.log('Delete curso with id:', id);
};

const formatFechas = (fechas: { fecha_inicio: string }[]) => {
  if (!fechas || fechas.length === 0 || !fechas[0]) return 'N/A';
  const primeraFecha = new Date(fechas[0].fecha_inicio).toLocaleDateString();
  return `${primeraFecha}...`;
};

const getEstadoText = (estado: number) => {
  const estados: { [key: number]: string } = {
    0: 'Pendiente',
    1: 'Vigente',
    2: 'Anulado',
    3: 'Finalizado',
  };
  return estados[estado] || 'Desconocido';
};

const getEstadoSeverity = (estado: number) => {
  const severities: { [key: number]: string } = {
    0: 'warning',
    1: 'success',
    2: 'danger',
    3: 'info',
  };
  return severities[estado] || 'secondary';
};
</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 5px;
}

h1 {
  font-size: 24px;
  font-weight: bold;
}

.cursos-view p {
  color: #6b7280;
  margin-bottom: 20px;
}

.status {
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: bold;
}

.status.activo {
  background-color: #d1fae5;
  color: #065f46;
}

.status.próximo {
  background-color: #dbeafe;
  color: #1e40af;
}

.status.completado {
  background-color: #e5e7eb;
  color: #374151;
}

.status.borrador {
  background-color: #fef3c7;
  color: #92400e;
}
</style>
