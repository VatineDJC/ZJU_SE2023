<template>
  <el-container>
    <el-aside width="fit content">
      <el-menu :collapse="isCollapse">
        <template v-for="place of placeData">
          <el-sub-menu :index="place.id+''">
            <template #title>
              <el-icon>
                <HomeFilled/>
              </el-icon>
              <span v-if="modifyMode === false">{{ place.name }}</span>
              <el-input
                  v-if="modifyMode === true"
                  v-model="place.name"
                  @blur="updateplaceName(place.id, place.name)"
              />
              <el-button
                  v-if="modifyMode === true"
                  type="danger"
                  style="margin-left: 8px"
                  @click="removePlace(place.id)"
              >
                Remove
              </el-button>
            </template>

            <!-- <template > -->
            <el-menu-item>
              <span v-if="modifyMode === false">{{ place.description }}</span>
              <el-input
                  v-if="modifyMode === true"
                  v-model="place.description"
                  @blur="updateplaceDes(place.id, place.description)"
              />
            </el-menu-item>
            <!-- </template> -->

            <template v-for="room of place.rooms">
              <el-menu-item :index="room.id+''" @click="createNewTab(room.id, room.name, room.img)">
                <el-icon>
                  <House/>
                </el-icon>
                <span v-if="modifyMode === false">{{ room.name }}</span>
                <el-input
                    v-if="modifyMode === true"
                    v-model="room.name"
                    @blur="updateRoomName(room.id, room.name)"
                />
                <el-button
                    v-if="modifyMode === true"
                    type="danger"
                    style="margin-left: 8px"
                    @click="removeRoom(place.id, room.id)"
                >
                  Remove
                </el-button>
              </el-menu-item>
            </template>
            <el-menu-item :index="'new_room'+place.id" @click="createNewRoom(place.id)">
              <el-icon>
                <Plus/>
              </el-icon>
              <span>New Room</span>
            </el-menu-item>
          </el-sub-menu>
        </template>

        <!--        <el-menu-item-group title="场景管理">-->
        <el-menu-item @click="createNewplace" index="add">
          <el-icon>
            <CirclePlus/>
          </el-icon>
          <span>New Place</span>
        </el-menu-item>
        <!-- <el-menu-item @click="changeModifyMode" index="modify"> -->
        <el-menu-item index="modify">
        <!-- <el-space index="modify" style="padding: 0.1rem;margin-left: 10%;"> -->
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
      <CanvasTabs ref="canvasTabsRef" :placeData="placeData" :userData="userData"/>
    </el-main>
  </el-container>
</template>

<script setup>
import {ref} from 'vue'
import axios from "axios";
import {loginRouter} from "@/router/index.js";
import CanvasTabs from "comps/CanvasTabs.vue";
import qs from "qs";

const canvasTabsRef = ref();
const isCollapse = ref(false)
let placeData = ref([])
let userData = ref()
let modifyMode = ref(false)

function changeModifyMode() {
  modifyMode.value = !modifyMode.value
}

function changeCollapse() {
  isCollapse.value = !isCollapse.value;
  modifyMode.value = false
}

//if login, redirect to /index
axios({
  method: 'post',
  url: 'api/user/check',
  withCredentials: true
})
    .then((response) => {
      if (response.data.state !== 0) {
        loginRouter.push('/login')
      } else {
        userData.value = response.data
        console.log(response.data)
      }
    })
    .catch((error) => {
      console.log(error)
    })

function getAllPlaceData() {
  // get place data
  axios({
    method: 'post',
    url: 'api/place/list',
    withCredentials: true
  })
      .then((response) => {
        placeData.value = response.data.data
        console.log(response)
        console.log(placeData.value)
        placeData.value.forEach((i)=>{
            axios({
              method: 'post',
              url: 'api/place/getinfo',
              data: qs.stringify({"placeid": i.id}),
              withCredentials: true
            }).then((inner_response)=>{
              i.description = inner_response.data.description
              if(i.description == null){
                i.description = "no description"
              }
            }).catch((error) => {
              console.log(error)
            })

            console.log("i now is "+i)
            axios({
              method: 'post',
              url: 'api/room/list',
              data: qs.stringify({"placeid": i.id}),
              withCredentials: true
            }).then((inner_response)=>{
              i.rooms = inner_response.data.data
              console.log(inner_response)
              console.log(i.rooms)
            }).catch((error) => {
              console.log(error)
            })
        })
        console.log(placeData.value)
      })
      .catch((error) => {
        console.log(error)
      })
}

