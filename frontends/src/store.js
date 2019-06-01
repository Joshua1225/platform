import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLog: false
  },
  mutations: {
    changeisLog(){
      this.state.isLog=!this.state.isLog
    }
  },
  actions: {

  }
})
