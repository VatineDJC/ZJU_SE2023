<template>
  <el-upload
      class="upload-demo"
      drag
      action="api/files/upload"
      :on-success="handleSuccess"
      :data={room_id}
      multiple
  >
    <el-icon class="el-icon--upload">
      <upload-filled/>
    </el-icon>
    <div class="el-upload__text">
      Drag your room pic to this box<em> Or click Here to Upload a pic</em>
    </div>
    <div class="el-upload__text">
      the ico visualize function cnbe used after a icon is uploaded
    </div>
    <template #tip>
      <div class="el-upload__tip">
        the size of the pic mustn't be to large, otherwise the loading will be effected
      </div>
    </template>
  </el-upload>
</template>

<script setup>
const props = defineProps({
  room_id: Object
})

const emit = defineEmits(['handleUpload'])
console.log(props.room_id)

function handleSuccess(res) {
  console.log(res)
  emit("uploaded", res.file_name,props.room_id)
}
</script>

<script>
export default {
  name: "UploadFile"
}
</script>

<style scoped>

</style>