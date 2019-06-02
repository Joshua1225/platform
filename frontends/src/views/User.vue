// 搜索系列页面

<style>
.userouter{
  width: 80%;
  margin-left: 10%;
}
</style>

<template>
  <div class="userouter">
    <userinfo />
    <guessyoulike />

  </div>
</template>
<script>
import userinfo from "@/components/userinfo.vue";
import guessyoulike from "@/views/guessyoulike";
export default {
  name: "user",
  components: {
    userinfo,
    guessyoulike
  }
};
</script>
