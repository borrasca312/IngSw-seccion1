<template>
  <input
    :class="cn(
      'flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50',
      props.class
    )"
    v-bind="$attrs"
  />
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