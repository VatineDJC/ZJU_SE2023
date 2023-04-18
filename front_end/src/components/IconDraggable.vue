<template>
  <div class="far_box">
    <div v-drag="that" class="move_box" :id="device.id">

      <el-popover
          placement="top-start"
          :width="300"
          trigger="hover"
      >
        <template #reference>

          <!-- <img src="../assets/light_on.svg"> -->
          <img src="../assets/light_on.svg" alt="开灯" draggable="false" :style="'height:' + iconSize"
               v-if="device.type_content === 'light' && device.info.light !== 0">
          <img src="../assets/light_off.svg" alt="开灯" draggable="false" :style="'height:' + iconSize"
               v-if="device.type_content === 'light' && device.info.light === 0">

          <img src="../assets/switch_on.svg" alt="开灯" draggable="false" :style="'height:' + iconSize"
               v-if="device.type_content === 'switch' && device.info.status === 'on'">
          <img src="../assets/switch_off.svg" alt="开灯" draggable="false" :style="'height:' + iconSize"
               v-if="device.type_content === 'switch' && device.info.status === 'off'">

          <img src="../assets/doorlock_on.svg" alt="开灯" draggable="false" :style="'height:' + iconSize"
               v-if="device.type_content === 'lock' && device.info.status === 'on'">
          <img src="../assets/doorlock_off.svg" alt="开灯" draggable="false" :style="'height:' + iconSize"
               v-if="device.type_content === 'lock' && device.info.status === 'off'">

          <img src="../assets/sensor_on.svg" alt="开灯" draggable="false" :style="'height:' + iconSize"
               v-if="device.type_content === 'sensor'">
        </template>
        <el-table :data="[device]">
          <el-table-column width="100" property="name" label="device_name"/>
          <el-table-column width="100" property="type_content" label="type_content"/>
          <el-table-column width="100" property="info.light" label="Light" v-if="device.type_content === 'light'"/>
          <el-table-column width="100" property="info" label="value" v-if="device.type_content === 'sensor'"/>
          <el-table-column width="100" property="info.status" label="status"
                           v-if="device.type_content === 'lock' || device.type_content === 'switch' "/>
        </el-table>
      </el-popover>
    </div>
  </div>
</template>

<script setup>
const iconSize = "35px"
</script>

<script>
export default {
  // 指令
  name: "IconDraggable",
  directives: {
    drag(el, that) {
      // console.log('el', el)
      // console.log("that", that)
      // 鼠标移动到目标盒子上--监听鼠标按下事件
      el.onmousedown = function (e) {
        // console.log('e1', e)
        // 计算出此时点击目标盒子 相对于自己的左上角距离（目的是为了下方位移时候 赋值减去相应的自己左上角位置 保证盒子定位点还是自己点击的点 而不是左上角点）
        // vue项目对于原生的dom操作 其实就是在方法内 也就是js内 使用原生的方法对元素进行dom操作 和普通的js操作一样
        const disx = e.offsetX;
        const disy = e.offsetY;
        document.onmousemove = function (e2) {
          // const move_box = document.getElementsByClassName('move_box')[0];
          const move_box = document.getElementById(that.value.device.id)

          move_box.style.position = 'fixed'
          move_box.style.left = e2.clientX - disx + 'px'
          move_box.style.top = e2.clientY - disy + 'px'
          // console.log('最后的定位：', e2.clientX - disx, e2.clientY - disy, e2)
        }
        document.onmouseup = function () {
          // const move_box = document.getElementsByClassName('move_box')[0];
          const move_box = document.getElementById(that.value.device.id)

          that.value.$emit("dropped", that.value.device.id, move_box.style.top, move_box.style.left)
          document.onmousemove = document.onmouseup = null
        }
      }
    }
  },
  data() {
    return {
      msg: '其他盒子元素',
      that: this
    }
  },
  props: {
    device: Object,
    initTop: {
      type: Number,
      default: 500
    },
    initLeft: {
      type: Number,
      default: 500
    }
  },
  mounted() {
    const move_box = document.getElementById(this.device.id)
    move_box.style.position = 'fixed'
    move_box.style.left = this.initLeft + 'px'
    move_box.style.top = this.initTop + 'px'
    if(this.device.type_content === 'light'){
      console.log(this.device, this.device.info, this.device.info === 0)
    }
  }
}
</script>

<style lang="less">
.far_box {
  .move_box {
    position: fixed;
    top: 0;
    left: 0;
    width: 100px;
    height: 50px;
    line-height: 50px;
  }

  .move_box:active {
  }
}
</style>

