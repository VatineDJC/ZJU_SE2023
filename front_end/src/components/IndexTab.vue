<template>
  <el-card class="box-card">
    <div class="card-header">
      <span>Smart Home management System</span>
      <el-avatar
        src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
        style="float: right"
        size="large"
        shape="square"
      />
    </div>
  </el-card>

  <el-card class="box-card" style="margin-top: 20px">
    <el-descriptions
      title="Account Informations"
      :column="2"
      border
      style="margin-bottom: 10px"
    >
      <template #extra>
        <el-button type="danger" @click="changepwd">Change password </el-button>
        <el-button type="danger" @click="logout">Log out </el-button>
      </template>
      <el-descriptions-item
        label="Username"
        label-align="center"
        align="center"
        label-class-name="my-label"
        class-name="my-content"
      >
        {{ userData?.username }}
      </el-descriptions-item>
      <el-descriptions-item label="phoneNumber" label-align="center" align="center">
        {{ userData?.phoneNumber }}
      </el-descriptions-item>
    </el-descriptions>
  </el-card>

  <el-card class="box-card" style="margin-top: 20px">
    <el-descriptions title="All the rooms in you home" :column="3" border />
    <el-row justify="space-evenly" :gutter="20">
      <template v-for="place of placeData">
        <template v-for="room of place.rooms" :key="room.id">
          <el-col :span="12">
            <el-card
              :body-style="{ padding: '0px' }"
              style="margin-bottom: 20px;"
              class="demo-image__error"
              shadow="hover"
            >
              <el-row justify="space-evenly" :gutter="20">  
                <el-col :span="12">
                  <div style="padding: 14px; font-size: 25px">
                    <el-card class="box-card">
                      <el-image
                        :src="
                          'http://192.168.31.207:8886/files/download?file_name=' + room.img
                        "
                        class="image demo-image__placeholder demonstration"
                        fit="cover"
                      >
                        <template #placeholder>
                          <div class="image-slot">
                            Loading<span class="dot">...</span>
                          </div>
                        </template>
                        <template #error>
                          <div class="image-slot">
                            <span>No img uploaded</span>
                          </div>
                        </template>
                      </el-image>
                    </el-card>
                  </div>
                </el-col>
                <el-col :span="12" style="height:100%">
                  <div style="padding: 14px; font-size: 25px">
                    <el-card shadow="never" class="box-card">
                      <span>{{ room.name }}</span>
                      <div class="bottom">
                        <time class="time">place: {{ place.name }}</time>
                      </div>
                    </el-card>
                  </div>
                </el-col>
              </el-row>
            </el-card>
          </el-col>
        </template>
      </template>
    </el-row>
  </el-card>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import qs from "qs";
import { loginRouter } from "@/router/index.js";

const props = defineProps({
  placeData: Object,
  userData: Object,
});

const currentDate = ref(new Date());

function logout() {
  axios({
    method: "post",
    url: "/api/user/logout",
    withCredentials: true,
  })
    .then((response) => {
      console.log(response.data);
      if (response.data.code === 0) {
        alert("logout success");
        loginRouter.push("/login");
      }
    })
    .catch((error) => {
      console.log(error);
    });
}

function changepwd() {
  alert("change password");
  loginRouter.push("/changepwd");
}
</script>

<script>
export default {
  name: "IndexTab",
};
</script>

<style scoped>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.box-card {
  width: auto;
  border-radius: 2.5%;
}

.time {
  font-size: 12px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button {
  padding: 0;
  min-height: auto;
}

.image {
  width: 100%;
  display: block;
}

.demo-image__error .block {
  padding: 30px 0;
  text-align: center;
  border-right: solid 1px var(--el-border-color);
  display: inline-block;
  width: 49%;
  box-sizing: border-box;
  vertical-align: top;
}

.demo-image__error .demonstration {
  display: block;
  color: var(--el-text-color-secondary);
  font-size: 14px;
  margin-bottom: 20px;
}

.demo-image__error .el-image {
  padding: 0;
  max-width: 300px;
  max-height: 200px;
  width: 100%;
  height: 200px;
}

.demo-image__error .image-slot {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  background: var(--el-fill-color-light);
  color: var(--el-text-color-secondary);
  font-size: 30px;
}

.demo-image__error .image-slot .el-icon {
  font-size: 30px;
}

.demo-image__placeholder .block {
  padding: 30px 0;
  text-align: center;
  border-right: solid 1px var(--el-border-color);
  display: inline-block;
  width: 49%;
  box-sizing: border-box;
  vertical-align: top;
}

.demo-image__placeholder .demonstration {
  display: block;
  color: var(--el-text-color-secondary);
  font-size: 14px;
  margin-bottom: 20px;
}

.demo-image__placeholder .el-image {
  padding: 0 5px;
  max-width: 300px;
  max-height: 200px;
}

.demo-image__placeholder .image-slot {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  background: var(--el-fill-color-light);
  color: var(--el-text-color-secondary);
  font-size: 14px;
}

.demo-image__placeholder .dot {
  animation: dot 2s infinite steps(3, start);
  overflow: hidden;
}
</style>
