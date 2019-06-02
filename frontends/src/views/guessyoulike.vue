// 猜你喜欢

<style>
.guessyoulikeouter-style { 
    float: right;
    width: 55%;
    height: 100%;
}
</style>

<template>
  <div class="guessyoulikeouter-style">
    <guessyoulikelist />
  </div>
</template>
<script>
import guessyoulikelist from "@/components/guessyoulikelist.vue";
export default {
  name: "guessyoulike",
  components: {
    guessyoulikelist
  }
};
</script>
