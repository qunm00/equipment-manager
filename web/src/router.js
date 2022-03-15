import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from './components/Dashboard.vue'
import Equipment from './components/Equipment.vue'
import Employees from './components/Employees.vue'

const routes = [
    { path: '/', component: Dashboard },
    { path: '/equipment', component: Equipment },
    { path: '/employees', component: Employees }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router

