<template>
  <div class="card">
    <h3>{{ title }}</h3>
    <p class="stat">{{ stat }}</p>
    <small>{{ change }}</small>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  title: string;
  stat: string | number;
  change: string;
}>();
</script>

<style scoped>
.card {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card h3 {
  font-size: 14px;
  color: #6b7280;
}

.card .stat {
  font-size: 32px;
  font-weight: bold;
  margin: 10px 0;
}

.card small {
  color: #10b981;
}
</style>
