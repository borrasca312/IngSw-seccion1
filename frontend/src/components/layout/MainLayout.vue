<template>
  <div class="main-layout">
    <aside class="sidebar">
      <div class="logo">
        <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M20 0L40 20L20 40L0 20L20 0Z" fill="#4F46E5"/>
          <path d="M20 5L35 20L20 35L5 20L20 5Z" stroke="white" stroke-width="2"/>
          <path d="M10 20L20 30L30 20L20 10L10 20Z" stroke="white" stroke-width="2"/>
        </svg>
        <span>GICS</span>
      </div>
      <nav>
        <router-link to="/dashboard">Dashboard</router-link>
        <router-link to="/cursos">Cursos</router-link>
        <router-link to="/preinscripciones">Preinscripciones</router-link>
        <router-link to="/participantes">Participantes</router-link>
        <router-link to="/pagos">Pagos</router-link>
      </nav>
      <div class="dark-mode-toggle">
        <span>Modo Oscuro</span>
      </div>
    </aside>
    <main class="main-content">
      <header>
        <div class="user-info">
          <span>Admin Scout</span>
          <small>admin@scouts.org</small>
        </div>
        <button @click="logout">Salir</button>
      </header>
      <div class="content">
        <slot />
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();

const logout = () => {
  localStorage.removeItem('access_token');
  router.push({ name: 'Login' });
};
</script>

<style scoped>
.main-layout {
  display: flex;
  height: 100vh;
}

.sidebar {
  width: 250px;
  background-color: #1f2937;
  color: white;
  display: flex;
  flex-direction: column;
  padding: 20px;
}

.logo {
  display: flex;
  align-items: center;
  margin-bottom: 40px;
}

.logo span {
  font-size: 24px;
  font-weight: bold;
  margin-left: 10px;
}

nav {
  display: flex;
  flex-direction: column;
}

nav a {
  color: white;
  text-decoration: none;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 10px;
}

nav a.router-link-exact-active {
  background-color: #4f46e5;
}

.dark-mode-toggle {
  margin-top: auto;
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

header {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  padding: 20px;
  background-color: white;
  border-bottom: 1px solid #e5e7eb;
}

.user-info {
  text-align: right;
  margin-right: 20px;
}

.user-info span {
  font-weight: bold;
}

.user-info small {
  color: #6b7280;
}

header button {
  background: none;
  border: 1px solid #d1d5db;
  padding: 5px 10px;
  border-radius: 4px;
  cursor: pointer;
}

.content {
  padding: 20px;
  background-color: #f3f4f6;
  flex: 1;
  overflow-y: auto;
}
</style>
