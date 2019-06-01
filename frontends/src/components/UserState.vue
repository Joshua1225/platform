<template>
  <div>
    <div v-if="!this.$store.state.isLog">
        <el-button type="primary" style="float:right" @click="goLogin()">登陆</el-button>
    </div>
    <div v-else>
        <i class="el-icon-message"></i>
        <i class="el-icon-user"></i>
    </div>
  </div>
</template>

<script>
import store from '@/store'
export default {
  name: "userstate",
  data() {
    return {
      isLog: store.state.isLog
    };
  },
  methods: {
    goLogin() {
        store.commit('changeisLog')
        console.log(this.isLog)
        this.$router.push("/login")
    }
  }
};
</script>
