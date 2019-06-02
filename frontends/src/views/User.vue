// 搜索系列页面

<style>
.userouter{
  width: 35%;
  margin-left: 10%;
}
</style>

<template>
  <div class="userouter">
    <userinfo />
  </div>
</template>
<script>
import userinfo from "@/components/userinfo.vue";
export default {
  name: "user",
  components: {
    userinfo
  }
};
</script>
