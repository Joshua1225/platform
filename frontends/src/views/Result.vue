
<template>
  <div>
    <!-- Logo-->
    <div>
      <searchBar :input="q" ref="sb" style="margin-top:10px" @searchclick="goSearch"/>
    </div>
    <br>
    <br>
    <el-row>
      <el-col :span="6">
        <div class="grid-content"></div>
      </el-col>
      <el-col :span="12">
        <div>
          <paperList
            :papers="parentPapers"
            :page_total="page_To"
            @pagechange="updatePage"
            title="搜索结果"
          />
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
var host = "";
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
    this.q = this.$route.query.q;

    axios.post(host + "/search", JSON.stringify(searchData)).then(res => {
      this.parentPapers = res.data;
      console.log(res.data);
      if (res.data.code == 0) {
        this.$message.warning("数据有限，建议加钱");
        this.$router.push("/");
      } else {
        this.transfer();
      }

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
      q: "",
      page_To: 1,
      parentSearch: "",
      parentPapers: []
    };
  },
  methods: {
    goSearch(searchData) {
      console.log(searchData);
      this.q = searchData.q;
      this.parentSearch = searchData;

      axios.post(host + "/search", JSON.stringify(searchData)).then(res => {
        if (res.data.code == 0) {
          this.$message.warning("数据有限，建议加钱");
          this.$router.push("/");
        } else {
          this.transfer();
        }
      });
    },
    updatePage(page) {
      this.parentSearch.page_num = page;
      axios.post(host + "/search", JSON.stringify(searchData)).then(res => {
        if (res.data.code == 0) {
          this.$message.warning("数据有限，建议加钱");
          this.$router.push("/");
        } else {
          this.transfer();
        }
      });
    },
    rep(str) {
      var a = str.replace("[", "");
      var b = a.replace("]", "");
      var c = b.split("\'").join("");
      var d = c.split('\"').join("");
      var e = d.split(",");
      return e;
    },
    transfer() {
     
      // for (var i = 0; i < 10; i++) {
      //   tmp[i] = this.parentPapers[i];
      //   if (this.parentPapers[i].n_citation == null) {
      //     this.parentPapers[i].n_citation = "暂无";
      //   }
      //   if (this.parentPapers[i].year == null) {
      //     this.parentPapers[i].year = "暂无";
      //   }
      //   if (this.parentPapers[i].keywords == null) {
      //     this.parentPapers[i].keywords = ["暂无"];
      //   }
      // }
      console.log(this.parentPapers);
      if (this.parentPapers.code == 0) {
        this.$message.warning("数据有限，建议加钱");
        this.$$router.push("/");
        return
      }
      this.page_To = 5;
      var temp = [];

      for (var i = 0; i < 10; i++) {
        if (this.parentPapers[i].keywords == null) {
          this.parentPapers[i].keywords = ["暂无"];
        } else {
          this.parentPapers[i].keywords = this.rep(
            this.parentPapers[i].keywords
          );
          console.log(this.parentPapers[i].keywords);
        }
        if (this.parentPapers[i].author == null) {
          this.parentPapers[i].author = ["暂无"];
        } else {
          var a = this.parentPapers[i].author.split("\'").join('\"');
          this.parentPapers[i].author = JSON.parse(a);
        }
        if (this.parentPapers[i].n_citation == null) {
          this.parentPapers[i].n_citation = "暂无";
        }
        if (this.parentPapers[i].year == null) {
          this.parentPapers[i].year = "暂无";
        }
        temp[i] = this.parentPapers[i];
      }
      this.parentPapers = temp;
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
