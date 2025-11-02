<template>
  <button :class="cn(buttonVariants({ variant, size }), props.class)" v-bind="$attrs">
    <slot />
  </button>
</template>

<script setup lang="ts">
import { computed, useAttrs, defineOptions} from 'vue'
import { buttonVariants, type ButtonVariants } from './index'
import { cn } from '../../../utils'
const $attrs = useAttrs()
defineOptions({ inheritAttrs: false })

interface Props extends ButtonVariants {
  class?: string
}

const props = defineProps<Props>()
</script>