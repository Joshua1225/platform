<style>
.likeouter-style {
  float: left;
  height: 40px;
  font-size: 24px;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>



<template>
  <div>
    <el-row>
      <el-card shadow="always">
        <div class="likeouter-style">猜你喜欢</div>
      </el-card>
    </el-row>
    <el-row>
      <el-col :span="24">
        <PaperList/>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Vue from "vue";
import ElementUI from "element-ui";
import PaperList from "./PaperList.vue";
import "element-ui/lib/theme-chalk/index.css";

export default {
  name: "guessyoulikelist",
  props: {},
  data: function() {
    return {};
  },
  components: {
    PaperList
  }
};
</script>