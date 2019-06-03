import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import axios from 'axios'
import 'element-ui/lib/theme-chalk/index.css'
import top from '@/components/Top.vue'

Vue.use(ElementUI)

Vue.config.productionTip = false


new Vue({
  router,
  store,
  components: {
    top
  },
  render: h => h(App)
}).$mount('#app')
router.push("/User")

<<<<<<< HEAD
//router.push("/")
=======
router.push("/papers")
>>>>>>> 51653082677f14ee2e8b6329a523d459b8031e82

