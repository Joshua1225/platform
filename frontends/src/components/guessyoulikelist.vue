<style>
.likeouter-style{
  height: 55px;
  font-size: 32px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color:thistle;
}

</style>



<template>
<div>
  <el-row>
    <div class="likeouter-style"><el-col :span="24">猜你喜欢</el-col></div>
  </el-row>
  <el-row>
    <el-col :span="24">
      <PaperList />
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
    return {
    };
  },
    components: {
    PaperList
  }
};
</script>