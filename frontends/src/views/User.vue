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
          <userinforemake :signature="this.signature" :interests="this.interests"/>
        </el-col>
        <el-col :span="16" :offset="1">
          <paperlist title="根据您的兴趣，为您推荐了高质量的论文。"></paperlist>
        </el-col>
      </el-tab-pane>
      <el-tab-pane label="我的关注" name="second">
        <el-col>
          <expertspot :title="expertnum"></expertspot>
        </el-col>
      </el-tab-pane>
      <el-tab-pane label="我的消息" name="third">
        <Message/>
      </el-tab-pane>
      <el-tab-pane label="我的信息" name="fourth">
        <userform />
      </el-tab-pane>
      <el-tab-pane label="我的论文" name="fifth">
        <el-col :span="22">
          <paperlist :title="papernum"></paperlist>
        </el-col>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
import userinforemake from "@/components/UserInfoRemake.vue";
import Message from "@/views/Message.vue";
import paperlist from "@/components/PaperList.vue";
import userform from "@/components/UserForm.vue";
import mypapers from "@/views/mypapers";
import expertspot from "@/views/expertspot.vue";
import Axios from "axios";

export default {
  name: "user",
  created: function() {
    var data = { username: this.$store.state.userName };
    var that=this;
    Axios.post("http://154.8.237.76:8000/userinfo", JSON.stringify(data)).then(
      res => {
        console.log(res);
        that.signature=res["data"][0]["userinfo"][0]["fields"]["signature"];
        that.interests=res["data"][0]["userinfo"][0]["fields"]["interest"];
        that.transfer();
        
      }
    );
  },
  components: {
    userinforemake,
    paperlist,
    mypapers,
    expertspot,
    Message,
    userform
  },
  data: function() {
    return {
      chosen:"first",
      papernum: "您已发表了10篇论文",
      expertnum: "198",
      signature: "我喜欢唱、跳、rap、篮球",
      interests: "唱;跳;rap;篮球"
    }
  },
  methods: {
    handleClick: function(res) {},
    transfer: function() {
      this.interests = this.interests.split(";");
    }
  }
};
</script>
