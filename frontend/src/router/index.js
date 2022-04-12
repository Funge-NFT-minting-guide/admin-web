import { createRouter, createWebHistory } from 'vue-router'

import DefaultLayout from '@/layouts/DefaultLayout'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: DefaultLayout,
    redirect: 'dashboard',
    children: [
      {
        path: 'dashboard',
        name: 'Dashboard',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
          import(/* webpackChunkName: "dashboard" */ '@/views/Dashboard.vue'),
        meta: { requiredAuth: true },
      },
      {
        path: 'login',
        name: 'Login',
        component: () =>
          import(/* webpackChunkName: "login" */ '@/views/Login.vue'),
        meta: { requiredAuth: false },
      },
      {
        path: 'minting',
        name: 'Minting',
        component: () =>
          import(/* webpackChunkName: "minting" */ '@/views/Minting.vue'),
        meta: { requiredAuth: true },
      },
      {
        path: 'test',
        name: 'Test',
        component: () =>
          import(/* webpackChunkName: "test" */ '@/views/Test.vue'),
      },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior() {
    // always scroll to top
    return { top: 0 }
  },
})

router.beforeEach((to, from, next) => {
  let isAuthenticated = localStorage.getItem('isAuthenticated')

  console.log(to.meta)
  if (to.meta.requiredAuth) {
    if (!isAuthenticated && to.name !== 'Login') {
      return next({ name: 'Login' })
    }
  } else {
    if (isAuthenticated && to.name === 'Login') {
      return next('/dashboard')
    }
    if (!isAuthenticated && to.name === 'Login') {
      return next()
    }
  }

  return next()
})

export default router
