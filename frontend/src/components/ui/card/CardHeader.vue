<template>
  <div :class="cn('flex flex-col space-y-1.5 p-6', props.class)" v-bind="$attrs">
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