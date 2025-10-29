<template>
  <div class="p-4 border rounded-lg">
    <h3 class="text-lg font-semibold">{{ curso.descripcion }}</h3>
    <p class="text-sm text-gray-500">{{ curso.codigo }}</p>
  </div>
</template>

<script setup lang="ts">
import type { Curso } from '@/types/cursos';

defineProps<{
  curso: Curso;
}>();
</script>
