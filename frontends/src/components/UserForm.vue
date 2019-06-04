<template>
  <div class="aform0" ref="form">
    <el-card body-style="text-align :left ; padding :40px ;">
      <el-form :disabled="false" label-width="80px">
        <el-form-item label="用户名" v-model="form">{{form.email}}</el-form-item>
        <el-form-item label="邮箱" v-model="form">{{form.email}}</el-form-item>
        <el-form-item label="头像">
          <el-upload
            class="avatar-uploader"
            action=""
            :http-request="uploadImg"
            :show-file-list="false"
            :on-success="handleSuccess"
          >
            <img v-if="imageUrl" :src="imageUrl" class="avatar">
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
        </el-form-item>

        <el-form-item label="个性签名">
          <el-input type="textarea" v-model="form.content"></el-input>
        </el-form-item>
      </el-form>
      <el-row>
        <el-col :span="2" class="interests-title">兴趣领域</el-col>
        <el-col :span="22">
          <el-tag
            :key="tag"
            v-for="tag in dynamicTags"
            closable
            :disable-transitions="false"
            @close="handleClose(tag)"
          >{{tag}}</el-tag>
          <el-input
            class="input-new-tag00"
            v-if="inputVisible"
            v-model="inputValue"
            ref="saveTagInput"
            size="small"
            @keyup.enter.native="handleInputConfirm"
            @blur="handleInputConfirm"
          ></el-input>
          <el-button v-else class="button-new-tag00" size="small" @click="showInput">+ New Tag</el-button>
        </el-col>
      </el-row>

      <div style="text-align : center ; margin-top : 10px">
        <span v-if="con">
          <el-button type="primary" @click="submitForm">提交</el-button>
          <el-button>取消</el-button>
        </span>
        <span v-else>
          <el-button type="primary" @click="submitForm">修改信息</el-button>
        </span>
      </div>
    </el-card>
  </div>
</template>

<script>
import Axios from "axios";
//url = "http://154.8.237.76/upload_paper";

export default {
  name: "userform",
  props: {
    obj: String,
    dynamicTags:[]
  },
  data: function() {
    return {
      con: true,
      imageUrl:
        "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559583527839&di=2e0ed1add3b598ac589e63c718444f05&imgtype=0&src=http%3A%2F%2Fimage20.it168.com%2Fpicshow%2F900x675%2F20111124%2F2011112416144308103.jpg",
      form: {
        email: "daiyue@buaa.edu.cn",
        content: "我叫王佳奇"
      },
      uploadUrl: "",
      file: "",
      fileList: [],
      inputVisible: false,
      inputValue: ""
    };
  },
  methods: {
    uploadImg: function(param) {
      const formData = new FormData();
      formData.append("file", param.file);
      //axios.post(url,)
      UploadImageApi(formData)
        .then(response => {
          console.log("上传图片成功");
        })
        .catch(response => {
          console.log("图片上传失败");
        });
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
    submitForm: function() {},
    handleClose(tag) {
      this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1);
    },

    showInput() {
      this.inputVisible = true;
      this.$nextTick(_ => {
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },

    handleInputConfirm() {
      let inputValue = this.inputValue;
      if (inputValue) {
        this.dynamicTags.push(inputValue);
      }
      this.inputVisible = false;
      this.inputValue = "";
    }
  }
};
</script>

<style>
.el-tag + .el-tag {
  margin-left: 10px;
}
.button-new-tag00 {
  margin-left: 10px;
  height: 32px;
  line-height: 30px;
  padding-top: 0;
  padding-bottom: 0;
}
.input-new-tag00 {
  width: 10px;
  margin-left: 10px;
  vertical-align: bottom;
}

.aform0 {
  margin-left: 10%;
}

.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
.interests-title {
  font-size: 14px;
  text-align: center;
  margin-top: 7px;
}
</style>

