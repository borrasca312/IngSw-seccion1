<template>
  <p :class="cn('text-sm text-muted-foreground', props.class)" v-bind="$attrs">
    <slot />
  </p>
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