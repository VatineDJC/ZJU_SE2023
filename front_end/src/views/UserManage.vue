<template>
  <div>
    <!-- 面包屑导航 -->
    <el-breadcrumb separator="/" style="padding-left: 10px;padding-bottom: 10px;font-size: 12px">
      <el-breadcrumb-item :to="{ path: '/main' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>用户管理</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 用户列表卡片 -->
    <div>
      <el-input v-model="searchId" placeholder="Search by ID" width:70px></el-input>
      <el-button type="primary" @click="search(searchId)">Search</el-button>
      <el-table :data="users" style="width: 100%">
        <el-table-column prop="id" label="ID"></el-table-column>
        <el-table-column prop="username" label="Name"></el-table-column>
        <el-table-column prop="phoneNumber" label="PhoneNumber"></el-table-column>
        <el-table-column prop="description" label="Description"></el-table-column>
        <el-table-column label="Action">
          <template v-slot="scope">
            <el-button type="danger" @click="deleteUser(scope.row.id)">Delete</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import QueryString from 'qs';
export default {
  name: 'UserManage',
  data() {
    return {
      users: [{ id: 1, username: '张三', phoneNumber: 123456, description: '测试样例' }],
      searchId: ''
    };
  },
  created() {
    this.getUsers();
  },
  methods: {
    //获取所有用户，不传入参数
    getUsers() {
      axios.get('/api/user/displayAllUser')
        .then(response => {
          console.log(response.data);
          this.users = [];
          for (var user in response.data.users) {
            this.users.push(response.data.users[user]);
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    //删除某一用户
    deleteUser(id) {
      console.log(id);
      axios({
          method: "post",
          url: "/api/user/delete",
          data: QueryString.stringify({ id:  id}),
          withCredentials: true,
      }).then(response => {
          console.log(response.data);
          this.getUsers();
        })
        .catch(error => {
          console.log(error);
        });
    },
    search(searchId) {
      if (this.searchId !== '') {
        axios({
          method: "post",
          url: "/api/user/searchbyid",
          data: QueryString.stringify({ id:  searchId}),
          withCredentials: true,
        }).then(response => {
            console.log(response.data);
            this.users = [];
            this.users.push({ id: response.data.id, username: response.data.username, 
              phoneNumber: response.data.phoneNumber, description: response.data.description });
            // for (var user in response.data.users) {
            //   this.users.push(response.data.users[user]);
            // }
          })
          .catch(error => {
            console.log(error);
          });
      } else {
        this.getUsers();
      }
    }
  }
};
</script>
