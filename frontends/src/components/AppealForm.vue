<template  >
  <div class="aform" ref="form">
    <el-card body-style="text-align :left ; padding :40px ;">
      <el-form :disabled="false" label-width="80px">
        <el-form-item :label="selectType">{{title}}</el-form-item>

        <el-form-item label="当前文章" v-model="form">{{form.objId}}</el-form-item>

        <el-form-item label="问题描述">
          <el-input type="textarea" v-model="form.content"></el-input>
        </el-form-item>

        <el-form-item label="上传文件">
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
            :http-request="uploadImg"
            :limit="1"
            :data="form"
            :on-exceed="handleExceed"
            :on-success="handleSuccess"
            :on-error="handleError"
            :file-list="fileList"
          >
            <i class="el-icon-plus"></i>
          </el-upload>
        </el-form-item>
      </el-form>
      <div style="text-align : center ; margin-top : 30px">
        <span>
          <el-button type="primary" @click="submit">提交</el-button>
        
          <el-button @click="back">取消</el-button>
        </span>
      </div>
    </el-card>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "appealform",
  props: {
    title: String
  },
  created: function() {
    if ((this.title = "upload")) {
      this.title = "论文上传";
    } else if ((this.title = "expert")) {
      this.title = "专家认证";
    } else if ((this.title = "change")) {
      this.title = "论文申诉";
    } else {
      this.title = "其他";
    }
  },
  data: function() {
    return {
      selectType: "认证原因",
      form: {
        type: "认证原因",
        objId: "",
        content: ""
      },
      uploadUrl: "",
      file: "",
      fileList: []
    };
  },
  methods: {
    submit: function(e) {
      var loginUrl = "http://154.8.237.76:8000/login";
      var loginData = { username: "123", password: "123" };

      axios.post(loginUrl, JSON.stringify(loginData)).then(res => {
        console.log(res);
        this.$refs.upload.submit();
      });
    },
    uploadImg(param) {
      var url = "http://154.8.237.76:8000/userinfo";

      axios.post(url).then(res => {
        console.log(res);
      });
      // var uploadUrl = "http://154.8.237.76:8000/upload_paper";
      // var fileObj = param.file;
      // console.log("upload");
      // var form = new FormData();
      // form.append("file", fileObj);
      // form.append("id", this.objId);
      // axios.post(uploadUrl, form).then(res => {
      //   console.log(res);
      // });
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
    },
    back: function() {
      this.$router.go(-1);
    }
  }
};
</script>

<style>
.aform {
  margin-left: 30%;
}
</style>
