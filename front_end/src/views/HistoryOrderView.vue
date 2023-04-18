<template>
  <div>
    <h1>历史订单</h1>
    <table>
      <thead>
        <tr>
          <th>订单号</th>
          <th>日期</th>
          <th>总价</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in orders" :key="order.id">
          <td>{{ order.order_number }}</td>
          <td>{{ order.date }}</td>
          <td>{{ order.total_price }}</td>
        </tr>
      </tbody>
    </table>
     <button @click="goBack">返回</button>
  </div>
</template>

<script>
import axios from 'axios';
import { loginRouter } from "../router/index.js";

export default {
  data() {
    return {
      orders: [
        {
          id: 1,
          order_number: 'ORD-001',
          date: '2023-04-15',
          total_price: 100.0,
        },
        {
          id: 2,
          order_number: 'ORD-002',
          date: '2023-04-16',
          total_price: 200.0,
        },
        {
          id: 3,
          order_number: 'ORD-003',
          date: '2023-04-17',
          total_price: 300.0,
        },
      ],
    };
  },
  methods: {
    goBack() {
        loginRouter.push("/main");
    },
  },
//   mounted() {
//     axios.get('/api/orders')
//       .then(response => {
//         //this.orders = response.data;
//       })
//       .catch(error => {
//         //console.log(error);
//       });
//   },
};
</script>
