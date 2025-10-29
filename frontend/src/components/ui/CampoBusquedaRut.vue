<template>
  <div>
    <label for="rut" class="block text-sm font-medium text-gray-700">RUT</label>
    <div class="mt-1">
      <input type="text" id="rut" v-model="rut" @input="search" class="input-base w-full" />
    </div>
    <div v-if="results.length > 0" class="mt-2">
      <ul>
        <li v-for="result in results" :key="result.id">
          {{ result.nombres }} {{ result.apellido_paterno }} {{ result.apellido_materno }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { searchPersonByRut } from '@/services/personas';
import type { Persona } from '@/types/personas';

const rut = ref('');
const results = ref<Persona[]>([]);

const search = async () => {
  if (rut.value.length > 2) {
    results.value = await searchPersonByRut(rut.value);
  } else {
    results.value = [];
  }
};
</script>
