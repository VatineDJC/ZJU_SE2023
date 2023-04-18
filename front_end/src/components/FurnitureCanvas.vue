<template>
  <template v-for="device of deviceData">
    <icon-draggable :device="device" :init-top="device.posx" :init-left="device.posy"
                    @dropped="handleDrop"/>
  </template>
</template>

<script setup>
import IconDraggable from "comps/IconDraggable.vue";
import axios from "axios";
import qs from "qs";

const props = defineProps({
  deviceData: Object
})

function handleDrop(device_id, top, left) {
  top = parseInt(top)
  left = parseInt(left)
  axios({
    method: 'post',
    url: 'api/device/update/pos',
    data: qs.stringify({'id': device_id, 'pos_x': top, 'pos_y': left}),
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
export default {
  name: "FurnitureCanvas"
}

</script>

<style scoped>

</style>