<template>
  <div align="center">
    <el-card class="box-card" >
      <div slot="header" class="clearfix">
        <span style="float:left ;font-size:20px;width:75%">
          论女装
          <br>
          <div style="width:300px;float:left" v-for="author in paper.authors" :key="author.authorid">
            <router-link class="author" to="/">{{author.name}}</router-link>as&nbsp;&nbsp;
          </div>
        </span>
        <span style="float:right">
          <el-button type="warning" icon="el-icon-star-off" circle></el-button>
          <el-button type="info" round>认证</el-button>
        </span>
      </div>
      <div>摘要</div>
      <div class="text item">
        {{abstract}}
      </div>
      <el-divider></el-divider>
      <div class="clearfix">
        <span style="float:left">
          <p style="float:left;margin: 4px 0px">DOI：{{DOI}}</p>
          <br>
          <p style="float:left;margin: 4px 0px">被引量：{{reference}}</p>
        </span>
        <span style="float:right">
          <el-button type="success">下载</el-button>
        </span>
      </div>
    </el-card>
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
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
  height:400px
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}

.box-card {
  width: 80%;
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
