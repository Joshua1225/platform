<template>
  <div class="expertInfo">
    <el-row>
      <el-col :span="6">
        <el-card class="image">
          <div @click="goAppeal"><el-image class="icon" :src="this.url" ></el-image></div>
          <div class="name">{{name}}</div>
          <div class="experience">
            <div class="experienceItem" v-for="ins in experience">
              <i class="el-icon-paperclip"></i>
              &nbsp;
              {{ins}}
            </div>
          </div>
        </el-card>

        <el-card class="info">
          <div class="flag">大家好，我是练习时长两年半的蔡徐坤，喜欢唱跳rap，篮球</div>
          <div class="interest" v-for="ins in work">
            <i class="el-icon-paperclip"></i>
            &nbsp;
            {{ins}}
          </div>
        </el-card>
      </el-col>
      <el-col :span="16" offset="1">
        <el-card class="info">
          <div class="flag">大家好，我是练习时长两年半的蔡徐坤，喜欢唱跳rap，篮球</div>
          <div class="interest" v-for="ins in work">
            <i class="el-icon-paperclip"></i>
            &nbsp;
            {{ins}}
          </div>
        </el-card>
        <el-card class="info">
          <div class="flag">大家好，我是练习时长两年半的蔡徐坤，喜欢唱跳rap，篮球</div>
          <div class="interest" v-for="ins in work">
            <i class="el-icon-paperclip"></i>
            &nbsp;
            {{ins}}
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "expert",
  data: function() {
    return {
      name: "XiaoZHIPEIEN",
      experience: "膜法师;;程序员",
      interests: ["膜", "码"],
      contact: "wjq@buaa.edu.cn;;BUAA",
      work: "大家好，我是练习时长两年半的蔡徐坤;;喜欢唱跳rap，篮球",
      Cooperation: "V-dark"
    };
  },
  mounted() {
    // 初始化页面数据
    this.transfer();
  },
  methods: {
    transfer: function() {
      this.experience = this.experience.split(";;");
      this.work = this.work.split(";;");
    },
    goAppeal(){
      console.log(555555)
      this.$router.push("/appeal");
    }
  }
};
</script>
<style>
.expertInfo {
  text-align: center;
  font-family: Arial, Helvetica, Sans-Serif;
}
.experience {
  padding-left: 25px;
  text-align: left;
  color: #999;
  font-size: 13px;
}
.experienceItem {
  margin-bottom: 5px;
}
.name {
  font-size: 20px;
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
.interest {
  margin-left: 20px;
  margin-top: 3px;
  margin-bottom: 12px;
}
.work {
}
</style>

