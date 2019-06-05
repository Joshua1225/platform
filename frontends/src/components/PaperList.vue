<template>
  <div style="padding:10px">
    <el-card shadow="always" body-style="text-align : left ; font-size : 13px ;">{{title}}</el-card>
    <el-card shadow="hover">
      <el-dropdown trigger="click" style="float:right">
        <span class="el-dropdown-link">
          结果排序
          <i class="el-icon-arrow-down el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>按时间排序</el-dropdown-item>
          <el-dropdown-item>按被引量排序</el-dropdown-item>
          <el-dropdown-item>按时间降序</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <div class="paper" style shadow="hover" v-for="paper in papers" :key="paper.title">
        <div class="title">
          <router-link class="title" :to="{path:'paper',query:{id:paper.id}}">{{paper.title}}</router-link>
        </div>
        <div class="abstract"><span v-for="kw in paper.keywords">{{kw}};&nbsp;</span></div>
        <div class="info">
          <span v-for="auth in paper.author">
            <router-link :to="{path:'expert',query:{id:auth.id}}">{{auth.name}}</router-link>;&nbsp;
          </span>
          <span>被引量：{{paper.n_citation}}</span>
          &nbsp;&nbsp;
          <span class="year">-{{paper.year}}年</span>
        </div>
      </div>
      <el-pagination
        background
        layout="prev, pager, next"
        :total="page_total"
        :current-change="page_change"
      ></el-pagination>
    </el-card>
  </div>
</template>

<script>
import { constants } from 'crypto';
export default {
  name: "paperList",
  props: {
    title: String,
    papers: [],
    page_no: Number,
    page_total: Number
  },
  data: function() {
    return {};
  },
  methods: {
    page_change(p) {
      consol.log(p+" page")
      this.$$emit("pagechange", p);
    }
  }
};
</script>
<style scope>
.paperList {
  padding: 40px;
  width: 750px;
  text-align: center;
}
.paper {
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: 10px;
  padding: 10px;
  width: 600px;
  text-align: left;
  border-bottom: 1px solid #efefef;
}
.title {
  font-family: "Helvetica Neue", Helvetica, Arial, "Microsoft YaHei", 微软雅黑;
  font-size: 18px;
  font-weight: 400;
  margin-bottom: 6px;
  color: #06c;
}

.abstract {
  font-size: 15px;
  margin-top: 10px;
  color: #666;
}
.year {
  color: #999;
}
.info {
  font-size: 13px;
  margin-top: 5px;
  margin-bottom: 10px;
  font: 100;
  color: #333;
}

a {
  color: #333;
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
  color: #999;
}
</style>

