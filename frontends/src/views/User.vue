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
    <userinforemake />
    <guessyoulike />
    </el-tab-pane>
    <el-tab-pane label="我的关注" name="second">
      <expertspot />
      </el-tab-pane>
    <el-tab-pane label="我的消息" name="third">
      <Message />
    </el-tab-pane>
    <el-tab-pane label="我的论文" name="fourth">
      <mypapers/>
    </el-tab-pane>
  </el-tabs>
  </div>
</template>
<script>
import userinforemake from "@/components/UserInfoRemake.vue";
import Message from "@/views/Message.vue";
import guessyoulike from "@/views/guessyoulike";
import mypapers from "@/views/mypapers";
import expertspot from "@/views/expertspot.vue";
export default {
  name: "user",
  components: {
    userinforemake,
    guessyoulike,
    mypapers,
    expertspot,
    Message
  },
  data: function()
  {
    return {
      chosen:"",
    }
  }
};
</script>
