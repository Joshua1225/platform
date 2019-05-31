<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-view/>
    <el-button v-on:click='transfer' type="danger" >危险按钮</el-button>
  </div>
</template>

<script>
export default {
  name: 'App',
  methods: {
    transfer:function(){
      console.log("push")
      this.$router.push('message')
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
