// 搜索系列页面

<style>
.userouter{
  width: 80%;
  margin-left: 10%;
}
</style>

<template>
  <div class="userouter">
      <el-tabs v-model= "chosen" type="card" @tab-click="handleClick">
    <el-tab-pane label="我的信息" name="first">
      <userinfo />
    <guessyoulike />
    </el-tab-pane>
    <el-tab-pane label="我的关注" name="second">我的关注</el-tab-pane>
    <el-tab-pane label="我的消息" name="third">我的消息</el-tab-pane>
    <el-tab-pane label="我的论文" name="fourth">
      <mypapers/>
    </el-tab-pane>
  </el-tabs>
  </div>
</template>
<script>
import userinfo from "@/components/userinfo.vue";
import guessyoulike from "@/views/guessyoulike";
import mypapers from "@/views/mypapers";
export default {
  name: "user",
  components: {
    userinfo,
    guessyoulike,
    mypapers
  },
  data: function()
  {
    return {
      chosen:"first",
    }
  }
};
</script>
