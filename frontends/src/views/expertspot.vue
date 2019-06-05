<style>
.expertspot-style {
  float: left;
  font-size: 16px;
  height: 40px;
}
</style>

<template>
  <div style="padding :10px">
    <expertList flag="true" :experts2="experts1"></expertList>
  </div>
</template>

<script>
import expertList from "@/components/ExpertList.vue";
export default {
  props: { experts1: [] },
  name: "expertspot",
  components: {
    expertList
  },
  data: function() {
    return {
      papernums: 100,
      quotenums: 999
    };
  }
};
</script>

