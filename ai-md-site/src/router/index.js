import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'
import Try_it from '../views/Try_It.vue'
import AboutView from '../views/AboutView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: AboutView
    },
    {
      path: '/try-it',
      name: 'try_it',
      component: Try_it
    }

  ]
})

export default router
