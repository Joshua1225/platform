<template>
  <div class="Top">
    <div v-if="!this.$store.state.isLog">
      <el-button type="info" plain @click="goLogin()">鐧诲綍</el-button>
      
    </div>
    <div v-else>
      <el-row>
        <el-col :span="6"><i class="el-icon-user" style="font-size:40px"></i></el-col>
        <el-col :span="18"><div class="nick">鏅撲箣浣╂仼</div></el-col>
      </el-row>
      
    </div>
  </div>
</template>

<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

<script>
import store from "@/store";
import axios from "axios";


//var host="http://154.8.237.76:8000";
var host="";

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
          "/platform/register?email=1&password=1&name=1"
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
.nick{
  float: left;
  margin-top: 7px;
  height: 100%;
  font: bolder;
  font-size: 20px;
}
</style>
