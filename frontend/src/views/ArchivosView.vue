<template>
  <div>
    <h1>Archivos</h1>
    <div class="flex justify-between mb-4">
      <input type="text" placeholder="Buscar por descripción" class="input-base" />
      <button @click="createArchivo" class="btn-primary">Crear Archivo</button>
    </div>
    <table>
      <caption>Lista de Archivos</caption>
      <thead>
        <tr>
          <th>ID</th>
          <th>Descripción</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="archivo in archivos" :key="archivo.id">
          <td>{{ archivo.id }}</td>
          <td>{{ archivo.descripcion }}</td>
          <td>
            <button @click="editArchivo(archivo)">Editar</button>
            <button @click="deleteArchivo(archivo)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import type { Archivo } from '../types/archivos';
import { getArchivos, deleteArchivo as deleteArchivoApi } from '../services/archivos';

const router = useRouter();
const archivos = ref<Archivo[]>([]);

const fetchArchivos = async () => {
  archivos.value = await getArchivos();
};

const createArchivo = () => {
  router.push({ name: 'Archivos.New' });
};

const editArchivo = (archivo: Archivo) => {
  router.push({ name: 'Archivos.Edit', params: { id: archivo.id } });
};

const deleteArchivo = async (archivo: Archivo) => {
  await deleteArchivoApi(archivo.id);
  fetchArchivos();
};

onMounted(() => {
  fetchArchivos();
});
</script>
