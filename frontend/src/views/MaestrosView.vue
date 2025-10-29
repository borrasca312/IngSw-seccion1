<template>
  <div>
    <h1>Maestros</h1>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div class="card p-6">
        <h3 class="text-lg font-semibold text-slate-900 mb-4">Regiones</h3>
        <ul>
          <li v-for="region in regiones" :key="region.id">{{ region.descripcion }}</li>
        </ul>
      </div>
      <div class="card p-6">
        <h3 class="text-lg font-semibold text-slate-900 mb-4">Provincias</h3>
        <ul>
          <li v-for="provincia in provincias" :key="provincia.id">{{ provincia.descripcion }}</li>
        </ul>
      </div>
      <div class="card p-6">
        <h3 class="text-lg font-semibold text-slate-900 mb-4">Comunas</h3>
        <ul>
          <li v-for="comuna in comunas" :key="comuna.id">{{ comuna.descripcion }}</li>
        </ul>
      </div>
      <div class="card p-6">
        <h3 class="text-lg font-semibold text-slate-900 mb-4">Cargos</h3>
        <ul>
          <li v-for="cargo in cargos" :key="cargo.id">{{ cargo.descripcion }}</li>
        </ul>
      </div>
      <div class="card p-6">
        <h3 class="text-lg font-semibold text-slate-900 mb-4">Tipos de Curso</h3>
        <ul>
          <li v-for="tipo in tiposCurso" :key="tipo.id">{{ tipo.descripcion }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { getRegiones, getProvincias, getComunas, getCargos, getTiposCurso } from '../services/maestros';
import type { Region, Provincia, Comuna, Cargo, TipoCurso } from '../types/maestros';

const regiones = ref<Region[]>([]);
const provincias = ref<Provincia[]>([]);
const comunas = ref<Comuna[]>([]);
const cargos = ref<Cargo[]>([]);
const tiposCurso = ref<TipoCurso[]>([]);

onMounted(async () => {
  regiones.value = await getRegiones();
  provincias.value = await getProvincias();
  comunas.value = await getComunas();
  cargos.value = await getCargos();
  tiposCurso.value = await getTiposCurso();
});
</script>
