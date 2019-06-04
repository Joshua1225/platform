<style>
.expertspot-style{
    float: left;
    font-size: 16px;
    height: 40px;
}
</style>

<template>
  <div style="padding :10px">
    
    <expertList :title="title"></expertList>
  </div>
</template>

<script>

import expertList from '@/components/ExpertList.vue'
export default {
  props: { title: String },
  name: "expertspot",
  components: {
    expertList
  },
  data: function()
  {
    return {
        papernums:100,
        quotenums:999,
    }
  }
};
</script>

