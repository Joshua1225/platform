<template>
  <div class="user">
    <el-card class="image">
      <el-image class="icon" src="this.$store.state.userAvator"></el-image>
      <div class="name">{{this.$store.state.userName}}</div>
    </el-card>
    <el-card class="info">
      <div class="flag">{{signature}}</div>
      <div class='interest' v-for="ins in interests">
          <i class="el-icon-paperclip"></i>&nbsp;
          {{ins}}</div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "userinfo",
  props:{
    signature:String,
    interests:[]
  },
  methods: {
    
  }
  // data: function() {
  //   return {
  //     interests: ["唱", "跳", "rap", "篮球"]
  //   };
  // }
};
</script>
<style scope>
.user {
  float: left;
  text-align: center;
  padding:10px;
}
.name {
  font-size: 20px;
  font: 黑体;
  font-weight: 10px;
  margin-top: 20px;
  margin-bottom: 20px;
}
.icon {
  width: 200px;
  height: 200px;
  margin-top: 30px;
  border-radius: 10px;
}
.info {
  text-align: left;
}
.flag {
  padding: 20px;
  color: #999;
}
.interest{
    margin-left: 20px;
    margin-top: 3px;
    margin-bottom: 12px;
}
</style>
