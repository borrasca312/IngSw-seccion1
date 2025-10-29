<template>
  <MainLayout>
    <div class="pagos-view">
      <div class="chart-container">
        <h2>Ingresos</h2>
        <!-- Placeholder for line chart -->
        <div class="placeholder">Line Chart</div>
      </div>

      <div class="filters">
        <InputText placeholder="Buscar por participante, curso o referencia..." class="search-input" />
        <!-- Add filters for estado and cursos later -->
        <Button label="Exportar" class="p-button-secondary" />
      </div>

      <DataTable :value="pagos" responsiveLayout="scroll">
        <Column field="persona.nombres" header="Participante"></Column>
        <Column field="curso.descripcion" header="Curso"></Column>
        <Column field="curso.cuota_con_almuerzo" header="Monto Total"></Column>
        <Column field="valor" header="Monto Pagado"></Column>
        <Column header="Pendiente">
          <template #body="slotProps">
            {{ slotProps.data.curso.cuota_con_almuerzo - slotProps.data.valor }}
          </template>
        </Column>
        <Column header="Estado">
          <template #body="slotProps">
            <span :class="['status', getStatus(slotProps.data.valor, slotProps.data.curso.cuota_con_almuerzo).toLowerCase()]">{{ getStatus(slotProps.data.valor, slotProps.data.curso.cuota_con_almuerzo) }}</span>
          </template>
        </Column>
        <Column header="Acciones">
          <template #body>
            <Button label="Registrar Pago" class="p-button-link" />
          </template>
        </Column>
      </DataTable>
    </div>
  </MainLayout>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import MainLayout from '@/components/layout/MainLayout.vue';
import { getPagos } from '@/services/pagos';
import type { Pago } from '@/types/pagos';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';

const pagos = ref<Pago[]>([]);

const getStatus = (pagado: number, total: number) => {
  if (pagado >= total) {
    return 'Pagado';
  }
  if (pagado > 0) {
    return 'Parcial';
  }
  return 'Pendiente';
};

onMounted(async () => {
  try {
    pagos.value = await getPagos();
  } catch (error) {
    console.error('Error fetching pagos:', error);
  }
});
</script>

<style scoped>
.chart-container {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  margin-bottom: 20px;
}

.placeholder {
  height: 150px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #9ca3af;
  background-color: #f9fafb;
  border-radius: 8px;
  margin-top: 20px;
}

.filters {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.search-input {
  flex: 1;
}

.status {
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: bold;
}

.status.pagado {
  background-color: #d1fae5;
  color: #065f46;
}

.status.pendiente {
  background-color: #fef3c7;
  color: #92400e;
}

.status.vencido {
  background-color: #fee2e2;
  color: #991b1b;
}

.status.parcial {
  background-color: #dbeafe;
  color: #1e40af;
}
</style>
