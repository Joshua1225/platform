import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLog: false,
    userName:"",
    userAvator:""
  },
  mutations: {
    setOnline() {
      this.state.isLog = true;
    }, setOffline() {
      this.state.isLog = false;
    }
  },
  actions: {

  }
})
