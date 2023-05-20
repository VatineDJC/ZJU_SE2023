<template>
    <div class="chat-input">
      <input v-model="newMessage" placeholder="输入消息..." />
      <button @click="sendMessage">发送</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        newMessage: ""
      };
    },
    methods: {
      sendMessage() {
        // 在这里处理发送消息的逻辑
        if (this.newMessage.trim() !== "") {
          // 发送消息的逻辑
          console.log("发送消息:", this.newMessage);
          // 清空输入框
          this.newMessage = "";
        }
      }
    }
  };
  </script>
  
  <style>
  /* 样式代码 */
  </style>
  