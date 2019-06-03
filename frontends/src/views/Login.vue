<template>
  <div class="login-outer">
    <el-row align="middle" justify="start">
      <el-col :span="16">
        <el-image style="width: 600px; height: 400px" :src="url" :fit="fits"></el-image>
      </el-col>

      <el-col :span="8">
        <el-card class="box-card-login">
          <div class="login-inner" v-show="!isReg">
            <el-image style="width: 350px; height: 40px; margin-top: 10%" :src="url2" :fit="fit2"></el-image>
            <el-row style="margin-top: 12%">
              <el-col :span="6">
                <div class="tips">用户名：</div>
              </el-col>
              <el-col :span="18">
                <el-input v-model="usernameinput" placeholder="请输入用户名"></el-input>
              </el-col>
            </el-row>
            <el-row style="margin-top: 12%">
              <el-col :span="6">
                <div class="tips">密码：</div>
              </el-col>
              <el-col :span="18">
                <el-input v-model="passwordinput" placeholder="请输入密码" show-password></el-input>
              </el-col>
            </el-row>
            <el-row style="margin-top: 12%">
              <el-col span="6" offset="4">
                <el-button type="primary" plain @click="login()">登陆</el-button>
              </el-col>
              <el-col span="14">
                <el-button plain @click="reg()">注册</el-button>
              </el-col>
            </el-row>
          </div>

          <div v-show="isReg">
            <el-image style="width: 350px; height: 40px; margin-top: 10%" :src="url2" :fit="fit2"></el-image>
            <el-row style="margin-top: 8%">
              <el-col :span="6">
                <div class="tips">用户名：</div>
              </el-col>
              <el-col :span="18">
                <el-input v-model="newusernameinput" placeholder="请输入用户名"></el-input>
              </el-col>
            </el-row>
            <el-row style="margin-top: 8%">
              <el-col :span="6">
                <div class="tips">密码：</div>
              </el-col>
              <el-col :span="18">
                <el-input v-model="newpasswordinput" placeholder="请输入密码" show-password></el-input>
              </el-col>
            </el-row>
            <el-row style="margin-top: 8%">
              <el-col :span="6">
                <div class="tips">再次输入：</div>
              </el-col>
              <el-col :span="18">
                <el-input v-model="newpasswordreinput" placeholder="请再次输入密码" show-password></el-input>
              </el-col>
            </el-row>
            <el-row style="margin-top: 8%">
              <el-col span="6" offset="4">
              <el-button type="primary" plain @click="addUesr()">确定</el-button>
              </el-col>
              <el-col span="14">
              <el-button plain @click="cancel()">取消</el-button>
              </el-col>
            </el-row>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      isReg: false,
      name: "",
      password: "",
      repeat: "",
      usernameinput: "",
      passwordinput: "",
      newusernameinput :"",
      newpasswordinput: "",
      newpasswordreinput: "",
      fits: "contain",
      url:
        "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559570068854&di=b066e351ef728a6b786721f9e1201225&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201611%2F14%2F20161114231558_GczZe.jpeg",
      fits2: "contain",
      url2: require("@/assets/joinus.png")
    };
  },
  methods: {
    login() {
      if (
        this.name === localStorage.getItem("name") &&
        this.password === localStorage.getItem("password")
      ) {
        this.name = "";
        this.password = "";
        alert("登陆成功");
        this.$router.push("/");
      } else {
        alert("登陆失败");
        this.password = "";
      }
    },
    reg() {
      console.log("调用reg");
      this.isReg = true;
    },
    cancel() {
      console.log("调用cancel");
      this.name = "";
      this.password = "";
      this.repeat = "";
      this.isReg = false;
    },
    addUesr() {
      if (this.password === this.repeat) {
        localStorage.setItem("name", this.name);
        localStorage.setItem("password", this.password);
        alert("注册成功");
        this.name = "";
        this.isReg = false;
      } else {
        alert("两次输入的密码不同");
        this.password = "";
        this.repeat = "";
      }
    }
  }
};
</script>

<style scoped>
</style>

<style scope>
.login-outer {
  height: 400px;
  width: 80%;
  margin-left: 5%;
}
.tips {
  margin-top: 15%;
  font-size: 16px;
}
.login-inner {
  height: 100%;
  width: 100%;
}
.box-card-login {
  width: 400px;
  height: 400px;
}
</style>
