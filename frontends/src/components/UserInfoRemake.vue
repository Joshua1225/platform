<template>
  <div class="user">
    <el-card class="image">
      <el-image class="icon" :src="this.url"></el-image>
      <div class="name">我叫王佳奇</div>
    </el-card>
    <el-card class="info">
      <div class="flag">大家好，我是练习时长两年半的蔡徐坤，喜欢唱跳rap，篮球</div>
      <div class='interest' v-for="ins in interests">
          <i class="el-icon-paperclip"></i>&nbsp;
          {{ins}}</div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "userinfo",
  data: function() {
    return {
      url:
        "https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3504306845,2989079885&fm=173&s=9BB8A009562376AE8C3185C30300F0B5&w=640&h=480&img.JPEG",
      interests: ["唱", "跳", "rap", "篮球"]
    };
  }
};
</script>
<style scope>
.user {
  width: 40%;
  float: left;
  text-align: center;
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
