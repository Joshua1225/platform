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
        <div class="abstract">{{paper.abstract}}</div>
        <div class="info">
          <span v-for="author in paper.authors" :key="author.authorid">
            <router-link to="/">{{author.name}}</router-link>&nbsp;
          </span>
          <span>被引量：{{paper.cited}}</span>
          &nbsp;&nbsp;
          <span class="year">-{{paper.year}}年</span>
        </div>
      </div>
      <el-pagination background layout="prev, pager, next" :total="1000"></el-pagination>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "paperList",
  props: { 
    title: String ,
    papers: []
    },
  data: function() {
    return {
      // papers: [
      //   {
      //     id: "53e9ab9eb7602d970354a97e",
      //     title: "基于深度学习的水文1",
      //     abstract:
      //       "今天搞个大新闻！苟利国家生死以,岂因祸福避趋之。今天搞个大新闻！苟利国家生死以,岂因祸福避趋之。今天搞个大新闻！苟利国家生死以,岂因祸福避趋之。今天搞个大新闻！",
      //     authors: [
      //       { name: "作者1", authorid: "12345" },
      //       { name: "作者2", authorid: "15345" }
      //     ],
      //     cited: "555",
      //     year: "2019",
      //     origin: "BUAA"
      //   },
      //   {
      //     id: "53e9ab9eb7602d970354a97e",
      //     title: "基于深度学习的水文2",
      //     abstract: "今天搞个大新闻！苟利国家生死以,岂因祸福避趋之。",
      //     authors: [
      //       { name: "作者1", authorid: "12345" },
      //       { name: "作者2", authorid: "15345" }
      //     ],
      //     cited: "555",
      //     year: "2019",
      //     origin: "BUAA"
      //   }
      // ]
    };
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

