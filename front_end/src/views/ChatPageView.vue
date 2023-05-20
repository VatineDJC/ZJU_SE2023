<template>
  <div class="chat-page">
    <div class="left-pane">
      <ChatList @selectChat="selectChat" />
    </div>
    <div class="right-pane">
      <div class="chat-window-container">
        <ChatWindow :selectedChat="selectedChat" />
      </div>
      <div class="chat-input-container">
        <ChatInput :selectedChat="selectedChat" />
      </div>
    </div>
  </div>
</template>

<script>
import ChatList from "@/components/ChatList.vue";
import ChatWindow from "@/components/ChatWindow.vue";
import ChatInput from "@/components/ChatInput.vue";

export default {
  components: {
    ChatList,
    ChatWindow,
    ChatInput
  },
  data() {
    return {
      selectedChat: null
    };
  },
  methods: {
    selectChat(chat) {
      this.selectedChat = chat;
    }
  }
};
</script>

<style>
/* 样式代码 */
</style>
