<template>
  <div style="width:60%;margin: 0 auto;">
    <el-input style="width:80%;" v-model="input" placeholder="请输入搜索内容">
      <el-popover placement="left" width="100%" v-model="visible" slot="append">
        <div class="showsearch">
          包含全部检索词:
          <el-input v-model="input1" placeholder></el-input>
        </div>
        <div class="showsearch">
          包含至少一个检索词:
          <el-input v-model="input2" placeholder="多个检索词以-号分隔"></el-input>
        </div>
        <div class="showsearch">
          不包含检索词:
          <el-input v-model="input3" placeholder="多个检索词以-号分隔"></el-input>
        </div>
        <div class="showsearch">
          作者
          <el-input v-model="input4" placeholder="请输入作者名字"></el-input>
        </div>
        <div class="showsearch">
          最早发布年份
          <el-input v-model="input5" placeholder="包含全部检索词"></el-input>
        </div>
        <div class="showsearch">
          最晚发布年份
          <el-input v-model="input6" placeholder="包含全部检索词"></el-input>
        </div>
        <div class="showsearch">
          语言检索范围(中文zh或者英文en)
          <el-input v-model="input7" placeholder="包含全部检索词"></el-input>
        </div>
        <div style="text-align: right; margin: 0">
          <el-button size="mini" type="text" @click="visible = false" style="margin-top:10px">取消</el-button>
          <el-button type="primary" size="mini" @click="toSearch">搜索</el-button>
        </div>
        <el-button
          slot="reference"
          icon="el-icon-arrow-down"
          style="margin:8px 10px 8px 10px;padding:0px;width='3%'"
        ></el-button>
      </el-popover>
      <el-button
        slot="append"
        type="primary"
        icon="el-icon-search"
        style="margin:2px 10px 2px 2px;padding:0px;width='3%'"
        @click="toSearch"
      >搜索</el-button>
    </el-input>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "SearchBar",
  methods: {
    toSearch() {
      if (this.visible == true) {
        this.visible = false;
        this.$router.push({
          path: "/Result",
          query: {
            model1: 1,
            q: this.input1,
            q_not: this.input3,
            q_or: this.input2,
            start_year: this.input5,
            end_year: this.input6,
            language: this.input7,
            author: this.input4,
            order: 0,
            page_size: 10,
            page_num: 1
          }
        });
        //复原
        this.input1 = "";
        this.input3 = "";
        this.input2 = "";
        this.input5 = "";
        this.input6 = "";
        this.input7 = "";
        this.input4 = "";
      } else {
        this.$router.push({
          path: "/Result",
          query: {
            model1: 0,
            q: this.input,
            order: 0,
            page_size: 10,
            page_num: 1
          }
        });
      }
    }
  },
  data() {
    return {
      input: "",
      input1: "",
      input2: "",
      input3: "",
      input4: "",
      input5: "",
      input6: "",
      input7: "",
      visible: false
    };
  }
};
</script>

<style scoped>
.el-dropdown {
  vertical-align: top;
}
.el-dropdown + .el-dropdown {
  margin-left: 15px;
}
.el-icon-arrow-down {
  font-size: 12px;
}
.showsearch {
  width: 750px;
  margin: 0 auto;
  text-align: left;
}
</style>