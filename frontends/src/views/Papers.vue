<template>
  <div style="width:100%;margin:0 auto;margin-top:30px">
    <el-row>
      <el-col :span="11" :offset="1">
        <div><paperinfo/></div>
        <div style="margin-top:10px"><expertlist title="推荐专家"/></div>
      </el-col>
      <el-col :span="11" :offset="0" >
        <paperlist class="paper-simple" title="相关文献"/>
      </el-col>
    </el-row>
    
  </div>
</template>

<script>
import paperinfo from '@/components/PaperInfo.vue'
import paperlist from '@/components/PaperList.vue'
import expertlist from '@/components/ExpertList.vue'
export default {
  name: "papers",
  components: {
    paperinfo,
    paperlist,
    expertlist
  }
};
</script>
<style>
.paper-simple{
  margin:0 auto
}
</style>
