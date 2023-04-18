<template>
  <el-container style="text-align: center">
    <el-header height="100px">
      <h5 style="font-size: 25px">Change Password</h5>
    </el-header>
    <el-main>
      <el-form :inline="true" :model="formInline" class="demo-form-inline">
        <el-row justify="center">
          <el-form-item label="Old Password">
            <el-input
              type="password"
              v-model="formInline.old_password"
              placeholder="Old Password"
              @keydown.enter="changepwd"
            />
          </el-form-item>
        </el-row>
        <el-row justify="center">
          <el-form-item label="Password">
            <el-input
              type="password"
              v-model="formInline.password"
              placeholder="New Password"
              @keydown.enter="changepwd"
            />
          </el-form-item>
        </el-row>
        <el-row justify="center">
          <el-form-item label="Confirm Password">
            <el-input
              type="password"
              v-model="formInline.confirm_password"
              placeholder="Confrim Password"
              @keydown.enter="changepwd"
            />
          </el-form-item>
        </el-row>
      </el-form>

      <el-row justify="center" :gutter="20">
        <el-col span="6">
          <el-button type="primary" @click="changepwd">Change</el-button>
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<script setup>
import { reactive } from "vue";
import axios from "axios";
import { loginRouter } from "../router/index.js";
import qs from "qs";

const formInline = reactive({
  old_password: "",
  password: "",
  confirm_password: "",
});

//if login, redirect to /index
// axios({
//   method: "post",
//   url: "api/user/check",
//   withCredentials: true,
// })
//   .then((response) => {
//     console.log(response.data);
//     if (response.data.state === 0) {
//       loginRouter.push("/main");
//     }
//   })
//   .catch((error) => {
//     console.log(error);
//   });

function changepwd() {
  if (formInline.password !== formInline.confirm_password) {
    alert("Confirm Password is not correct");
  } else {
    axios({
      method: "post",
      url: "/api/user/changepassword",
      data: qs.stringify({
        oldpassword: formInline.old_password,
        newpassword: formInline.password,
      }),
      withCredentials: true,
    })
      .then((response) => {
        console.log(response.data);
        if (response.data.code === 0) {
          loginRouter.push("/main");
          alert("modify success");
        } else {
          alert("modify failed");
          formInline.password = "";
          formInline.confirm_password = "";
          formInline.old_password = "";
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
  name: "changepassView",
};
</script>

<style scoped></style>
