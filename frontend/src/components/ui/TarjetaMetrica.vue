<template>
  <div class="p-6 bg-white rounded-lg shadow">
    <h3 class="text-sm font-medium text-slate-600">{{ title }}</h3>
    <p class="text-2xl font-semibold text-slate-900 mt-2">{{ value }}</p>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  title: string;
  value: string;
}>();
</script>
