// 上方状态栏
// 至少包含
// 至用户主页、站内信的超链接  ‘/user’ '/message'
//this.$router.push()
//或者 <router-link to=""></router-link>
//HTML 标签重复 warn

<template>
  <div class="head">
    <el-row align="middle">
      <el-col :span="6" :offset="2" style="float:left">
        <div style="cursor : pointer" @click="goSearch">
          <el-image
            style=" width: 210px; height: 60px;  display: flex; justify-content: center; align-items: center; border-radius: 10px ;"
            :src="url"
            :fit="fit"
          ></el-image>
        </div>
      </el-col>
      <el-col :span="4" :offset="11">
        <userstate/>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import userstate from "@/components/UserState.vue";
export default {
  name: "top",
  props: {
    msg: String
  },
  data() {
    return {
      fit: "fill",
      url: require("@/assets/logo.jpg")
    };
  },
  components: {
    userstate
  },
  methods:{
    goSearch(){
      this.$router.push("/search");
    }
  }
};
</script>

<style scoped>
.head {
  background-color: gray;
  width: 100%;
}
</style>
