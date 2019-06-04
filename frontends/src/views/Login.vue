<template>
  <div class="login-outer">
    <el-row align="middle" justify="start">
      <el-col :span="16">
        <el-image style="width: 600px; height: 400px" :src="url" :fit="fits"></el-image>
      </el-col>

      <el-col :span="8">
        <el-card class="box-card-login">
          <div class="login-inner" v-show="!isReg">
            <el-image style="width: 350px; height: 40px; margin-top: 10%" :src="url2" :fit="fits2"></el-image>
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
              <el-col :span="6" :offset="4">
                <el-button type="primary" plain @click="login()">登陆</el-button>
              </el-col>
              <el-col :span="14">
                <el-button plain @click="reg()">注册</el-button>
              </el-col>
            </el-row>
          </div>

          <div v-show="isReg">
            <el-image style="width: 350px; height: 40px; margin-top: 5%" :src="url2" :fit="fits2"></el-image>
            <el-row style="margin-top: 5%">
              <el-col :span="6">
                <div class="tips">用户名：</div>
              </el-col>
              <el-col :span="18">
                <el-input v-model="newusernameinput" placeholder="请输入用户名"></el-input>
              </el-col>
            </el-row>
            <el-row style="margin-top: 5%">
              <el-col :span="6">
                <div class="tips">电子邮箱：</div>
              </el-col>
              <el-col :span="18">
                <el-input v-model="emailinput" placeholder="请输入电子邮箱地址" show-password></el-input>
              </el-col>
            </el-row>
            <el-row style="margin-top: 5%">
              <el-col :span="6">
                <div class="tips">密码：</div>
              </el-col>
              <el-col :span="18">
                <el-input v-model="newpasswordinput" placeholder="请输入密码" show-password></el-input>
              </el-col>
            </el-row>
            <el-row style="margin-top: 5%">
              <el-col :span="6">
                <div class="tips">再次输入：</div>
              </el-col>
              <el-col :span="18">
                <el-input v-model="newpasswordreinput" placeholder="请再次输入密码" show-password></el-input>
              </el-col>
            </el-row>
            <el-row style="margin-top: 5%">
              <el-col :span="6" :offset="4">
                <el-button type="primary" plain @click="addUesr()">确定</el-button>
              </el-col>
              <el-col :span="14">
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
import axios from "axios";
import store from "@/store";
import { constants } from 'crypto';
export default {
  name: "Login",
  store,
  data() {
    return {
      isReg: false,
      usernameinput: "",
      passwordinput: "",
      newusernameinput: "",
      emailinput: "",
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
      if (this.usernameinput === "" || this.passwordinput === "") {
        alert("用户名或密码为空！");
      } else {
        var json = {
          username: this.usernameinput,
          password: this.passwordinput
        };
        axios
          .post("http://154.8.237.76:8000/login", JSON.stringify(json))
          .then(res => {
            console.log(res);
            console.log(store.state.isLog);
            store.commit("setOffline");
            if (res["data"][0]["code"] === 0) {
              store.commit("setOnline");
              this.$router.push("/");
              // axios
              // .post("http://154.8.237.76:8000/userinfo")
              // .then(res => {
              //     console.log(res);
              // })
              // .catch(res => {
              //   console.log(res);
              // });
            } else if (res["data"][0]["code"] === 2) {
              alert("账号不存在！");
            } else if (res["data"][0]["code"] === 3) {
              alert("密码错误！");
            }
          })
          .catch(res => {
            console.log(res);
          });
      }
    },
    reg() {
      console.log("reg页面");
      this.isReg = true;
    },
    cancel() {
      console.log("返回login");
      this.newusernameinput = "";
      this.newpasswordinput = "";
      this.newpasswordreinput = "";
      this.emailinput = "";
      this.isReg = false;
    },
    addUesr() {
      if (
        this.newusernameinput === "" ||
        this.newpasswordinput === "" ||
        this.newpasswordreinput === "" ||
        this.emailinput === ""
      ) {
        alert("请补全信息！");
      } else {
        if (this.newpasswordinput === this.newpasswordreinput) {
          var reg = {
            username: this.newusernameinput,
            password: this.newpasswordinput
          };
          axios
            .post("http://154.8.237.76:8000/register", JSON.stringify(reg))
            .then(response => {
              console.log(response);
            })
            .catch(response => {
              console.log(response);
            });
        } else {
          alert("两次输入的密码不一致！");
        }
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
