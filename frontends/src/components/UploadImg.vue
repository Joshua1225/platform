<template>
  <el-upload
    class="upload-simple"
    :multiple="false"
    :show-file-list="false"
    action="https://jsonplaceholder.typicode.com/posts/"
    :on-change="handleChange"
    :file-list="fileList"
  >
    <el-button size="small" type="primary">点击上传</el-button>
    <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
  </el-upload>
</template>

<script>
export default {
    name:'uploadimg'
}
</script>
<style>
.upload-simple{
  text-align: left;
  width: 300px;
  padding:10px;
}

</style>
