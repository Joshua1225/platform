import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Appeal from './views/Appeal.vue'
import Search from './views/Search.vue'
import Login from './views/Login.vue'
import Result from './views/Result.vue'
import PaperList from "./components/PaperList.vue"
import Papers from './views/Papers.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    
    {
      path: '/',
      name: 'appeal',
      component: PaperList
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/search',
      name: 'search',
      component:Search
    },
    {
      path: '/login',
      name: 'login',
      component:Login
    },
    {
      path:'/result',
      name:'result',
      component:Result
    },
    
    {
      path:'/papers',
      name:'papers',
      component:Papers
    }
  ]
})
