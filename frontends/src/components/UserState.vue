<template>
  <div class="Top">
    <div v-if="!this.$store.state.isLog">
      <el-button type="info" plain @click="goLogin()">登录</el-button>
    </div>
    <div v-else>
      <el-row style="cursor : pointer " >
        <el-col :span="10" class="nick">
          <el-dropdown style="cursor : pointer" @command="handleCommand">
            <el-image style="width: 60px; height: 40px; border-radius: 100px " src=this.$store.state.userName :fit="fits"  @click="goUser" >
              <div slot="error" class="image-slot">
        <el-image style="width: 60px; height: 40px; border-radius: 100px " :src="url0" :fit="fits"  @click="goUser" ></el-image>
      </div>
            </el-image>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item  icon="el-icon-plus" command="toUserInfo">我的主页</el-dropdown-item>
              <el-dropdown-item icon="el-icon-circle-plus" command="logOff">注销</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </el-col>
        <el-col :span="14">
          <div class="nick" style="margin-top: 8px"  @click="goUser">{{this.$store.state.userName}}</div>
        </el-col>
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
  store,
  data() {
    return {
      fits: "contain",
      url:
        "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559570068854&di=b066e351ef728a6b786721f9e1201225&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201611%2F14%2F20161114231558_GczZe.jpeg",
      url0:
      require('@/assets/avatar2.png'),
    };
  },
  methods: {
    goLogin() {

      this.$router.push("/login");
    },
    goUser:function(){
      this.$router.push("/user");
    },
    handleCommand(command) {
      if(command=="toUserInfo")
      {
        console.log(1);
        this.$router.push("/user");
      }
      else if(command=="logOff")
      {
        console.log(1);
        store.commit('setOffline');
        this.$router.push("/Login");
      }
    },
  }
};
</script>

<style scoped>
.Top {
  margin-top: 10px;
  height: 100%;
}
.nick {
  float: left;
  height: 100%;
  font: bolder;
  font-size: 20px;
}
</style>
