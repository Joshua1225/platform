<template>
  <div class="infoouter">
    <el-row>
      <el-col :span="10">
        <div class="img-style">
          <el-image style="width: 210px; height: 210px" :src="url" :fit="fit"></el-image>
        </div>
      </el-col>
      <el-col :span="14">
        <el-row>
          <div class="nickname-style">{{nickname}}</div>
        </el-row>
        <el-row>
          <div class="email-style">{{email}}</div>
        </el-row>
        <el-row>
          <div class="unknown-style">11111111111111111111</div>
        </el-row>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24">
        <div class="introduction-style">{{introduction}}</div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="8">
        <div class="intereststitle-style">兴趣领域</div>
      </el-col>
      <el-col :span="16">
          <el-row>
            <el-col :span="8"><div class="interests-style">兴趣1</div></el-col>
            <el-col :span="8"><div class="interests-style">兴趣2</div></el-col>
            <el-col :span="8"><div class="interests-style">兴趣3</div></el-col>
          </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Vue from "vue";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";

export default {
  name: "userinfo",
  props: {},
  data: function() {
    return {
      url:
        "https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3504306845,2989079885&fm=173&s=9BB8A009562376AE8C3185C30300F0B5&w=640&h=480&img.JPEG",
      fit: "fill",
      nickname: "吼姆拉",
      email: "homura@madoka.qb",
      introduction: "这个人很懒什么也没有留下"
    };
  }
};
</script>
<style>
.infoouter {
  float: left;
  width: 40%;
}

.img-style {
  width: 100%;
  height: 210px;
  background-color: whitesmoke;
}

.nickname-style {
  height: 100px;
  font-size: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: aquamarine;
}
.email-style {
  height: 55px;
  font-size: 22px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: cornsilk;
}
.unknown-style {
  height: 55px;
  font-size: 22px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: aquamarine;
}
.introduction-style {
  height: 45px;
  font-size: 18px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: wheat;
}
.interests-style {
  height: 45px;
  font-size: 18px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color:violet;
}
.intereststitle-style {
  height: 45px;
  font-size: 18px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color:steelblue;
}
</style>