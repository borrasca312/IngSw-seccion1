<template>
  <div class="line-chart">
    <svg :width="width" :height="height" class="chart-svg">
      <!-- Líneas de cuadrícula -->
      <g class="grid">
        <line 
          v-for="i in 5" 
          :key="`h-${i}`"
          :x1="padding" 
          :y1="padding + (i - 1) * ((height - 2 * padding) / 4)"
          :x2="width - padding" 
          :y2="padding + (i - 1) * ((height - 2 * padding) / 4)"
          stroke="#f0f0f0" 
          stroke-width="1"
        />
      </g>
      
      <!-- Línea de datos -->
      <polyline
        :points="linePoints"
        fill="none"
        stroke="#41B883"
        stroke-width="3"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
      
      <!-- Puntos de datos -->
      <circle
        v-for="(point, index) in dataPoints"
        :key="index"
        :cx="point.x"
        :cy="point.y"
        r="4"
        fill="#41B883"
        class="data-point"
      />
      
      <!-- Etiquetas -->
      <g class="labels">
        <text
          v-for="(label, index) in chartData.labels"
          :key="index"
          :x="padding + (index * (width - 2 * padding) / (chartData.labels.length - 1))"
          :y="height - 10"
          text-anchor="middle"
          font-size="12"
          fill="#666"
        >
          {{ label }}
        </text>
      </g>
    </svg>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';

interface ChartData {
  labels: string[];
  data: number[];
}

const props = defineProps<{
  chartData: ChartData;
  width?: number;
  height?: number;
}>();

const width = props.width || 400;
const height = props.height || 250;
const padding = 40;

const maxValue = computed(() => Math.max(...props.chartData.data));
const minValue = computed(() => Math.min(...props.chartData.data));

const dataPoints = computed(() => {
  return props.chartData.data.map((value, index) => {
    const x = padding + (index * (width - 2 * padding) / (props.chartData.data.length - 1));
    const y = height - padding - ((value - minValue.value) / (maxValue.value - minValue.value)) * (height - 2 * padding);
    return { x, y };
  });
});

const linePoints = computed(() => {
  return dataPoints.value.map(point => `${point.x},${point.y}`).join(' ');
});
</script>

<style scoped>
.line-chart {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.chart-svg {
  max-width: 100%;
  max-height: 100%;
}

.data-point {
  cursor: pointer;
  transition: r 0.2s ease;
}

.data-point:hover {
  r: 6;
}
</style>