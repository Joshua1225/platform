
<style>
.upper {
  height: 1px;
  background-color: blue;
  width: 100%;
}
.blank {
  height: 50px;
  width: 100%;
}
.outer {
  border: 1px #000000;
  height: 180px;
}
.div-a {
  float: left;
  width: 40%;
  height: 100%;
  text-align: left;
}
.div-b {
  float: right;
  width: 40%;
  height: 100%;
}
.about {
  float: right;
  width: 80%;
  height: 25%;
  text-align: left;
  font-size: 16pt;
}
.question {
  float: right;
  width: 80%;
  height: 75%;
  line-height: 250%;
}
.contact {
  float: right;
  width: 80%;
  height: 25%;
  text-align: left;
}
</style>


<template>
  <div class="outer" id="main0">
    <div class="upper"></div>
    <div class="blank"></div>
    <div class="div-a">
      <div class="about">{{ask}}</div>
      <div class="question">{{question1}}</div>
    </div>
    <div class="div-b">
      <div class="about">{{contactus}}</div>
      <div class="contact">
        <i class="el-icon-phone"></i>
        {{contact1}}
      </div>
      <div class="contact">
        <i class="el-icon-edit-outline"></i>
        {{contact2}}
      </div>
      <div class="contact">
        <i class="el-icon-s-home"></i>
        {{contact3}}
      </div>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import App from "../App.vue";
import router from "../router";
import store from "../store";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import head from "@/components/Top.vue";

export default {
  name: "bottom",
  props: {
    msg: String
  },
  data: function() {
    return {
      ask: "关于我们",
      question1:
        "百度学术集成海量学术资源，融合人工智能、深度学习、大数据分析等技术，\
	  为科研工作者提供全面快捷的学术服务。在这里我们保持学习的态度，不忘初心，砥砺前行。",
      contactus: "联系我们",
      contact1: "1234567890",
      contact2: "1234567890",
      contact3: "1234567890"
    };
  }
};
</script>