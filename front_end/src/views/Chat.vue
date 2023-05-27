<template>
    <Navbar />
    <div class="message-container">
      <div class="message-list">
        <ul>
          <li @click="selectMessage(user)" v-for="(user, index) in userlist" :class="{ 'active': user.id === currentUser.id }" :key="index">
            <div class="message-info">
              <img class="avatar" :src="user.avatar" alt="avatar">
              <div>
                <div class="username">{{ user.name }}</div>
                <div class="preview">{{ user.messages.length > 0 ? user.messages[user.messages.length - 1].text : '暂无消息' }}</div>
              </div>
            </div>
          </li>
        </ul>
      </div>
      <div class="message-dialog">
        <div class="dialog-header">{{ currentUser.name }}</div>
        <ul class="dialog-body" ref="messageList">
          <li class="message-item" v-for="(message, index) in currentMessage.messages" :class="{'right': message.sender_id !== currentUser.id, 'left': message.sender_id === currentUser.id}" :key="index">
            <div class="message-time">{{ message.time }}</div>
            <div class="message-text" :class="{'right': message.sender_id !== currentUser.id, 'left': message.sender_id === currentUser.id}">{{ message.text }}</div>
          </li>
        </ul>
        <div class="message-footer">
          <input class="message-input" type="text" v-model="newMessage.text" @keydown.enter="sendMessage(this.userId)">
          <button class="message-submit" @click="sendMessage(this.userId)">发送</button>
          <button class="message-flush" @click="flush(this.userId)">刷新</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import Navbar from '@/components/Navbar.vue';
  import QueryString from 'qs';
  import axios from 'axios';
