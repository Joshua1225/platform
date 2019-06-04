
<template>
  <div>
    <!-- Logo-->
    <div>
      <searchBar :input="q" ref="sb" style="margin-top:10px"  @searchclick="goSearch"/>
    </div>
    <br>
    <br>
    <el-row>
      <el-col :span="6">
        <div class="grid-content"></div>
      </el-col>
      <el-col :span="12">
        <div>
          <paperList :papers="parentPapers" title="搜索结果"/>
        </div>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import SearchBar from "@/components/SearchBar.vue";
import Selector from "@/components/Selector.vue";
import PaperList from "@/components/PaperList.vue";
import axios from "axios";

//var host="http://154.8.237.76:8000";
var host="";
export default {
  name: "result",
  created: function() {
    var searchData = {
      q: this.$route.query.q,
      q_not: this.$route.query.q_not,
      q_or: this.$route.query.q_or,
      start_year: this.$route.query.start_year,
      end_year: this.$route.query.end_year,
      language: this.$route.query.language,
      author: this.$route.query.author,
      order: 0,
      page_size: 10,
      page_num: 1
    };
    this.q=this.$route.query.q;
    console.log(this.$refs.SearchBar);
    console.log(searchData);
    axios
      .post(host+"/search/", JSON.stringify(searchData))
      .then(res => {
        console.log(res);
      });
  },
  components: {
    SearchBar,
    Selector,
    PaperList
  },
  data() {
    return {
      q:'',
      parentPapers: [
        {
          id: "53e9ab9eb7602d970354a97e",
          title: "基于深度学习的水文114141",
          abstract:
            "今天搞个大新闻！苟利国家生死以,岂因祸福避趋之。今天搞个大新闻！苟利国家生死以,岂因祸福避趋之。今天搞个大新闻！苟利国家生死以,岂因祸福避趋之。今天搞个大新闻！",
          authors: [
            { name: "作者1", authorid: "12345" },
            { name: "作者2", authorid: "15345" }
          ],
          cited: "555",
          year: "2019",
          origin: "BUAA"
        },
        {
          id: "53e9ab9eb7602d970354a97e",
          title: "基于深度学习的水文2",
          abstract: "今天搞个大新闻！苟利国家生死以,岂因祸福避趋之。",
          authors: [
            { name: "作者1", authorid: "12345" },
            { name: "作者2", authorid: "15345" }
          ],
          cited: "555",
          year: "2019",
          origin: "BUAA"
        }
      ]
    };
  },
  methods: {
    goSearch(searchData) {
      console.log(searchData);
      axios
        .post(host+"/search/", JSON.stringify(searchData))
        .then(res => {
          console.log(res);
        });
    }
  }
};
</script>
<style>
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
</style>
