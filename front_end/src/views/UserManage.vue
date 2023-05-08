<template>
  <div id='main_image'>
    <div class = "login-box">
      <!-- 面包屑导航 -->
      <el-breadcrumb separator="/" style="padding-left: 10px;padding-bottom: 10px;font-size: 12px">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>用户管理</el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 用户列表卡片 -->
        <div>
          <div class = "container">
          <el-input v-model="searchId" placeholder="Search by ID" width:70px class="input"></el-input>
          <el-button type="primary" @click="search(searchId)">Search</el-button>
          </div>
          <div class = "table-container">
              <el-table :data="users" style="width: 100%" >
              <el-table-column prop="id" label="ID" ></el-table-column>
              <el-table-column prop="username" label="Name" ></el-table-column>
              <el-table-column prop="phoneNumber" label="PhoneNumber" ></el-table-column>
              <el-table-column prop="description" label="Description" ></el-table-column>
              <el-table-column label="Action" >
                <template v-slot="scope">
                  <el-button type="danger" @click="deleteUser(scope.row.id)">Delete</el-button>
                </template>
              </el-table-column>
              </el-table>
          </div>
        </div>
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

<style>
#main_image{
    background-image: url("https://tu.ltyuanfang.cn/api/fengjing.php");
  width:100%;
  height:100%;
  position:fixed;
  background-size:100% 100%;
}

.container {
  display: flex;
}

.table-container {
  height: 300px; /* 设置容器的固定高度 */
  overflow: auto; /* 添加滚动条 */

}

.input {
  float: left;
  margin-right: 10px; /* 可选的间距设置 */
}

.login-box{
  border:1px solid #dccfcf;
  width: 1000px;
  margin:90px auto;
  padding: 35px 80px 15px 35px;
  border-radius: 5px;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  box-shadow: 0 0 25px #909399;
  background-color:rgba(0,0,0,0.7);
}
</style>

