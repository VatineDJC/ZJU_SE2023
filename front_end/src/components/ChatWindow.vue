<template>
    <div class="chat-window">
      <div class="messages">
        <div v-for="message in messages" :key="message.id" class="message-item">
          <div :class="['message-bubble', message.sender === 'me' ? 'sent' : 'received']">
            {{ message.content }}
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        messages: [
          {
            id: 1,
            content: "Hello",
            sender: "me"
          },
          {
            id: 2,
            content: "Hi there",
            sender: "other"
          },
          // 添加更多聊天消息的数据
        ]
      };
    }
  };
  </script>
  
  <style>
  /* 样式代码 */
  </style>
  