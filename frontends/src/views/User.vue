// 搜索系列页面

<style>
.userouter {
  width: 80%;
  margin-left: 10%;
}
</style>

<template>
  <div class="userouter">
    <el-tabs v-model="chosen" type="card" @tab-click="handleClick">
      <el-tab-pane label="我的主页" name="first">
        <el-col :span="6">
          <userinforemake/>
        </el-col>
        <el-col :span='16' :offset="1">
          <paperlist title="根据您的兴趣，为您推荐了高质量的论文。"></paperlist>
        </el-col>
      </el-tab-pane>
      <el-tab-pane label="我的关注" name="second">
        <el-col>
          <expertspot/>
        </el-col>
        
      </el-tab-pane>
      <el-tab-pane label="我的消息" name="third">
        
        <Message/>
      </el-tab-pane>
      <el-tab-pane label="我的论文" name="fourth">
        <el-col :span="22">
          <paperlist title="papernum"></paperlist>
        </el-col>
      
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
import userinforemake from "@/components/UserInfoRemake.vue";
import Message from "@/views/Message.vue";
import paperlist from "@/components/PaperList.vue";
import mypapers from "@/views/mypapers";
import expertspot from "@/views/expertspot.vue";
export default {
  name: "user",
  components: {
    userinforemake,
    paperlist,
    mypapers,
    expertspot,
    Message
  },
  data: function() {
    return {
      chosen:"first",
    }
  },
  methods:{
    handleClick:function(res){

    }
  }
};
</script>
