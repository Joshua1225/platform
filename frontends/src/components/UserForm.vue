<template>
  <div class="aform0">
    <el-card body-style="text-align :left ; padding :40px ;">
      <el-form :disabled="false" label-width="80px" @submit.native.prevent>
        <el-form-item label="用户名" >{{info.username}}</el-form-item>
        <el-form-item label="注册邮箱">{{info.email}}</el-form-item>
        <el-form-item label="个人头像">
          <el-upload
            class="avatar-uploader"
            action="www"
            :http-request="uploadImg"
            :show-file-list="false"
            :on-success="handleAvatarSuccess"
            :before-upload="beforeAvatarUpload"
          >
            <img v-if="imageUrl" :src="imageUrl" class="avatar">
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
        </el-form-item>

        <el-form-item label="个性签名">
          <el-input type="textarea" v-model="signature"></el-input>
        </el-form-item>
        <el-form-item label="兴趣领域">
          <el-tag
            :key="tag"
            v-for="tag in dynamicTags"
            closable
            :disable-transitions="false"
            @close="handleClose(tag)"
          >{{tag}}</el-tag>
          <el-input
            class="input-new-tag"
            v-if="inputVisible"
            v-model="inputValue"
            ref="saveTagInput"
            size="small"
            @keyup.enter.native="handleInputConfirm"
            @blur="handleInputConfirm"
          ></el-input>
          <el-button v-else class="button-new-tag" size="small" @click="showInput">+ New Interest</el-button>
        </el-form-item>
      </el-form>

      <div style="text-align : center ; margin-top : 10px">
        <span v-if="con">
          <el-button type="primary" @click="submitForm">提交</el-button>
          <el-button @click="recoverForm">取消</el-button>
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
  name: "userform",
  props: {
    info: {}
  },
  created: function() {
    console.log(this.info);
    this.signature = this.info.signature;
    this.email = this.info.email;
    this.username = this.info.username;
    var tmp=this.info.interests;
    
    this.dynamicTags =tmp.split(";");
    console.log(tmp.split(";"));
    console.log(this.dynamicTags);
  },
  data: function() {
    return {
      con: true,
      imageUrl: "",
      signature: "",
      dynamicTags: [],
      uploadUrl: "",
      file: "",
      fileList: [],
      inputVisible: false,
      inputValue: ""
    };
  },
  methods: {
    uploadImg(param) {
      const formData = new FormData();
      formData.append("file", param.file);

      console.log("to do: add url");
      Axios.post(param.action, formData)
        .then(response => {
          this.$message.error("上传成功!");
          this.handleAvatarSuccess(param);
        })
        .catch(response => {
          this.$message.error("上传失败!");
        });
    },
    handleAvatarSuccess(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === "image/jpeg";
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error("上传头像图片只能是 JPG 格式!");
      }
      if (!isLt2M) {
        this.$message.error("上传头像图片大小不能超过 2MB!");
      }
      return isJPG && isLt2M;
    },

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
    },
    getCollectPaper() {
      var data = { username: "123" };
      Axios.post(host + "/listcollection", JSON.stringify(data)).then(res => {
        console.log(res);
      });
    },
    submitForm: function() {
      for (i in this.dynamicTags) {
        this.interest = this.interest + ";" + i;
      }
      var info = {
        username: "123",
        signature: this.signature,
        interest: this.interest
      };
      Axios.post(host + "/change_info", info).then(res => {
        console.log(res);
        this.$emit("up");
      });
    },
    recoverForm:function(){
      this.signature=info.signature;
      this.dynamicTags=info.interests.spilit(';');
    }
  }
};
</script>

<style scoped>
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
  margin: 10px;
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

