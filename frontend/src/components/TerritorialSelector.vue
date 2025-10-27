<template>
  <div class="territorial-selector-container">
    
    <div class="selector-group">
      <label for="region">Región</label>
      <select id="region" v-model="selectedRegion" @change="onRegionChange">
        <option disabled value="">Seleccione una región</option>
        <option v-for="region in regions" :key="region.codigo" :value="region.codigo">
          {{ region.nombre }}
        </option>
      </select>
    </div>

    <div class="selector-group">
      <label for="zona">Zona</label>
      <select id="zona" v-model="selectedZona" @change="onZonaChange" :disabled="zonas.length === 0">
        <option disabled value="">Seleccione una zona</option>
        <option v-for="zona in zonas" :key="zona.codigo" :value="zona.codigo">
          {{ zona.nombre }}
        </option>
      </select>
    </div>

    <div class="selector-group">
      <label for="distrito">Distrito</label>
      <select id="distrito" v-model="selectedDistrito" @change="onDistritoChange" :disabled="distritos.length === 0">
        <option disabled value="">Seleccione un distrito</option>
        <option v-for="distrito in distritos" :key="distrito.codigo" :value="distrito.codigo">
          {{ distrito.nombre }}
        </option>
      </select>
    </div>

    <div class="selector-group">
      <label for="grupo">Grupo</label>
      <select id="grupo" v-model="selectedGrupo" :disabled="grupos.length === 0">
        <option disabled value="">Seleccione un grupo</option>
        <option v-for="grupo in grupos" :key="grupo.codigo" :value="grupo.codigo">
          {{ grupo.nombre }}
        </option>
      </select>
    </div>

  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { catalogService } from '@/services/catalog'
import type { Region, Zona, Distrito, GrupoScout } from '@/services/catalog'

// --- 1. Variables para las listas de opciones ---
const regions = ref<Region[]>([])
const zonas = ref<Zona[]>([])
const distritos = ref<Distrito[]>([])
const grupos = ref<GrupoScout[]>([])

// --- 2. Variables para guardar lo que el usuario selecciona ---
const selectedRegion = ref('')
const selectedZona = ref('')
const selectedDistrito = ref('')
const selectedGrupo = ref('')

// --- 3. Lógica de "Lazy Loading" (Carga perezosa) ---

// Al cargar el componente, buscar las regiones
onMounted(async () => {
  regions.value = await catalogService.getRegiones()
})

// Cuando el usuario cambia la REGIÓN...
const onRegionChange = async () => {
  // Resetear los valores hijos
  zonas.value = []
  selectedZona.value = ''
  distritos.value = []
  selectedDistrito.value = ''
  grupos.value = []
  selectedGrupo.value = ''

  // Buscar las zonas de esta región
  if (selectedRegion.value) {
    zonas.value = await catalogService.getZonas(selectedRegion.value)
  }
}

// Cuando el usuario cambia la ZONA...
const onZonaChange = async () => {
  // Resetear los valores hijos
  distritos.value = []
  selectedDistrito.value = ''
  grupos.value = []
  selectedGrupo.value = ''

  // Buscar los distritos de esta zona
  if (selectedZona.value) {
    distritos.value = await catalogService.getDistritos(selectedZona.value)
  }
}

// Cuando el usuario cambia el DISTRITO...
const onDistritoChange = async () => {
  // Resetear los valores hijos
  grupos.value = []
  selectedGrupo.value = ''
  
  // Buscar los grupos de este distrito
  if (selectedDistrito.value) {
    grupos.value = await catalogService.getGrupos(selectedDistrito.value)
  }
}
</script>

<style scoped>
/* Estilos básicos para que se vea ordenado */
.territorial-selector-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.selector-group {
  display: flex;
  flex-direction: column;
}
select {
  padding: 0.5rem;
  border-radius: 4px;
  border: 1px solid #ccc;
}
select:disabled {
  background-color: #f4f4f4;
}
</style>