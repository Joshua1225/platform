<template>
  <div align="center" style="padding:10px">
    <el-card class="box-card" shadow="hover">
      <e slot="header" class="clearfix">
        <span style="float:left ;font-size:20px;width:75%">
          <el-row>
            <el-col>
              <div class="title" to="/">{{paper.title}}</div>
            </el-col>
          </el-row>
          <el-row>
            <span class="author" style=" float : left ; color : #999 ">作者：</span>
            <span style="float:left" v-for="author in paper.authors" :key="author.authorid">
              <router-link class="author" :to="{path:'/expert',id:author.authorid}">{{author.name}}</router-link>&nbsp;&nbsp;
            </span>
          </el-row>
        </span>
        <span style="float:right">
          <el-button type="warning" icon="el-icon-star-off" circle style="margin-top:10px "></el-button>
          <el-button type="info" round style="margin-top:10px " @click="goAppeal">认证</el-button>
        </span>
      </e>
      <el-row style="height : 290px">
        <el-col :span="0.5">
          <div class="author" style=" float : left ; color : #999 ">摘要：</div>
        </el-col>
        <el-col :span="20" class="text item abstract">
          <div style=" float : left ; line-height:26px">&nbsp;&nbsp;&nbsp;&nbsp;{{paper.abstract}}</div>
        </el-col>
      </el-row>

      <el-divider></el-divider>
      <div class="clearfix">
        <span style="float:left">
          <p class="info">DOI：{{paper.DOI}}</p>
          <p class="info">被引量：{{paper.cited}}</p>
        </span>
        <span style="float:right">
          <el-button type="success" style="margin-top:10px" @click="download_button">下载</el-button>
        </span>
      </div>
    </el-card>
  </div>
</template>

<script>
import Axios from "axios";

//var host="http://154.8.237.76:8000";
var host = "";

export default {
  name: "paperinfo",
  data() {
    return {
      paper: {
        title: "基于深度学习的水文1",
        abstract:
          "由于Internet的使用,不分时间与地域地获得信息已成为现实,但是,如何有效利用这些信息,并使用这些信息提高生产率成为迫切需要解决的问题.机器学习是解决这类问题的有效方法之一.在此将对目前机器学习研究的主要趋势、理论与技术以及存在的问题,根据作者的研究经验进行综述,以便引起研究者的注意.",
        authors: [
          { name: "戴岳", authorid: "12345" },
          { name: "王佳奇", authorid: "15345" }
        ],
        DOI: "123",
        cited: "555",
        year: "2019",
        origin: "BUAA",
        paperid: "123"
      }
    };
  },
  methods: {
    download_button() {
      var js = {
        //id: this.paperid
      };
      Axios.post(host + "/userinfo", JSON.stringify(js)).then(function(res) {
        console.log(res);
      });
    },
    goAppeal() {
      this.$router.push("/appeal");
    }
  }
};
</script>


<style scoped>
.text {
  font-family: "Helvetica Neue", Helvetica, Arial, "Microsoft YaHei", 微软雅黑;
  font-size: 15px;
  font-weight: 400;
  margin-bottom: 2px;
  margin-top: 6px;
  color: #666;
}

.item {
  margin-bottom: 18px;
  height: 200px;
}
.abstract {
  float: left;
  color: #666;
  text-align: justify;
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
  width: 100%;
}
.gray {
  color: #999;
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
.info {
  font-size: 13px;
  margin-top: 5px;
  margin-bottom: 10px;
  font: 100;
  color: #333;
}
a:hover {
  text-decoration: underline;
  color: darkmagenta;
}
</style>
