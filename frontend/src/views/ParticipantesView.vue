<template>
  <MainLayout>
    <div class="participantes-view">
      <div class="header">
        <h1>Participantes</h1>
        <Button label="+ Nuevo Participante" />
      </div>
      <p>Gestiona todos los participantes.</p>

      <DataTable :value="personas" :loading="loading" responsiveLayout="scroll">
        <template #empty> No se encontraron participantes. </template>
        <template #loading> Cargando participantes... </template>
        <Column field="nombres" header="Nombre"></Column>
        <Column field="email" header="Email"></Column>
        <Column field="telefono" header="Teléfono"></Column>
        <Column header="Acciones">
          <template #body>
            <Button icon="pi pi-pencil" class="p-button-rounded p-button-text" />
            <Button icon="pi pi-trash" class="p-button-rounded p-button-text p-button-danger" />
          </template>
        </Column>
      </DataTable>
    </div>
  </MainLayout>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import MainLayout from '@/components/layout/MainLayout.vue';
import { getPersonas } from '@/services/personas';
import type { Persona } from '@/types/personas';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';

const personas = ref<Persona[]>([]);
const loading = ref(true);

onMounted(async () => {
  try {
    personas.value = await getPersonas();
  } catch (error) {
    console.error('Error fetching personas:', error);
  } finally {
    loading.value = false;
  }
});
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

.participantes-view p {
  color: #6b7280;
  margin-bottom: 20px;
}
</style>
