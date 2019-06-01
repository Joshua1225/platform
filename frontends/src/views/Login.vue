<template>
  <div>
    <form v-show="!isReg">
      <div>用户名：</div>
      <input type="text" v-model="name">
      <div>密码：</div>
      <input type="password" v-model="password">
      <div><button type="button" @click="login()">登陆</button></div>
      <div><button type="button" @click="reg()">注册</button></div>
    </form>
    <form v-show="isReg">
        <div>新用户名：</div>
        <input type="text" v-model="name">
        <div>新密码：</div>
        <input type="password" v-model="password">
        <div>再次输入密码</div>
        <input type="password" v-model="repeat">
        <div><button type="button" @click="addUesr()">确定</button></div>
        <div><button type="button" @click="cancel()">取消</button></div>  
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
        if(this.name === localStorage.getItem("name")&&this.password === localStorage.getItem("password")){
          this.name = ''
          this.password = ''
          alert("登陆成功")
          this.$router.push('/')
        }
        else{
          alert("登陆失败")
          this.password = ''
        }
        
      },
      reg () {
        console.log("调用reg")
        this.isReg = true
      },
      cancel () {
        console.log("调用cancel")
        this.name = ''
        this.password = ''
        this.repeat = ''
        this.isReg = false
      },
      addUesr (){
        if(this.password === this.repeat){
          localStorage.setItem("name",this.name)
          localStorage.setItem("password",this.password)
          alert("注册成功")
          this.name = ''
          this.isReg = false
        }
        else{
          alert("两次输入的密码不同")
          this.password = ''
          this.repeat = ''
        }
        
      }
    }
  }
</script>

<style scoped>

</style>
