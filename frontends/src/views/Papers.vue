<template>
  <div>
    <paperinfo/>
    <el-divider></el-divider>
    <paperlist/>
  </div>
</template>

<script>
import paperinfo from '@/components/PaperInfo.vue'
import paperlist from '@/components/PaperList.vue'
export default {
  name: "papers",
  components: {
    paperinfo,
    paperlist
  }
};
</script>
