import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import head from '@/components/Top.vue'

Vue.use(ElementUI)

Vue.config.productionTip = false


new Vue({
  router,
  store,
  components: {
    head
  },
  render: h => h(App)
}).$mount('#app')
<<<<<<< HEAD
//router.push("/Search")
=======
router.push("/")
>>>>>>> c5604aba90720a11de80dd28efce46943a2e2d0b
