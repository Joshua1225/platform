<template>
  <div>
    <div>
      <span class="left">
        <table border="1">抠脚大汉如何女装</table>
        <table border="1">作者：王佳奇</table>
      </span>
      <span class="right">
        <el-button type="warning" icon="el-icon-star-off" circle></el-button>
        <el-button type="info" round>认证</el-button>
      </span>
    </div>
    <div>
      <table width="100%" height="300px" border="1">123</table>
    </div>
    <div>
      <span class="left">
        <table border="1">DOI：123456</table>
        <table border="1">被引量：1111111</table>
      </span>
      <span class="right">
        <el-button type="success">下载</el-button>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: "paperinfo"
};
</script>


<style scoped>
table {
  border: 1;
}
.left {
  float: left;
}
.right {
  float: right;
}
div {
  overflow: hidden;
}
span {
  display: inline-block;
}
</style>
