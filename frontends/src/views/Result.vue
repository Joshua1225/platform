
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
          <paperList :papers="parentPapers" @nextpage="updatePage" title="搜索结果"/>
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
      parentSearch:'',
      parentPapers: []
    };
  },
  methods: {
    goSearch(searchData) {
      console.log(searchData);
      this.parentSearch=searchData;

      axios
        .post(host+"/search", JSON.stringify(searchData))
        .then(res => {
          this.parentPapers=res.data
          console.log(res);
        });
    },
    updatePage(page){
        this.parentSearch.page_num=page;
        axios
        .post(host+"/search", JSON.stringify(searchData))
        .then(res => {
          this.parentPapers=res.data
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
