<template>
  <div class="mis-preinscripciones-view">
    <Card>
      <CardHeader>
        <CardTitle>Mis Preinscripciones</CardTitle>
        <CardDescription>
          Aquí puedes ver el estado de tus preinscripciones y descargar tu QR de acreditación.
        </CardDescription>
      </CardHeader>
      
      <CardContent>
        <div v-if="isLoading" class="loading-placeholder">
          Cargando preinscripciones...
        </div>
        
        <div v-else-if="preinscripciones.length === 0" class="empty-state">
          No tienes preinscripciones activas.
        </div>

        <div v-else class="preinscripcion-list">
          <div v-for="pre in preinscripciones" :key="pre.id" class="preinscripcion-item">
            <div class="info">
              <span class="curso-titulo">{{ pre.cursoNombre }}</span>
              <span class="estado" :class="pre.estado">{{ pre.estado }}</span>
            </div>
            
            <Button 
              variant="primary" 
              @click="descargarQR(pre.id)" 
              :disabled="pre.estado !== 'CONFIRMADA'">
              Descargar QR
            </Button>
          </div>
        </div>
      </CardContent>
    </Card>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

// --- Importamos los componentes del Design System que arreglamos ---
// OJO: Si la importación de 'Button' da error, cámbiala por la ruta completa
import Button from '@/components/ui/button/Button.vue'
import { 
  Card, 
  CardHeader, 
  CardTitle, 
  CardDescription, 
  CardContent 
} from '@/components/ui/card'

// --- Lógica de la página (simulada por ahora) ---

const isLoading = ref(true)
const preinscripciones = ref<any[]>([]) // Idealmente, se crearía un tipo para esto

// Simulación de datos
const simularCarga = () => {
  isLoading.value = true
  setTimeout(() => {
    preinscripciones.value = [
      { id: 1, cursoNombre: 'Curso de Liderazgo Básico', estado: 'CONFIRMADA' },
      { id: 2, cursoNombre: 'Taller de Primeros Auxilios', estado: 'EN_VALIDACION' },
      { id: 3, cursoNombre: 'Curso de Fogata Avanzada', estado: 'RECHAZADA' },
    ]
    isLoading.value = false
  }, 1500)
}

// Al cargar la página, se buscan los datos
onMounted(() => {
  // Aquí iría la llamada real a la API, por ejemplo:
  // preinscripciones.value = await preinscripcionesStore.fetchMisPreinscripciones()
  simularCarga()
})

const descargarQR = (preinscripcionId: number) => {
  alert(`Descargando QR para la preinscripción ID: ${preinscripcionId}. ¡Esta función debe ser implementada!`)
  // Aquí iría la lógica para llamar a la API que genera el QR
}
</script>

<style scoped>
.mis-preinscripciones-view {
  padding: 2rem;
  max-width: 900px;
  margin: 0 auto;
}

.preinscripcion-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border-bottom: 1px solid #dee2e6; /* Usar variable CSS si la definimos */
}

.preinscripcion-item:last-child {
  border-bottom: none;
}

.info {
  display: flex;
  flex-direction: column;
}

.curso-titulo {
  font-weight: 600;
}

.estado {
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0.2rem 0.5rem;
  border-radius: 99px;
  margin-top: 0.25rem;
  text-align: center;
  display: inline-block;
  width: fit-content;
}

/* Estilos de ejemplo para los estados */
.estado.CONFIRMADA {
  color: #155724;
  background-color: #d4edda;
}
.estado.EN_VALIDACION {
  color: #0c5460;
  background-color: #d1ecf1;
}
.estado.RECHAZADA {
  color: #721c24;
  background-color: #f8d7da;
}
</style>