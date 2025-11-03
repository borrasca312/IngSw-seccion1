<template>
  <div v-if="curso">
    <h1>{{ curso.descripcion }}</h1>
    <p>Código: {{ curso.codigo }}</p>
    <p>Responsable: {{ curso.responsable }}</p>
    <p>Estado: {{ curso.estado }}</p>
    <!-- Add other fields as needed -->
  </div>
  <div v-else>
    <p>Cargando...</p>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import type { Curso } from '../../types/cursos';
import { getCursos } from '../../services/cursos';

const route = useRoute();
const curso = ref<Curso | null>(null);

onMounted(async () => {
  const id = route.params.id;
  if (id) {
    // This is not ideal, we should have a getCursoById function
    const cursos = await getCursos();
    curso.value = cursos.find((c) => c.id === Number(id)) || null;
  }
});
</script>