import { time } from '@tensorflow/tfjs';
  export default {
    components: {
        Navbar
    },
    data() {
      return {
        userlist: [
          {
            id: 1,
            name: "John",
            user_id: 1,
            avatar: "https://via.placeholder.com/40x40/ff0000/ffffff?text=J",
            messages: [
              {
                sender_id: 1,
                text: "Hello",
                time: "1 minute ago"
              }
            ]
          },
          {
            id: 2,
            name: "Anna",
            user_id: 2,
            avatar: "https://via.placeholder.com/40x40/00ff00/ffffff?text=A",
            messages: [
              {
                sender_id: 2,
                text: "Hi",
                time: "3 minutes ago"
              }
            ]
          },
          {
            id: 3,
            name: "Bob",
            user_id: 3,
            avatar: "https://via.placeholder.com/40x40/0000ff/ffffff?text=B",
            messages: [
              {
                sender_id: 3,
                text: "Hey",
                time: "5 minutes ago"
              }
            ]
          }
        ],
        currentMessage: {
          id: null,
          messages: []
        },
        currentUser: {
          id: 0,
          name: null,
          avatar: null
        },
        newMessage: {
          text: ""
        },
        userId:0,
        options: {
          year: 'numeric',
          month: '2-digit',
          day: '2-digit',
          hour: '2-digit',
          minute: '2-digit',
          second: '2-digit'
        },
        time:""
      };
    },
    mounted() {
        this.userId = localStorage.getItem('userId');
        this.userId = 1;
        this.flush(this.userId);
    },
    methods: {
      selectMessage(user) {
        this.currentMessage = user;
        this.currentUser = {
          id: user.id,
          name: user.name,
          avatar: user.avatar
        };
        this.newMessage.text = "";
      },
      sendMessage(UID) {
        if (this.newMessage.text) {
          this.time = new Date().toLocaleString();
          axios({
                method: "post",
                url: "/api/chat/send",
                data: QueryString.stringify({ chatID: this.currentMessage.id,
                                              sender_id: UID,
                                              text: this.newMessage.text,
                                              time: this.time}),
                withCredentials: true,
            }).then(response => {
                  this.flush(UID);
                  const message = {
                    text: this.newMessage.text,
                    time: this.time,
                  };
                  this.currentMessage.messages.push(message);
                  this.newMessage.text = "";
                  this.$nextTick(() => {
                    const messageList = this.$refs.messageList;
                    messageList.scrollTop = messageList.scrollHeight;  // 将滚动条滚动到底部
                  });
                })
                .catch(error => {
                console.log(error);
            });
        }
      },
      // pollMessages() {
      //   setInterval(() => {
      //     this.flush(this.userId);
      //   }, 2000);  // 每隔2秒获取一次最新的消息数据
      // },
      flush(UID){
        axios({
                method: "post",
                url: "/api/chat/get",
                data: QueryString.stringify({ UID:UID}),
                withCredentials: true,
            }).then(response => {
                console.log(UID);
                console.log(response.data);
                this.userlist = response.data.data;
                })
                .catch(error => {
                console.log(error);
            });
      }
    }
  };
  </script>
  
  <style>
  .message-container {
    display: flex;
    height: 100%;
    flex:1;
    border: 1px solid #ddd;
    margin-top:2px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
    border-radius: 5px;
  }
  
  .message-list {
    width: 33.33%;
    height: 100%;
    overflow-y: auto;
    border-right: 1px solid #ddd;
    border-radius: 5px;
  }
  
  .message-list li.selected {
    background-color: #f0f0f0;
  }
  
  .message-dialog {
    flex: 1;
    height: 100%;
    display: flex;
    flex-direction: column;
  }
  
  .dialog-header {
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 20px;
    border-bottom: 1px solid #ddd;
  }
  
  .dialog-body {
    flex: 1;
    list-style: none;
    margin: 0;
    overflow-y: auto;
    background-color: #decfcf;
    padding: 10px;
  }
  
  .message-time {
    font-size: 12px;
    color: #000000;
  }
  
  .message-text {
    color: #000000;
    background-color: #b69696;
    border-radius: 5px;
    padding: 10px;
    font-size: 14px;
    max-width: 60%;
    word-wrap: break-word;
  }
  
  .message-footer {
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-top: 1px solid #2d2d2d;
  }
  
  .message-input {
    flex: 1;
    border-radius: 5px;
    border: 1px solid #cdc2c2;
    padding: 10px;
    font-size: 14px;
  }
  
  .message-submit {
    flex-shrink: 0;
    margin-left: 10px;
    background-color: #409eff;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 8px 16px;
    font-size: 14px;
    cursor: pointer;
  }

  .message-flush {
    flex-shrink: 0;
    margin-left: 10px;
    background-color: #409eff;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 8px 16px;
    font-size: 14px;
    cursor: pointer;
  }
  
  .message-submit:hover {
    background-color: #66b1ff;
  }
  
  @media screen and (max-width: 768px) {
    .message-container {
      flex-direction: column;
    }
  
    .message-list,
    .message-dialog {
      width: 100%;
    }
  
    .message-list {
      height: 30%;
    }
  
    .message-dialog {
      height: 70%;
      border-top: 1px solid #aea7a7;
    }
  }
  
  .message-info {
    display: flex;
    align-items: center;
    padding: 10px;
  }
  
  .avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
  }
  
  .username {
    font-weight: bold;
    font-size: 16px;
  }
  
  .preview {
    margin-left: 10px;
    font-size: 14px;
    color: #999;
  }

  /* 新增样式，设置message-dialog的height为100% */
  .message-dialog {
    height: 100%;
  }

  /* 新增样式，设置dialog-body的flex-grow属性为1，使其填充父容器的剩余空间 */
  .dialog-body {
    flex-grow: 1;
  }
  
  html,
    body,
    #app {
    height: 95%;
    }

  .message-item {
    display: flex;
    width: 100%;
    flex-direction: column;
    margin: 10px;
    max-width: 95%;
    }

    .right {
    align-self: flex-end;
    text-align: right;
    margin-right: 0px;
    }

    .left {
    align-self: flex-start;
    text-align: left;
    }

    li.active {
    color: #409eff;
    background-color: #cf0a0a;
    font-weight: bold;

    }
  </style>
  