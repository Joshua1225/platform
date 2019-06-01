<template>
  <div class=''>
    <el-card shadow="hover" v-for="paper in papers" :key="paper.title">
      <h1>{{paper.title}}</h1>
      <el-row>
        <span v-for="author in paper.authors" :key="author.authorid">{{author.name}}</span>
      </el-row>
      <el-row>{{paper.cited}}</el-row>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "paperList",
  data: function() {
    return {
      papers: [
        {
          title: "基于深度学习的水文",
          abstract: "摘要",
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
  }
};
</script>
