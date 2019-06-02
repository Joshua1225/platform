<template>
  <div>
    <paperinfo/>
    <el-divider></el-divider>
    <similarpaper/>
  </div>
</template>

<script>
import paperinfo from '@/components/PaperInfo.vue'
import similarpaper from '@/components/SimilarPaper.vue'
export default {
  name: "papers",
  components: {
    paperinfo,
    similarpaper
  }
};
</script>
