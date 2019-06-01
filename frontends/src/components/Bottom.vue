// 下方状态栏
// 删除无用信息
//仅作为展示性质

<style>
.upper {
  height: 500px;
}
.outer {
  border: 1px #000000;
  height: 150px;
  text-align: left;
}
.div-a {
  float: left;
  width: 40%;
  height: 100%;
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
}
.question {
  float: right;
  width: 80%;
  height: 75%;
  line-height:200%;
}
.contact {
  float: left;
  width: 51%;
  height: 25%;
}
</style>


<template>
  <div class="outer" id="main0">
    <div class="div-a">
      <div class="about">{{ask}}</div>
      <div class="question">{{question1}}</div>
    </div>
    <div class="div-b">
      <div class="contact">{{contactus}}</div>
      <div class="contact">{{contact1}}</div>
      <div class="contact">{{contact2}}</div>
      <div class="contact">{{contact3}}</div>
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