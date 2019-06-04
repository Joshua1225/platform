<template  >
  <div class="aform" ref="form">
    <el-card body-style="text-align :left ; padding :40px ;">
      <el-form :disabled="false" label-width="80px">
        <el-form-item :label="form.type">
          <el-select v-model="form.reasonValue" placeholder="请选择申诉原因">
            <el-option
              v-for="item in reasons"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            ></el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="当前文章" v-model="form">{{obj}}</el-form-item>

        <el-form-item label="问题描述">
          <el-input type="textarea" v-model="form.content"></el-input>
        </el-form-item>

        <el-form-item label="上传图片">
          <el-upload
            ref="upload"
            class="upload-demo"
            :action="uploadUrl"
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :before-remove="beforeRemove"
            :auto-upload="false"
            :multiple="false"
            list-type="picture-card"
            :limit="1"
            :data="form"
            :on-exceed="handleExceed"
            :on-success="handleSuccess"
            :on-error="handleError"
            :file-list="fileList"
          >
            <i class="el-icon-plus"></i>
            <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
          </el-upload>
        </el-form-item>
      </el-form>
      <div style="text-align : center ; margin-top : 10px">
        <span v-if="con">
            <el-button type="primary" @click="submit">提交</el-button>
            <el-button>取消</el-button>
        </span>
        <span>
            <el-button type="primary" @click="submit">修改</el-button>
        </span>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "appealform",
  props: {
    obj: String
  },
  data: function() {
    return {
      reasons: [
        { label: "作者错误", value: 0 },
        { label: "内容错误", value: 1 }
      ],
      form: {
        type: "申诉原因",
        obj: 12345678,
        resonValue: "",
        content: "我叫王佳奇"
      },
      uploadUrl: "",
      file: "",
      fileList: []
    };
  },
  methods: {
    submit: function() {
      this.uploadUrl = "www.baidu.com";
      this.$refs.upload.submit();
      console.log(this.$refs.upload.data);
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePreview(file) {
      console.log(file);
    },
    handleExceed(files, fileList) {
      this.$message.warning(
        `当前限制选择 1 个文件，本次选择了 ${
          files.length
        } 个文件，共选择了 ${files.length + fileList.length} 个文件`
      );
    },
    beforeRemove(file, fileList) {
      return this.$confirm(`确定移除 ${file.name}？`);
    },
    handleSuccess: function(response, file, fileList) {
      this.$message.warning("上传成功！");
    },
    handleError: function(response, file, fileList) {
      this.$message.warning("上传失败，请检查网络环境_(:з)∠)_");
    }
  }
};
</script>

<style>
.aform {
  margin-left: 30%;
}
</style>
