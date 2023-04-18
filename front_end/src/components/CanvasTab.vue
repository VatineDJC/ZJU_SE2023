<template>
  <el-container>
    <el-aside width="fit content">
      <el-menu style="margin-top: 0; font-weight: normal" :collapse="isCollapse">
        <template v-for="device of deviceData">
          <el-sub-menu :index="device.id">
            <template #title>
              <el-icon v-if="device.type_content === 'switch'  && device.info.status === 'off'"  >
                <TurnOff />
              </el-icon>
              <el-icon v-if="device.type_content === 'switch'  && device.info.status === 'on'"  >
                <Open />
              </el-icon>
              <el-icon v-if="device.type_content === 'light'">
                <Sunrise/>
              </el-icon>
              <el-icon v-if="device.type_content === 'sensor'">
                <Odometer/>
              </el-icon>
              <el-icon v-if="device.type_content === 'lock'  && device.info.status === 'off'"  >
                <Lock />
              </el-icon>
              <el-icon v-if="device.type_content === 'lock'  && device.info.status === 'on'"  >
                <Key />
              </el-icon>

              <span v-if="modifyMode === false">{{ device.name }}</span>
              <el-input
                  v-if="modifyMode === true"
                  v-model="device.name"
                  @blur="updateDeviceName(device.id, device.name)"
              />
              <el-button
                  v-if="modifyMode === true"
                  type="danger"
                  style="margin-left: 8px"
                  @click="deleteDevice(device.id)"
              >
                Remove
              </el-button>
            </template>

            <el-menu-item :index="device.id+''">
              <el-slider
                  v-if="device.type === 0"
                  v-model="device.info.light"
                  @change="updateDeviceInfo(device.id, device.info)"
              >
              </el-slider>
              <el-tag
                  v-if="device.type === 1"
                  class="ml-2"
              >
                <span>value: {{ device.info }}</span>
              </el-tag>
              <el-switch
                  v-model="device.info.status"
                  v-if="device.type_content === 'lock' || device.type_content === 'switch'"
                  active-value='on'
                  inactive-value='off'
                  class="ml-2"
                  active-text="on"
                  inactive-text="off"
                  style="font-weight: normal"
                  @change="updateDeviceInfo(device.id, device.info)"
              />
            </el-menu-item>
          </el-sub-menu>
        </template>
      

        <el-sub-menu index="add">
          <template #title>
            <el-icon>
              <CirclePlus/>
            </el-icon>
            <span>New Device</span>
          </template>

          <el-menu-item index="add1" @click="createNewDevice('light', '0')">
            <el-icon>
              <Plus/>
            </el-icon>
            <span>Light</span>
          </el-menu-item>
          <el-menu-item index="add2" @click="createNewDevice('switch', '0')">
            <el-icon>
              <Plus/>
            </el-icon>
            <span>Switch</span>
          </el-menu-item>
          <el-menu-item index="add3" @click="createNewDevice('lock', '0')">
            <el-icon>
              <Plus/>
            </el-icon>
            <span>Lock</span>
          </el-menu-item>
          <el-menu-item index="add4" @click="createNewDevice('sensor', getRandomInt(256))">
            <el-icon>
              <Plus/>
            </el-icon>
            <span>Sensor</span>
          </el-menu-item>
        </el-sub-menu>

        <el-menu-item  index="modify">
          <el-icon>
            <Edit/>
          </el-icon>
          <span>Modify
            <el-switch
            v-model="modifyMode"
            class="ml-2"
            style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949; margin-right: 0%;"
          />
          </span>
        </el-menu-item>

        <el-menu-item @click="changeCollapse" index="collapse">
          <el-icon v-if="!isCollapse">
            <DArrowLeft/>
          </el-icon>
          <el-icon v-if="isCollapse">
            <DArrowRight/>
          </el-icon>
          <span>Fold</span>
        </el-menu-item>
        <!--        </el-menu-item-group>-->

      </el-menu>
    </el-aside>
    <el-main>
      <upload-file v-if="!room_.img" :room_id="room_.id" @uploaded="handleUpload"/>
      <el-image :src="'http://192.168.31.207:8886/files/download?file_name='+room_.img" fit="fill"
                v-if="room_.img"/>
      <furniture-canvas :deviceData="deviceData" v-if="room_.img"/>
    </el-main>
  </el-container>
