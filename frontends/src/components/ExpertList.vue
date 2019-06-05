<template>
  <div align="center" style="padding:10px">
    <el-card shadow="always" body-style="text-align : left ; font-size : 13px ;">您关注了{{experts2.length}}位专家</el-card>
    <el-card shadow="hover" >
      <div class="expert"   v-for="expert in experts2">
        <div class="name">
          <router-link class="name" to="/expert">{{expert.fields.name}}</router-link>
        </div>
        <el-button type="danger" icon="el-icon-delete" circle style="float : right" v-show="flag==='true'"></el-button>
        <div class="organization">{{expert.fields.orgs}}</div>
        <div class="info">
          <span>研究领域：{{expert.field.tags}}</span>
          &nbsp;&nbsp;
        </div>
      </div>
      <el-pagination background layout="prev, pager, next" :total="1000"></el-pagination>
    </el-card>
  </div>
</template>

<script>
import axios from "axios"
//import { METHODS } from 'http';
export default {
  name: "expertList",
  props: { 
    title: String ,
    flag: String,
    experts2: [],
    },
  data: function() {
    return {
    };
  },
  created: function(){
    for(expert in experts2){
      if(!boolean(expert.field.tags)){
        expert.field.tags="暂无"
        console.log(暂无)
      }
    }
  }
};
</script>
<style scoped>
.expertList {
  margin: 10px;
}
.expert {
  margin-top: 10px;
  margin-bottom: 10px;
  text-align: left;
  border-bottom: 1px solid #efefef;
}
.name {
  font-family: "Helvetica Neue", Helvetica, Arial, "Microsoft YaHei", 微软雅黑;
  font-size: 18px;
  font-weight: 400;
  margin-bottom: 6px;
  color: #06c;
}

.organization {
  font-size: 15px;
  margin-top: 10px;
  color: #666;
}
.info {
  font-size: 13px;
  margin-top: 5px;
  margin-bottom: 10px;
  font: 100;
  color: #333;
}

</style>

