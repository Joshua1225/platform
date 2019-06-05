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
          <userinforemake
            :signature="this.userInfo.signature"
            :interests="this.userInfo.interests"
          />
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
        <userform :info="this.userInfo" @up="updateInfo"/>
      </el-tab-pane>
      <el-tab-pane label="我的论文" name="fifth">
        <el-col :span="22">
          <paperlist :title="papernum"></paperlist>
        </el-col>
      </el-tab-pane>
      <el-tab-pane label="我的收藏" name="sixth">
        <el-col :span="22">
          <collectionlist :title="collectionnum"></collectionlist>
        </el-col>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
import userinforemake from "@/components/UserInfoRemake.vue";
import Message from "@/views/Message.vue";
import paperlist from "@/components/PaperList.vue";
import collectionlist from "@/components/collectionlist.vue";
import userform from "@/components/UserForm.vue";
import mypapers from "@/views/mypapers";
import expertspot from "@/views/expertspot.vue";
import Axios from "axios";

var host = "http://154.8.237.76:8000";
//var host="";

export default {
  name: "user",
  created: function() {
    var data = { username: this.$store.state.userName };
    this.updateInfo();
  },
  components: {
    userinforemake,
    paperlist,
    mypapers,
    expertspot,
    Message,
    userform,
    collectionlist
  },
  data: function() {
    return {
      userInfo: {
        signature: "我喜欢唱、跳、rap、篮球",
        interests: "唱;跳;rap;篮球",
        email: "123@163.com",
        username: "123"
      },
      chosen: "first",
      papernum: "您已发表了10篇论文",
      expertnum: "198",
      collectionnum: "您已收藏了10篇论文"
    };
  },
  methods: {
    handleClick: function(res) {},

    updateInfo: function() {
    
      Axios.post(host + "/userinfo", JSON.stringify({username:123})).then(res => {
        console.log(res);
        that.userInfo.signature =
          res["data"][0]["userinfo"][0]["fields"]["signature"];
        that.userInfo.interests =
          res["data"][0]["userinfo"][0]["fields"]["interest"];
      });
    }
  }
};
</script>
