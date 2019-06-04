// 搜索系列页面

<template>
  <div>
    <!-- Logo-->
    <el-image style="width: 500px; height: 200px; margin-top: 0px" :src="url" fit="contain"></el-image>
    <searchBar @searchclick="getResult"/>
    <div style="width:100%;margin: 0 auto; margin-top: 0px">
      <echarts/>
    </div>
  </div>
</template>
<script>
import SearchBar from "@/components/SearchBar.vue";
import echarts from "@/components/echarts.vue";
export default {
  name: "search",
  activated: function() {
    //this.$refs.chart.drawLine();
  },
  data() {
    return {
      url: require("@/assets/logo.jpg")
    };
  },
  methods: {
    getResult(arg) {
      this.$router.push({ path: "/Result", query: arg });
    }
  },
  components: {
    SearchBar,
    echarts
  }
};
</script>

