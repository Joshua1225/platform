
<style>
.infoouter {
  width: 40%;
}

.infoimg {
  height: 60%;
  width: 50%;
}

.infonick {
  width: 50%;
  height: 60%;
}
.interests {
  height: 35%;
  width: 100%;
}
</style>


<template>
  <div class="infoouter">
    <div class="infoimg">
      <el-image style="width: 100%; height: 100%" :src="url" :fit="fit"></el-image>
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
  name: "userinfo",
  props: {
    msg: String
  },
  data: function() {
    return {
      url:"http://pic.rmb.bdstatic.com/fcd9555bd33f379035bcc05e71be30d2.jpeg",
      fit:"contain",
    };
  }
};
</script>