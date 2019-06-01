// 上方状态栏
// 至少包含
// 至用户主页、站内信的超链接  ‘/user’ '/message'
//this.$router.push()
//或者 <router-link to=""></router-link>
//HTML 标签重复 warn

<template>
    <el-button>A Header</el-button>
</template>

<script>
export default {
  name: 'top',
  props: {
    msg: String
  }
}
</script>