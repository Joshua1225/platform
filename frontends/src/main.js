import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import axios from 'axios'
import 'element-ui/lib/theme-chalk/index.css'
import top from '@/components/Top.vue'
//词云
import echarts from 'echarts'
Vue.prototype.$echarts = echarts
require('echarts-wordcloud')

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

router.push("/Login")

