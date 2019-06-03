<template>
  <el-card shadow="hover" >
    <div class="expert"   v-for="expert in experts" :key="expert.title">
      <div class="name">
        <router-link class="name" to="/">{{expert.name}}</router-link>
      </div>
      <div class="organization">{{expert.organization}}</div>
      <div class="info">
        <span>研究领域：{{expert.field}}</span>
        &nbsp;&nbsp;
        <el-button type="danger" icon="el-icon-delete" circle></el-button>
      </div>
    </div>
    <el-pagination background layout="prev, pager, next" :total="1000"></el-pagination>
  </el-card>
</template>

<script>
export default {
  name: "expertList",
  data: function() {
    return {
      experts: [
        {
          name: "王佳奇",
          organization: "河北胡同口大学",
          field:"守望先锋"

        },
        {
          name: "王佳奇",
          organization: "河北胡同口大学",
          field:"守望先锋"
        }
      ]
    };
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

