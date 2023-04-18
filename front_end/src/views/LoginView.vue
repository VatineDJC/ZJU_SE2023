<template>
  <LoginPanel></LoginPanel>
</template>

<script setup>
import { reactive } from "vue";
import axios from "axios";
import { loginRouter } from "../router/index.js";
import qs from "qs";
import LoginPanel  from "../components/LoginPanel.vue";


</script>

<script>
export default {
  name: "LoginView",
};
</script>
