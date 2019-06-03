<template>
  <div>
    <button @click="change()">切换</button>
    <form v-if="!isReg">
      用户名：
      <input type="text" v-model="name">
      密码：
      <input type="password" v-model="password">
      <button type="button" @click="login()">登陆</button>
      <button type="button" @click="reg()">注册</button>
    </form>
    <form v-else>
      新用户名：
      <input type="text" v-model="name">
      新密码：
      <input type="password" v-model="password">
      再次输入密码
      <input type="password" v-model="repeat">
      <button type="button" @click="addUesr()">确定</button>
      <button type="button" @click="cancel()">取消</button>
    </form>
  </div>
</template>

<script>

  export default {
    name: 'Login',
    data () {
      return {
        isReg : false,
        name: '',
        password: '',
        repeat: ''
      }
      
    },
    methods: {
      login () {
        this.$router.push('/')
      },
      reg () {
        // console.log("调用reg")
        
        this.isReg = true
      },
      cancel () {
        console.log("调用cancel")
        this.isReg = false
      },
      change () {
        console.log("调用change")
        this.isReg = !this.isReg
      },
      addUesr (){
          
          // localStorage.setItem("name",this.name)
          // localStorage.setItem("password",this.password)
        
      }
    }
  }
</script>

<style scoped>

</style>
