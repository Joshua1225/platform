<template>
  <div class="Top">
    <div v-if="!this.$store.state.isLog">
      <el-button type="info" plain @click="goLogin()">登录</el-button>
      
    </div>
    <div v-else>
      <i class="el-icon-user" style="font-size:40px"></i>
    </div>
  </div>
</template>

<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

<script>
import store from "@/store";
import axios from "axios";
export default {
  name: "userstate",
  data() {
    return {
    };
  },
  methods: {
    goLogin() {
      axios
        .post(
          "http://154.8.237.76:8000/platform/register?email=1&password=1&name=1"
        )
        .then(function(response) {
          console.log(response);
        })
        .catch(function(error) {
          console.log(error);
        });
      console.log(123);
    }
  }
};
</script>

<style scoped>
.Top {
  margin-top: 10px;
  height: 100%;
}
</style>
