import { defineStore } from 'pinia';
import { ref } from 'vue';
import { cursoService } from '@/services/cursoService';
import type { Curso } from '@/types/curso';

export const useCursoStore = defineStore('curso', () => {
  const cursos = ref<Curso[]>([]);
  const isLoading = ref(false);
  const error = ref<string | null>(null);

  const fetchCursos = async () => {
    isLoading.value = true;
    error.value = null;
    try {
      cursos.value = await cursoService.getAll();
    } catch (err) {
      error.value = 'Error al cargar los cursos.';
      console.error(err);
    } finally {
      isLoading.value = false;
    }
  };

  const fetchCursoById = async (id: number) => {
    isLoading.value = true;
    error.value = null;
    try {
      return await cursoService.getById(id);
    } catch (err) {
      error.value = 'Error al cargar el curso.';
      console.error(err);
    } finally {
      isLoading.value = false;
    }
  };

  const createCurso = async (curso: Partial<Curso>) => {
    isLoading.value = true;
    error.value = null;
    try {
      const nuevoCurso = await cursoService.create(curso);
      cursos.value.push(nuevoCurso);
    } catch (err) {
      error.value = 'Error al crear el curso.';
      console.error(err);
    } finally {
      isLoading.value = false;
    }
  };

  const updateCurso = async (id: number, curso: Partial<Curso>) => {
    isLoading.value = true;
    error.value = null;
    try {
      const cursoActualizado = await cursoService.update(id, curso);
      const index = cursos.value.findIndex(c => c.id === id);
      if (index !== -1) {
        cursos.value[index] = cursoActualizado;
      }
    } catch (err) {
      error.value = 'Error al actualizar el curso.';
      console.error(err);
    } finally {
      isLoading.value = false;
    }
  };

  const deleteCurso = async (id: number) => {
    isLoading.value = true;
    error.value = null;
    try {
      await cursoService.delete(id);
      cursos.value = cursos.value.filter(c => c.id !== id);
    } catch (err) {
      error.value = 'Error al eliminar el curso.';
      console.error(err);
    } finally {
      isLoading.value = false;
    }
  };

  return {
    cursos,
    isLoading,
    error,
    fetchCursos,
    fetchCursoById,
    createCurso,
    updateCurso,
    deleteCurso,
  };
});
