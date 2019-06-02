<style>
.mypapers-style{
    float: left;
    font-size: 16px;
    height: 40px;
}
</style>

<template>
  <div>
    <el-row>
      <el-col :span="24"><div class="mypapers-style">您已有{{papernums}}篇论文，已被引用{{quotenums}}次</div></el-col>
    </el-row>
    <paperlist/>
  </div>
</template>

<script>
import paperlist from '@/components/PaperList.vue'
export default {
  name: "mypapers",
  components: {
    paperlist
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
