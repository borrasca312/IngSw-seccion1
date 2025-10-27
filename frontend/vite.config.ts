/**
 * Configuración de Vite para SGICS Frontend
 * 
 * Vite es el bundler y servidor de desarrollo que:
 * - Compila el código Vue.js + TypeScript
 * - Proporciona hot reload en desarrollo
 * - Optimiza el build para producción
 * - Maneja el proxy hacia el backend Django
 */

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { sentryVitePlugin } from "@sentry/vite-plugin";
import { resolve } from 'node:path'
// Configuración principal de Vite
// Documentación: https://vitejs.dev/config/
export default defineConfig({
  // Plugins de Vite - Vue.js plugin para soporte de SFC (Single File Components)
  plugins: [
    vue(),
    // Sentry plugin para subir sourcemaps (se activa solo si hay token/org/project)
    ...(process.env.SENTRY_AUTH_TOKEN && process.env.SENTRY_ORG && process.env.SENTRY_PROJECT
      ? [
        sentryVitePlugin({
          org: process.env.SENTRY_ORG as string,
          project: process.env.SENTRY_PROJECT as string,
          authToken: process.env.SENTRY_AUTH_TOKEN as string,
          telemetry: false,
          sourcemaps: {
            assets: ["./dist/**"],
          },
        }),
      ]
      : []),
  ],

  // Resolución de módulos
  resolve: {
    alias: {
      // Alias '@' apunta a la carpeta src/ para imports más limpios
      // Uso: import Component from '@/components/Component.vue'
      '@': resolve(__dirname, 'src'),
    },
  },

  // Configuración del servidor de desarrollo
  server: {
    port: 3000,  // Puerto del frontend (debe coincidir con Docker Compose)

    // Proxy para redirigir llamadas API al backend Django
    proxy: {
      '/api': {
        target: 'http://localhost:8000',  // Backend Django
        changeOrigin: true,               // Cambiar el header Origin
        // Ejemplo: http://localhost:3000/api/auth -> http://localhost:8000/api/auth
      },
    },
  },

  // Configuración de build para producción
  build: {
    outDir: 'dist',      // Directorio de salida para archivos compilados
    sourcemap: true,     // Generar sourcemaps para debugging en producción
  },

  // Nota: La configuración de Vitest vive en vitest.config.ts
})
