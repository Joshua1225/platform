<template>
  <div class="divx" style="width : 80% ;margin: 0 auto;">
    <div class="divx" style shadow="hover">
      <span>
        <el-row>
          <router-link class="title" to="/">{{paper.title}}</router-link>
        </el-row>
        <el-row >
          <span  v-for="author in paper.authors" :key="author.authorid">
            <router-link class="author" to="/">{{author.name}}</router-link>as&nbsp;&nbsp;
          </span>
          <span class="right">
            <el-button type="warning" icon="el-icon-star-off" circle></el-button>
            <el-button type="info" round>认证</el-button>
          </span>
        </el-row>
      </span>
    </div>
    <div class="divx">
      <table width="100%" height="300px" border="1">123</table>
    </div>
    <div class="divx">
      <span class="left">
        <table border="1">DOI：{{DOI}}</table>
        <table border="1">被引量：{{reference}}</table>
      </span>
      <span class="right">
        <el-button type="success">下载</el-button>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: "paperinfo",
  data(){
    return {
      paper : {
        title: "基于深度学习的水文1",
        abstract: "今天搞个大新闻！苟利国家生死以,岂因祸福避趋之。今天搞个大新闻！苟利国家生死以,岂因祸福避趋之。今天搞个大新闻！苟利国家生死以,岂因祸福避趋之。今天搞个大新闻！",
        authors: [
          { name: "作者1", authorid: "12345" },
          { name: "作者2", authorid: "15345" }
        ],
        cited: "555",
        year: "2019",
        origin: "BUAA"
      }
      
    }
  }
};
</script>


<style scoped>
table {
  border: 1;
}
.left {
  float: left;
}
.right {
  float: right;
}
.divx {
  overflow: hidden;
}
.title {
  font-family: "Helvetica Neue", Helvetica, Arial, "Microsoft YaHei", 微软雅黑;
  font-size: 18px;
  font-weight: 400;
  margin-bottom: 6px;
  float: left;
  color: #06c;
}
.author {
  font-family: "Helvetica Neue", Helvetica, Arial, "Microsoft YaHei", 微软雅黑;
  font-size: 15px;
  font-weight: 400;
  margin-bottom: 2px;
  margin-top: 6px;
  float: left;
  color: #06c;
  
}
a:hover {
  text-decoration: underline;
  color: darkmagenta;
}
</style>
