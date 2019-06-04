// 搜索系列页面

<template>
  <div>
    <!-- Logo-->
    <el-image style="width: 500px; height: 200px; margin-top: 0px" :src="url" fit="contain"></el-image>
    <searchBar />
    <div style="width:100%;margin: 0 auto; margin-top: 0px"><echarts/></div>
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

