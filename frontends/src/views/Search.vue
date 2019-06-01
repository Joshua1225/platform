// 搜索系列页面

<template>
  <div>
    <!-- Logo-->
  <top/>
    <searchBar/>
  <bottom/>
  </div>
</template>
<script>
import Top from "@/components/Top.vue";
import SearchBar from "@/components/SearchBar.vue";
import Bottom from "@/components/Bottom.vue";
export default {
  name: "search",
  components: {
    SearchBar,Bottom,Top
  }
};
</script>

