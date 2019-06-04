<template>
  <el-card shadow="hover">
    <div class="msg" style shadow="hover" v-for="msg in msgs" :key="msg.time">
      <div class="title">{{msg.type}} &nbsp;{{msg.time}}</div>
      <div class="content">
        <el-row :gutter="20">
          <el-col :span="22"><div><router-link to="/">{{msg.content}}</router-link></div></el-col>
          <el-col style="padding:10px" :span="2"> <i class="el-icon-delete"></i></el-col>
        </el-row>
        
        <!-- <i class="el-icon-delete"></i> -->
      </div>
    </div>
    <el-pagination background layout="prev, pager, next" :total="1"></el-pagination>
  </el-card>
</template>

<script>
export default {
  name: "MessageList",
  data: function() {
    return {
      msgs: [
        {
          type: "申诉消息",
          time: "2019-6-3 2:43",
          content:
            "今天搞个大新闻！苟利国家生死以,岂因祸福避趋之。今天搞个大新闻！苟利国家生死以,岂因祸福避趋之。今天搞个大新闻！苟利国家生死以,岂因祸福避趋之。",
          status: 0
        }
      ]
    };
  },
  methods: {
    getData: function(page) {
      for (var i = 0; i < 10; i++) {
        
      }
    }
  },
  mounted() {
    this.getData(0);
  }
};
</script>
<style scoped>

.msgList {
  padding: 40px;
  text-align: center;
}
.msg {
  margin-top: 5px;
  margin-bottom: 20px;
  margin-left: 10px;
  padding: 10px;
  width: 800px;
  text-align: left;
  border-bottom: 1px solid #efefef;
}
.title {
  font: 微软雅黑;
  font-size: 15px;
  font-weight: 200;
  margin-bottom: 6px;
  color: #999;
}

.content {
  font-size: 15px;
  margin-top: 10px;
  display: block;
  color: #666;

}

a {
  color: #666;
  text-decoration: none;
  padding: 5px;
}
a:hover {
  text-decoration: underline;
  color: #999;
}
</style>

