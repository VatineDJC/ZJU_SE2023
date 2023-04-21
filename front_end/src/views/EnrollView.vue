<template>
  <el-container style="text-align: center">
    <el-card class="login_card">
      <el-header height="100px">
        <h5 style="font-size: 25px">Register your Account</h5>
      </el-header>
      <el-main>
        <el-form
          :inline="true"
          :model="formInline"
          class="demo-form-inline"
          label-width="150px"
        >
          <el-row justify="center">
            <el-form-item label="Username">
              <el-input
                v-model="formInline.user"
                placeholder="Username"
                @keydown.enter="enroll"
              />
            </el-form-item>
          </el-row>
          <el-row justify="center">
            <el-form-item label="Password">
              <el-input
                type="password"
                v-model="formInline.password"
                placeholder="Password"
                @keydown.enter="enroll"
              />
            </el-form-item>
          </el-row>
          <el-row justify="center">
            <el-form-item label="Confirm Password">
              <el-input
                type="password"
                v-model="formInline.confirm_password"
                placeholder="confirm Password"
                @keydown.enter="enroll"
              />
            </el-form-item>
          </el-row>
          <el-row justify="center">
            <el-form-item label="Phone Number">
              <el-input
                v-model="formInline.phone"
                placeholder="Phone"
                @keydown.enter="enroll"
              />
            </el-form-item>
          </el-row>
        </el-form>

        <el-row justify="center" :gutter="20">
          <el-col span="3">
            <el-button type="success" @click="backToLogin">Back to login</el-button>
          </el-col>
          <el-col span="3">
            <el-button type="primary" @click="enroll">register</el-button>
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

const formInline = reactive({
  user: "",
  password: "",
  confirm_password: "",
  phone: "",
});

//if login, redirect to /index
axios({
  method: "post",
  url: "api/user/check",
  withCredentials: true,
})
  .then((response) => {
    console.log(response.data);
    if (response.data.state  === 0) {
      loginRouter.push("/main");
    }
  })
  .catch((error) => {
    console.log(error);
  });

function backToLogin() {
  loginRouter.push("/login");
}

function enroll() {
  if (formInline.password.length < 8) {
    alert("the password should be at least 8 characters");
  } else if (formInline.password !== formInline.confirm_password) {
    alert("the password and the confirm one is not the sames");
  } else if (formInline.phone.length !== 11 || formInline.phone.charAt(0) !== "1") {
    alert("the phoneNumber's format is wrong!");
  } else {
    axios({
      method: "post",
      url: "/user/register",
      data: qs.stringify({
        username: formInline.user,
        password: formInline.password,
        phoneNumber: formInline.phone,
      }),
      withCredentials: true,
    })
      .then((response) => {
        console.log(response.data);
        if (response.data.code === 0) {
          loginRouter.push("/main");
          alert("register success");
        } else {
          alert("register failed");
          formInline.password = "";
          formInline.phone = "";
          formInline.user = "";
        }
      })
      .catch((error) => {
        console.log(error);
      });
  }
}
</script>

<script>
export default {
  name: "EnrollView",
};
</script>

<style scoped>
.login_page {
  text-align: start;
  height: 100%;
  background-image: url("https://tu.ltyuanfang.cn/api/fengjing.php");
}
.login_card {
  width: 30;
  border-radius: 15%;
  margin: 0 auto;
  margin-top: 10%;
  margin-bottom: 10%;
}
</style>
