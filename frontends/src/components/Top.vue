// 上方状态栏
// 至少包含
// 至用户主页、站内信的超链接  ‘/user’ '/message'
//this.$router.push()
//或者 <router-link to=""></router-link>
//HTML 标签重复 warn

<template>
<el-row :gutter="20">
  <el-col :span="6" style="float:left">
    <div class="grid-content bg-purple">
      <div class="demo-image">
        <div class="block" >
          <el-image
            style="width: 100px; height: 100px"
            :src="url"
            :fit="fit"></el-image>
        </div>
      </div>
    </div>
  </el-col>
  <el-col :span="6"><div class="grid-content bg-purple" ></div></el-col>
  <el-col :span="6"  style="float:right"><div class="grid-content bg-purple"><userstate/></div></el-col>
</el-row>
  
</template>

<script>
import userstate from '@/components/UserState.vue'
export default {
  name: 'top',
  props: {
    msg: String
  },
   data() {
      return {
        fit:  'contain',
        url: require('@/assets/logo.jpg')
      }
   },
   components: {
    userstate
  }
}
</script>