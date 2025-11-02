<template>
  <div :class="cn('rounded-lg border bg-card text-card-foreground shadow-sm', props.class)" v-bind="$attrs">
    <slot />
  </div>
</template>

<script setup lang="ts">
import { cn } from '../../../utils' 

// 1. Definimos la interfaz de Props, incluyendo "class"
interface Props {
  class?: string
}

// 2. Definimos las props usando la interfaz
const props = defineProps<Props>()
</script>