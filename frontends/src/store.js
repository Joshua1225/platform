import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLog: false,
  },
  mutations: {
    setOnline() {
      this.state.isLog = ture;
    }, setOffline() {
      this.state.isLog = false;
    }
  },
  actions: {

  }
})
