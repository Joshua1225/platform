<style>
.expertspot-style{
    float: left;
    font-size: 16px;
    height: 40px;
}
</style>

<template>
  <div style="padding :10px">
      <el-card shadow="always" body-style="{padding-top : 5px ; text-align : left ; font-size : 13px ;}">
        您关注了{{papernums}}名学者，被{{quotenums}}人关注
      </el-card>
    
    <expertList />
  </div>
</template>

<script>
import expertList from '@/components/ExpertList.vue'
export default {
  name: "expertspot",
  components: {
    expertList
  },
  data: function()
  {
    return {
        papernums:100,
        quotenums:999
    }
  }
};
</script>

