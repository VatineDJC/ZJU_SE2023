<template>
    <div class="history-orders">
      <Navbar />
      <div class="orders-list">
        <h2>历史订单</h2>
        <OrderItem
          v-for="order in orders"
          :key="order.ID"
          :orderID="order.ID"
          :ItemID="order.itemID"
          :SellerID="order.userID"
          :OrderStatus="order.stat"
        />
      </div>
      <Footer />
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import Navbar from '@/components/Navbar.vue';
  import OrderItem from '@/components/OrderItem.vue';
  import Footer from '@/components/Footer.vue';
  import QueryString from 'qs';

  export default {
  components: {
    Navbar,
    OrderItem,
    Footer
  },
  data() {
    return {
      userId: '',
      orders: []
    };
  },
  mounted() {
    this.userId = localStorage.getItem('userId');
    console.log(this.userId);
    this.fetchOrders(this.userId);
  },
  methods: {
    fetchOrders(id) {
        console.log(id);
        axios({
            method: "post",
            url: "/api/order/getOrderByUser",
            data: QueryString.stringify({ id:  id}),
            withCredentials: true,
        }).then(response => {
            console.log(response.data);
            this.orders = response.data.data;
            })
            .catch(error => {
            console.log(error);
            });
    }
  }
};
</script>

<style>
.history-orders {
  padding: 20px;
}

.container {
max-width: 800px;
margin: 0 auto;
}

.orders-list {
margin-top: 20px;
}

h2 {
font-size: 24px;
margin-bottom: 20px;
}

.footer {
background-color: #f0f0f0;
padding: 20px;
text-align: center;
}
</style>