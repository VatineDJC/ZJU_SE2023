<template>
    <div class="navbar">
      <ul>
        <li><a href="#/home">首页</a></li>
        <li><a href="#/historyorder">历史订单</a></li>
        <li><a href="#/userdetail">个人信息</a></li>
      </ul>
    </div>
  </template>
  
  <style>
  .navbar {
    background-color: #f0f0f0;
    padding: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
  }
  
  li {
    display: inline;
    margin-right: 10px;
  }
  
  a {
    text-decoration: none;
    color: #333;
    font-weight: bold;
  }
  
  .logo {
    font-size: 24px;
  }
  
  </style>
  