
<template>
  <el-form>
    <el-form-item label="申诉原因">
      <el-select v-model="form.reason" placeholder="请选择申诉原因">
        <el-option label="信息错误" value="info"></el-option>
        <el-option label="作者错误" value="author"></el-option>
        <el-option label="其他" value="other"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="申诉详情">
      <el-input v-model="form.info"></el-input>
    </el-form-item>
  </el-form>

</template>

<script>
export default {
    data() {
      return {
        form: {
          name:'',
          reason:''
        }
      }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
