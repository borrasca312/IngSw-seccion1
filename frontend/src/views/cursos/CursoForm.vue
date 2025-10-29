<template>
  <MainLayout>
    <div class="curso-form">
      <h1>{{ isEditMode ? 'Editar' : 'Crear' }} Curso</h1>
      <form @submit.prevent="saveCurso">
        <div class="p-fluid grid">
          <div class="field col-12 md:col-6">
            <label for="descripcion">Nombre del Curso</label>
            <InputText id="descripcion" v-model="curso.descripcion" />
          </div>
          <div class="field col-12 md:col-6">
            <label for="codigo">Código</label>
            <InputText id="codigo" v-model="curso.codigo" />
          </div>
          <div class="field col-12 md:col-6">
            <label for="tipo_curso">Tipo de Curso</label>
            <Dropdown id="tipo_curso" v-model="selectedTipoCurso" :options="tiposCurso" optionLabel="descripcion" optionValue="id" placeholder="Seleccione un tipo" />
          </div>
          <div class="field col-12 md:col-6">
            <label for="responsable">Responsable</label>
            <Dropdown id="responsable" v-model="selectedResponsable" :options="personas" optionLabel="nombres" optionValue="id" placeholder="Seleccione un responsable" />
          </div>
          <div class="field col-12 md:col-6">
            <label for="cargo_responsable">Cargo del Responsable</label>
            <Dropdown id="cargo_responsable" v-model="selectedCargo" :options="cargos" optionLabel="descripcion" optionValue="id" placeholder="Seleccione un cargo" />
          </div>
          <div class="field col-12 md:col-6">
            <label for="comuna">Comuna</label>
            <Dropdown id="comuna" v-model="selectedComuna" :options="comunas" optionLabel="descripcion" optionValue="id" placeholder="Seleccione una comuna" />
          </div>
          <div class="field col-12 md:col-6">
            <label for="lugar">Lugar</label>
            <InputText id="lugar" v-model="curso.lugar" />
          </div>
          <div class="field col-12 md:col-6">
            <label for="fecha_solicitud">Fecha de Solicitud</label>
            <Calendar id="fecha_solicitud" v-model="curso.fecha_solicitud" dateFormat="yy-mm-dd" />
          </div>
          <div class="field col-12 md:col-4">
            <label for="cuota_con_almuerzo">Cuota con Almuerzo</label>
            <InputNumber id="cuota_con_almuerzo" v-model="curso.cuota_con_almuerzo" mode="currency" currency="CLP" locale="es-CL" />
          </div>
          <div class="field col-12 md:col-4">
            <label for="cuota_sin_almuerzo">Cuota sin Almuerzo</label>
            <InputNumber id="cuota_sin_almuerzo" v-model="curso.cuota_sin_almuerzo" mode="currency" currency="CLP" locale="es-CL" />
          </div>
          <div class="field col-12 md:col-4">
            <label for="modalidad">Modalidad</label>
            <InputText id="modalidad" v-model="curso.modalidad" />
          </div>
        </div>
        <Button type="submit" label="Guardar" class="mt-2" />
      </form>
    </div>
  </MainLayout>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useCursoStore } from '@/stores/curso';
import { maestroService } from '@/services/maestroService';
import MainLayout from '@/components/layout/MainLayout.vue';
import InputText from 'primevue/inputtext';
import Dropdown from 'primevue/dropdown';
import Calendar from 'primevue/calendar';
import InputNumber from 'primevue/inputnumber';
import Button from 'primevue/button';
import type { Curso } from '@/types/curso';

const router = useRouter();
const route = useRoute();
const cursoStore = useCursoStore();

const curso = ref<Partial<Curso>>({
  descripcion: '',
  codigo: '',
  lugar: '',
  fecha_solicitud: '',
  cuota_con_almuerzo: 0,
  cuota_sin_almuerzo: 0,
  modalidad: 0,
});
const isEditMode = computed(() => !!route.params.id);

const tiposCurso = ref<any[]>([]);
const personas = ref<any[]>([]);
const cargos = ref<any[]>([]);
const comunas = ref<any[]>([]);

const selectedTipoCurso = ref<number | null>(null);
const selectedResponsable = ref<number | null>(null);
const selectedCargo = ref<number | null>(null);
const selectedComuna = ref<number | null>(null);

watch(selectedTipoCurso, (val) => (curso.value.tipo_curso as any) = val);
watch(selectedResponsable, (val) => (curso.value.responsable as any) = val);
watch(selectedCargo, (val) => (curso.value.cargo_responsable as any) = val);
watch(selectedComuna, (val) => (curso.value.lugar_comuna as any) = val);

const loadDropdownData = async () => {
  tiposCurso.value = await maestroService.getTiposCurso();
  personas.value = await maestroService.getPersonas();
  cargos.value = await maestroService.getCargos();
  comunas.value = await maestroService.getComunas();
};

const saveCurso = async () => {
  if (isEditMode.value) {
    await cursoStore.updateCurso(curso.value.id!, curso.value);
  } else {
    await cursoStore.createCurso(curso.value);
  }
  router.push({ name: 'Cursos' });
};

onMounted(async () => {
  await loadDropdownData();
  if (isEditMode.value) {
    const cursoId = Number(route.params.id);
    const fetchedCurso = await cursoStore.fetchCursoById(cursoId);
    if (fetchedCurso) {
      curso.value = fetchedCurso;
      selectedTipoCurso.value = fetchedCurso.tipo_curso?.id || null;
      selectedResponsable.value = fetchedCurso.responsable?.id || null;
      selectedCargo.value = fetchedCurso.cargo_responsable?.id || null;
      selectedComuna.value = fetchedCurso.lugar_comuna?.id || null;
    }
  }
});
</script>

<style scoped>
.curso-form {
  max-width: 800px;
  margin: 0 auto;
}
</style>
