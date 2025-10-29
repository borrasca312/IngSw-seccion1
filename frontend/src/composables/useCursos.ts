import { ref, onMounted, computed } from 'vue';
import { getCursos } from '@/services/cursos';
import { getTiposCurso } from '@/services/maestros';
import type { Curso } from '@/types/cursos';
import type { TipoCurso } from '@/types/maestros';

export function useCursos() {
  const cursos = ref<Curso[]>([]);
  const tiposCurso = ref<TipoCurso[]>([]);
  const loading = ref(true);
  const error = ref<string | null>(null);

  const tiposCursoMap = computed(() => {
    return tiposCurso.value.reduce((acc, tipo) => {
      acc[tipo.id] = tipo.descripcion;
      return acc;
    }, {} as Record<number, string>);
  });

  const getCategoryName = (id: number) => {
    return tiposCursoMap.value[id] || 'Desconocido';
  };

  onMounted(async () => {
    try {
      [cursos.value, tiposCurso.value] = await Promise.all([
        getCursos(),
        getTiposCurso(),
      ]);
    } catch (err) {
      error.value = 'Error al cargar los datos.';
      console.error(err);
    } finally {
      loading.value = false;
    }
  });

  return {
    cursos,
    loading,
    error,
    getCategoryName,
  };
}
