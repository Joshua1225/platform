<style>
.expertspot-style{
    float: left;
    font-size: 16px;
    height: 40px;
}
</style>

<template>
  <div>
    <el-row>
      <el-col :span="24"><div class="expertspot-style">您关注了{{papernums}}名学者，被{{quotenums}}人关注</div></el-col>
    </el-row>
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

