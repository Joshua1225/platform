// 搜索系列页面

<template>
  <div>
    <!-- Logo-->
    <searchBar/>
    <echarts/>
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

