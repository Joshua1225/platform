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
          <expertspot :experts1="experts"></expertspot>
        </el-col>
      </el-tab-pane>
      <el-tab-pane label="我的消息" name="third">
        <Message :message="message"/>
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
    this.getmessage();
    this.getexperts();
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
      collectionnum: "您已收藏了10篇论文",
      message:[],
      experts:[],
      preexperts : {
        
    code: 0,
    followed: [
      {
        "model": "backends.unidentifiedacademia",
        "pk": "53f439a9dabfaec22ba9f894",
        "fields": {
          "name": "M. Krahe",
          "n_pubs": 1,
          "h_index": 0,
          "n_citation": 0,
          "orgs": "['']",
          "tags": "暂无",
          "pubs": "[{'i': '53e9a841b7602d970318af6b', 'r': 1}]",
          "position": null,
          "experience": null,
          "education": null,
          "tendency": null
        }
      },
      {
        "model": "backends.unidentifiedacademia",
        "pk": "53f439a9dabfaee1c0abba5c",
        "fields": {
          "name": "Jonathan S Potts",
          "n_pubs": 4,
          "h_index": 1,
          "n_citation": 63,
          "orgs": "['Centre for Maritime Research, The National Maritime Museum, Greenwich, London SE10 9NF, UK']",
          "tags": "'Recent Developments'",
          "pubs": "[{'i': '53e99a04b7602d970224e4e0', 'r': 1}, {'i': '53e99f64b7602d97028361a0', 'r': 1}, {'i': '53e9b259b7602d9703cfc02d', 'r': 1}, {'i': '53e9b39db7602d9703e8245a', 'r': 0}]",
          "position": null,
          "experience": null,
          "education": null,
          "tendency": null
        }
      },
      {
        "model": "backends.unidentifiedacademia",
        "pk": "53f43d98dabfaedf435b6442",
        "fields": {
          "name": "Lung-Ming Tsay",
          "n_pubs": 5,
          "h_index": 0,
          "n_citation": 0,
          "orgs": "['']",
          "tags": "暂无",
          "pubs": "[{'i': '53e9a3abb7602d9702cb8f10', 'r': 0}, {'i': '53e9b38fb7602d9703e7183e', 'r': 2}, {'i': '53e9a448b7602d9702d669b5', 'r': 0}, {'i': '56d866eddabfae2eeea78414', 'r': 0}, {'i': '56d8d216dabfae2eeeac6889', 'r': 0}]",
          "position": null,
          "experience": null,
          "education": null,
          "tendency": null
        }
      }
    ]
  }
    };
  },
  methods: {
    handleClick: function(res) {},
    getmessage: function() {
      var that=this;
      Axios.post(host + "/getmessage").then(res => {
        console.log("message:",res);
        that.message = res["data"];
      });
    },
    getexperts: function() {
      var that=this;
      Axios.post(host + "/listfollow", JSON.stringify({username:123})).then(res => {
        console.log("experts:",res);
        that.experts = that.preexperts.followed;
        console.log("that.experts:",that.experts);
      });
    },
    updateInfo: function() {
      var that=this;
      Axios.post(host + "/userinfo", JSON.stringify({username:123})).then(res => {
        console.log("userinfo:",res);
        that.userInfo.signature =
          res["data"][0]["userinfo"][0]["fields"]["signature"];
        that.userInfo.interests =
          res["data"][0]["userinfo"][0]["fields"]["interest"];
      });
    }
  }
};
</script>
