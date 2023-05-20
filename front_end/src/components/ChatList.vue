<template>
    <div class="chat-list">
      <ul>
        <li v-for="chat in chats" :key="chat.id" @click="selectChat(chat)">
          <div class="chat-item">
            <div class="avatar">
              <!-- 聊天对象的头像展示 -->
            </div>
            <div class="chat-info">
              <h3>{{ chat.name }}</h3>
              <p>{{ chat.lastMessage }}</p>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        chats: [
          {
            id: 1,
            name: "John",
            lastMessage: "Hello, how are you?"
          },
          {
            id: 2,
            name: "Emily",
            lastMessage: "Are we meeting today?"
          },
          // 添加更多聊天对象的数据
        ]
      };
    },
    methods: {
      selectChat(chat) {
        this.$emit("selectChat", chat);
      }
    }
  };
  </script>
  
  <style>
  /* 样式代码 */
  </style>
  