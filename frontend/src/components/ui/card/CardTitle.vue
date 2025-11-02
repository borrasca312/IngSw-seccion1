<template>
  <h3 :class="cn('text-2xl font-semibold leading-none tracking-tight', props.class)" v-bind="$attrs">
    <slot />
  </h3>
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