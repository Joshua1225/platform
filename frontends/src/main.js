import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import bottom from '@/components/Bottom.vue'
import top from '@/components/Top.vue'


Vue.use(ElementUI)

Vue.config.productionTip = false


new Vue({
  router,
  store,
  components: {
    bottom,top
  },
  render: h => h(App)
}).$mount('#app')
router.push("/Search")