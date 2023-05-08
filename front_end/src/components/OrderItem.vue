<template>
    <div class="order-item">
      <h3>订单号:{{ orderID }}</h3>
      <!-- 其他订单信息的显示 -->
      <div class="order-details">
        <!-- 具体订单细节的显示 -->
        <p>卖家ID:{{ SellerID }}</p>
        <p>商品ID:{{ ItemID }}</p>
        <p>订单状态:{{ OrderStatus }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      orderID: {
        type: String,
        required: true
      },
      SellerID: {
        type: String,
        required: true
      },
      ItemID: {
        type: String,
        required: true
      },
      OrderStatus: {
        type: String,
        required: true
      }
      // 其他订单信息的props
    }
  };
  </script>
  
  <style>
  .order-item {
    border: 1px solid #ccc;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    background-color: #fff;
    border-radius: 4px;
  }
  
  h3 {
    font-size: 20px;
    margin-bottom: 10px;
    color: #888;
  }
  
  p {
    color: #888;
  }
  
  .order-details {
    margin-top: 10px;
  }
  
  </style>
  