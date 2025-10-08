import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue'), // You'll need to create this view
  },
  // Add other routes here
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