</template>

<script setup>
import {ref} from "vue";
import axios from "axios";
import qs from "qs";
import {getRandomInt} from "element-plus/es/utils/index";
import FurnitureCanvas from "comps/FurnitureCanvas.vue";
import UploadFile from "comps/UploadFile.vue";

let deviceData = new ref([])
const isCollapse = ref(false)
let modifyMode = ref(false)

function changeModifyMode() {
  modifyMode.value = !modifyMode.value
}

function changeCollapse() {
  isCollapse.value = !isCollapse.value;
  modifyMode.value = false
}

const props = defineProps({
  room: Object
})

const room_ = new ref(props.room)

function handleUpload(file_name,room_id) {
  console.log("handle")
  room_.value.img = file_name
  axios({
    method: 'post',
    url: 'api/room/changeimg',
    data: qs.stringify({'roomid': room_id,'new_img':file_name}),
    withCredentials: true
  })
      .then((response) => {
        console.log("handleUpload:response.data")
        console.log(response.data)
        
        // deviceData.value.forEach((device) => {
        //   if (device.device_type === 'light') {
        //     device.device_info = parseInt(device.device_info)
        //   }
        // })
      })
      .catch((error) => {
        console.log(error)
      })
  // this.reload()
}

function getAllDeviceData(room_id) {
  axios({
    method: 'post',
    url: 'api/device/list',
    data: qs.stringify({'roomid': room_id}),
    withCredentials: true
  })
      .then((response) => {
        console.log("getAlldevice:response.data")
        console.log(response.data)
        deviceData.value = response.data.data
        // deviceData.value.forEach((device) => {
        //   if (device.device_type === 'light') {
        //     device.device_info = parseInt(device.device_info)
        //   }
        // })
      })
      .catch((error) => {
        console.log(error)
      })
}

getAllDeviceData(props.room.id)
console.log(deviceData.value)

function updateDeviceName(device_id, device_name) {
  axios({
    method: 'post',
    url: 'api/device/update/name',
    data: qs.stringify({"id": device_id, "name": device_name}),
    withCredentials: true
  })
      .then((response) => {
        console.log(response.data)
      })
      .catch((error) => {
        console.log(error)
      })
}

function updateDeviceInfo(device_id, device_info) {
  console.log(device_id, device_info)
  axios({
    method: 'post',
    url: 'api/device/update/info',
    data: {"id": device_id, "info": device_info},
    withCredentials: true
  })
      .then((response) => {
        console.log(response.data)
      })
      .catch((error) => {
        console.log(error)
      })
}

function deleteDevice(device_id) {
  axios({
    method: 'post',
    url: 'api/device/delete',
    data: qs.stringify({"id": device_id}),
    withCredentials: true
  })
      .then((response) => {
        console.log("in del device response.data")
        console.log(response.data)
        if (response.data.code === 0) {
          deviceData.value = deviceData.value.filter((device) => device.id !== device_id)
        }
      })
      .catch((error) => {
        console.log(error)
      })
}

function createNewDevice(device_type, device_info) {
  console.log(device_info)
  var type_num = 0;
  if(device_type == "light"){
    type_num =0;
  }else if(device_type == "sensor"){
    type_num = 1;
  }else if(device_type == "switch"){
    type_num =2;
  }else if(device_type == "lock"){
    type_num =3;
  }
  console.log("creating in room "+props.room.id)
  axios({
    method: 'post',
    url: 'api/device/add',
    data: qs.stringify(
        {
          "name": "Untitild"+device_type,
          "type": type_num,
          "roomid": props.room.id
        }),
    withCredentials: true
  })
      .then((response) => {
        console.log(response.data.data)
        if (response.data.code === 0) {
          deviceData.value.push(response.data.data)
        }
      })
      .catch((error) => {
        console.log(error)
      })
  console.log(deviceData)
}
</script>

<script>
export default {
  name: "CanvasTab"
}
</script>

<style scoped>

</style>