getAllPlaceData()

function createNewTab(room_id, room_name, room_pic) {
  canvasTabsRef.value.createNewTab(room_id, room_name, room_pic)
}

function createNewplace() {
  axios({
    method: 'post',
    url: 'api/place/create',
    data: qs.stringify({"name": "Untitled Place"}),
    withCredentials: true
  })
      .then((response) => {
        console.log(response.data)
        if (response.data.code === 0) {
          console.log("create success")
          placeData.value.push(response.data.info)
        }
      })
      .catch((error) => {
        console.log(error)
      })
}

function createNewRoom(place_id) {
  axios({
    method: 'post',
    url: 'api/room/create',
    data: qs.stringify({"placeid": place_id, "name": "Untitled room"}),
    withCredentials: true
  })
      .then((response) => {
        console.log(response.data)
        if (response.data.code === 0) {
          placeData.value.forEach((place) => {
            if (place.id === place_id) {
              if(place.rooms == null){
                place.rooms = []
              }
              place.rooms.push({id:response.data.info.id,name:response.data.info.name})
              console.log(place.rooms)
            }
          })
        }
      })
      .catch((error) => {
        console.log(error)
      })
}

function removePlace(place_id) {
  axios({
    method: 'post',
    url: 'api/place/remove',
    data: qs.stringify({"id": place_id}),
    withCredentials: true
  })
      .then((response) => {
        console.log(response.data)
        if (response.data.code === 0) {
          placeData.value.forEach((place) => {
            if (place.id === place_id) {
              for (let room of place.rooms) {
                canvasTabsRef.value.deleteTab(room.id)
              }
            }
          })
          placeData.value = placeData.value.filter((place) => place.id !== place_id)
        }
      })
      .catch((error) => {
        console.log(error)
      })
}

function removeRoom(place_id, room_id) {
  axios({
    method: 'post',
    url: 'api/room/remove',
    data: qs.stringify({"id": room_id}),
    withCredentials: true
  })
      .then((response) => {
        // console.log(response.data)
        if (response.data.state === 0) {
          placeData.value.forEach((place) => {
            if (place.id === place_id) {
              place.rooms = place.rooms.filter((room) => room.id !== room_id
              )
            }
          })
        }
      })
      .catch((error) => {
        console.log(error)
      })
      .finally(() => {
        // 点按钮同时也是点menu-item 把错误新建的标签页关了
        canvasTabsRef.value.deleteTab(room_id)
      })
}

function updateplaceName(place_id, place_name) {
  axios({
    method: 'post',
    url: 'api/place/modifyinfo',
    data: qs.stringify({"id": place_id, "name": place_name}),
    withCredentials: true
  })
      .then((response) => {
        console.log(response.data)
      })
      .catch((error) => {
        console.log(error)
      })
}

function updateRoomName(room_id, room_name) {
  axios({
    method: 'post',
    url: 'api/room/changename',
    data: qs.stringify({"id": room_id, "new_name": room_name}),
    withCredentials: true
  })
      .then((response) => {
        console.log(response.data)
        canvasTabsRef.value.updateTabName(room_id, room_name)
      })
      .catch((error) => {
        console.log(error)
      })
}

function updateplaceDes(place_id, place_description){
  axios({
    method: 'post',
    url: 'api/place/modifyinfo',
    data: qs.stringify({"id": place_id, "description": place_description}),
    withCredentials: true
  })
      .then((response) => {
        console.log(response.data)
      })
      .catch((error) => {
        console.log(error)
      })
}

</script>

<script>

</script>

<style scoped>

</style>