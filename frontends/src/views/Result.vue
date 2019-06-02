
<template>
  <div>
    <!-- Logo-->
    <div><searchBar/></div>
    <el-row>
      <el-col :span="4"><div><selector/></div></el-col>
      <el-col :span="1" :offset="1"><div class="grid-content"></div></el-col>
      <el-col :span="12"><div><paperList/></div></el-col>
    </el-row>
    
  </div>
</template>
<script>
import SearchBar from "@/components/SearchBar.vue";
import Selector from "@/components/Selector.vue"
import PaperList from "@/components/PaperList.vue"
export default {
  name: "result",
  components: {
    SearchBar,Selector,PaperList
  }
};

</script>
<style>
.grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
</style>
