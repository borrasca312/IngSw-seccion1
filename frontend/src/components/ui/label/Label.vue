<template>
  <label
    :class="cn(
      'text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70',
      props.class
    )"
    v-bind="$attrs"
  >
    <slot />
  </label>
</template>

<script setup lang="ts">
import { cn } from '../../../utils' // Ruta corregida

// 1. Definimos la interfaz de Props, incluyendo "class"
interface Props {
  class?: string
}

// 2. Definimos las props
const props = defineProps<Props>()
</script>