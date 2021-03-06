import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Appeal from './views/Appeal.vue'
import Search from './views/Search.vue'
import Login from './views/Login.vue'
import Result from './views/Result.vue'
import User from './views/User.vue'
import Expert from './views/Expert.vue'
import PaperList from "./components/PaperList.vue"
import MessageList from "./components/MessageList.vue"
import Paper from './views/Paper.vue'

//import userinfo from "./components/userinfo.vue"
import UserState from "./components/UserState.vue"
import ExpertList from "./components/ExpertList.vue"
import uploadImg from "./components/UploadImg.vue"

import userinfoR from "./components/UserInfoRemake.vue"
import expertInfo from "./views/Expert.vue"
import userForm from "./components/UserForm.vue"
import expertForm from "./components/ExpertForm.vue"

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'index',
      component: Search
    },
    {
      path: '/search',
      name: 'search',
      component: Search
    },
    {
      path: '/appeal',
      name: 'appeal',
      component: Appeal
    },
    {
      path: '/paper',
      name: 'paper',
      component:Paper
    },
    {
      path: '/expert',
      name: 'expert',
      component: Expert
    },
    {
      path: '/login',
      name: 'login',
      component:Login
    },
    {
      path: '/User',
      name: 'User',
      component: User
    },
    {
      path:'/result',
      name:'result',
      component:Result
    },
    
    {
      path:'/paper',
      name:'paper',
      component:Paper
    }
  ]
})
