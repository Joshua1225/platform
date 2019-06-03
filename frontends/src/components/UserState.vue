<template>
  <div class="Top">
    <div v-if="!this.$store.state.isLog">
      <el-button type="info" plain @click="goLogin()">登录</el-button>
      
    </div>
    <div v-else>
      <el-row>
        <el-col :span="6"><i class="el-icon-user" style="font-size:40px"></i></el-col>
        <el-col :span="18"><div class="nick">晓之佩恩</div></el-col>
      </el-row>
      
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
      console.log(1)
      this.$router.push('/Login')
    }
  }
};
</script>

<style scoped>
.Top {
  margin-top: 10px;
  height: 100%;
}
.nick{
  float: left;
  margin-top: 7px;
  height: 100%;
  font: bolder;
  font-size: 20px;
}
</style>
