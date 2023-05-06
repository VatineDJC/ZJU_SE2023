<template>
  <el-container class = "login_page">
    <el-card class="login_card">
      <el-header height="100px">
        <h5 style="font-size: 25px">Please login</h5>
      </el-header>
      <el-main>
        <el-form :inline="true" :model="formLogin" class="demo-form-inline">
          <el-row >
            <el-form-item label="用户名/Username">
              <el-input
                v-model="formLogin.user"
                placeholder="Username"
                @keydown.enter="login"
              />
            </el-form-item>
          </el-row>
          <el-row >
            <el-form-item label="密码/Password">
              <el-input
                type="password"
                v-model="formLogin.password"
                placeholder="Password"
                @keydown.enter="login"
              />
            </el-form-item>
          </el-row>
        </el-form>

        <el-row justify="center" :gutter="20">
          <el-col span=3>
            <el-button type="success" @click="enroll">创建新账户</el-button>
          </el-col>
          <el-col span=3>
            <el-button type="primary" @click="login">登录</el-button>
          </el-col>
        </el-row>
      </el-main>
    </el-card>
  </el-container>
</template>

<script setup>
import { reactive } from "vue";
import axios from "axios";
import { loginRouter } from "../router/index.js";
import qs from "qs";

// const props = defineProps({
// })

import { ref } from 'vue'

const count = ref(0)

const formLogin = reactive({
  user: "",
  password: "",
  id: "",
});

//if login, redirect to /index
axios({
  method: "post",
  url: "/api/user/check",
  withCredentials: true,
})
  .then((response) => {
    console.log(response.data);
    if (response.data.state === 0) {
      localStorage.setItem('userId', response.data.id);
      loginRouter.push("/historyorder");
    }
  })
  .catch((error) => {
    console.log(error);
  });

function enroll() {
  loginRouter.push("/enroll");
}

function login() {
  // loginRouter.push("/main");
  axios({
    method: "post",
    url: "/api/user/login",
    data: qs.stringify({ username: formLogin.user, password: formLogin.password }),
    withCredentials: true,
  })
    .then((response) => {
      console.log(response.data);
      if (response.data.code === 0) {
        localStorage.setItem('userId', response.data.id);
        loginRouter.push("/historyorder");
        alert("登录成功");
      } else {
        alert("用户名或密码错误");
        formLogin.password = "";
      }
    })
    .catch((error) => {
      console.log(error);
    });
}
</script>

<script>
export default {
  name: "LoginPanel",
};
</script>

<style scoped>
.login_page{
  text-align: start;
  height: 100%;
  background-image: url("https://tu.ltyuanfang.cn/api/fengjing.php");
}
.login_card{
  width: 30;
  border-radius: 15%;
  margin:0 auto;
  margin-top: 10%;
  margin-bottom: 10%;
}
</style>