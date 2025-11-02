<template>
  <div :class="cn('flex items-center p-6 pt-0', props.class)" v-bind="$attrs">
    <slot />
  </div>
</template>

<script setup lang="ts">
import { cn } from '../../../utils' // Ruta corregida

// 1. Definimos la interfaz de Props
interface Props {
  class?: string
}

// 2. Definimos las props
const props = defineProps<Props>()
</script>