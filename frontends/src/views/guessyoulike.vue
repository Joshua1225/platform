// 猜你喜欢

<style>
.userouter{
  width: 35%;
  margin-left: 10%;
}
</style>

<template>
  <div class="userouter">
    <guessyoulike />
  </div>
</template>
<script>
import guessyoulikelist from "@/components/guessyoulikelist.vue";
export default {
  name: "user",
  components: {
    guessyoulike
  }
};
</script>
