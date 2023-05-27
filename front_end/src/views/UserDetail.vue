<template>
    <div id='main_image'>
        <Navbar />
        <el-card class = "box">
            <el-row>
                <el-col :span="8">
                    <h3>ID: {{ user.id }}</h3>
                    <h3>用户名: {{ user.username }}</h3>
                    <h3>登录状态: {{ user.isLoggedIn ? '已登录' : '未登录' }}</h3>
                </el-col>
                <el-col :span="8">
                    <h3>个人信息</h3>
                    <p>{{ user.description }}</p>
                </el-col>
                <el-col :span="8">
                    <h3>电话号码</h3>
                    <p>{{ user.phoneNumber }}</p>
                </el-col>
            </el-row>
        </el-card>

        <el-card class = "box">
            <h3>其他人对他的评价</h3>
            <el-table :data="user.reviews">
                <el-table-column label="评价用户" prop="user"></el-table-column>
                <el-table-column label="评价内容" prop="content"></el-table-column>
                <el-table-column label="评价时间" prop="time"></el-table-column>
            </el-table>
        </el-card>
        <Footer />
    </div>
</template>


<script>
import axios from 'axios';
import QueryString from 'qs';
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';
export default {
    components: {
        Navbar,
        Footer
    },
    name: 'UserDetail',
    data() {
        return {
            user: {
                id: 10,
                username: 'JohnDoe',
                isLoggedIn: true,
                description: '用户的个人信息',
                phoneNumber: '电话号码',
                reviews: [
                    { user: 'user1', content: '评价1', time: '2023-05-20' },
                    { user: 'user2', content: '评价2', time: '2023-05-21' },
                    { user: 'user3', content: '评价3', time: '2023-05-22' }
                ]
            }
        };
    },
    created() {
        this.getinfo();
    },
    methods: {
        getinfo() {
                this.user.username = this.$route.query.username ||localStorage.getItem('userName');
                this.user.id = this.$route.query.userId || localStorage.getItem('userId');;
                axios({
                    method: "post",
                    url: "/api/user/searchbyid",
                    data: QueryString.stringify({ id: this.user.id }),
                    withCredentials: true,
                }).then(response => {
                    console.log(response.data);
                    this.user = {};
                    this.user={
                        id: response.data.id, username: response.data.username,isLoggedIn:response.data.isLoggedIn,
                        phoneNumber: response.data.phoneNumber, description: response.data.description,reviews:response.data.comments
                    };
                })
                .catch(error => {
                    console.log(error);
                });
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

.box{
  box-shadow: 0 0 25px #909399;
  background-color:rgba(0,0,0,0.6);
}
</style>
