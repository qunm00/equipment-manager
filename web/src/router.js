import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from './views/Dashboard.vue'

const routes = [
  { 
    path: '/',
    name: 'Dashboard',
    component: Dashboard 
  },
  { 
    path: '/equipment',
    name: 'Equipment',
    component: () => import('./views/Equipment.vue') 
  },
  { 
    path: '/employees',
    name: 'Employees',
    component: () => import('./views/employees/Employees.vue')
  }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router

