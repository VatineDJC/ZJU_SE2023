<template>
  <el-tabs
      v-model="openTabValue"
      type="card"
      class="demo-tabs"
      @edit="handleTabsEdit"
  >
    <el-tab-pane
        key="index"
        label="Main Page"
        name="Main Page"
    >
      <IndexTab :placeData="placeData" :userData="userData"/>
    </el-tab-pane>
    <el-tab-pane
        v-for="item in openTabs"
        :key="item.id"
        :label="item.name"
        :name="item.id"
        closable
    >
      <CanvasTab :room="item"/>
    </el-tab-pane>
  </el-tabs>
</template>

<script setup>
import {ref} from 'vue'
import IndexTab from "comps/IndexTab.vue";
import CanvasTab from "comps/CanvasTab.vue";

defineExpose({
  createNewTab,
  deleteTab,
  updateTabName
})

let openTabs = ref([])
let openTabValue = ref("Main Page")

let props = defineProps({
  placeData: Object,
  userData: Object
})

function deleteTab(room_id) {
  openTabs.value = openTabs.value.filter((tab) => tab.id !== room_id)
  openTabValue.value = "Main Page"
}

function updateTabName(room_id, room_name) {
  openTabs.value.forEach((tab) => {
    if (tab.id === room_id) {
      tab.name = room_name
    }
  })
}

function createNewTab(room_id, room_name, room_pic) {
  let new_tab_flag = true;
  for (let tab of openTabs.value) {
    if (tab.id === room_id) {
      new_tab_flag = false
      break
    }
  }
  if (new_tab_flag) {
    openTabs.value.push({id:room_id, name: room_name, img:room_pic})
  }
  openTabValue.value = room_id
  console.log("openTabs"+ openTabs)
  console.log(openTabs);
}

const handleTabsEdit = (targetName, action) => {
  console.log(action)
  if (action === 'remove') {
    const tabs = openTabs.value
    let activeName = openTabValue.value
    if (activeName === targetName) {
      tabs.forEach((tab, index) => {
        if (tab.room_id === targetName) {
          const nextTab = tabs[index + 1] || tabs[index - 1]
          if (nextTab) {
            activeName = nextTab.id
          }
        }
      })
    }

    openTabValue.value = activeName
    openTabs.value = tabs.filter((tab) => tab.id !== targetName)
    console.log(openTabs.value)
  }
}
</script>

<style>
.demo-tabs > .el-tabs__content {
  margin-top: 30px;
  margin-left: 0;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}
</style>

<script>
export default {
  name: "CanvasTabs"
}
</script>