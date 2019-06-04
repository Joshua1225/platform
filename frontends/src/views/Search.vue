// 搜索系列页面

<template>
  <div>
    <!-- Logo-->
    <el-image style="width: 500px; height: 200px; margin-top: 70px" :src="url" fit="contain"></el-image>
    <searchBar style="margin-top: 70px"/>
    <div style="height:20px"></div>
    <div style="width:60%;margin: 0 auto;"><echarts/></div>
  </div>
</template>
<script>
import SearchBar from "@/components/SearchBar.vue";
import echarts from "@/components/echarts.vue";
export default {
  name: "search",
  data() {
    return{
      url:require('@/assets/logo.jpg'),
    }
  },
  components: {
    SearchBar,echarts
  }
};
</script>

