<template>
  <div v-if="!isLog">
    <el-button type="primary" @click="goLogin()">登陆</el-button>
  </div>
</template>

<script>
export default {
  name: "userstate",
  data() {
    return {
      isLog: false
    };
  },
  methods: {
    goLogin() {
      this.$router.push("/login");
    }
  }
};
</script>
