// 搜索系列页面

<template>
  <div>
    <!-- Logo-->
    <searchBar/>
    <div style="height:20px"></div>
    <div style="width:60%;margin: 0 auto;"><echarts/></div>
  </div>
</template>
<script>
import SearchBar from "@/components/SearchBar.vue";
import echarts from "@/components/echarts.vue";
export default {
  name: "search",
  components: {
    SearchBar,echarts
  }
};
</script>

