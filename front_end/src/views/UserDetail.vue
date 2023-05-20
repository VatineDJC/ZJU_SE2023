<template>
    <div id='main_image'>
        <Navbar />
        <el-card class = "box">
            <el-row>
                <el-col :span="8">
                    <h3>UID: {{ user.uid }}</h3>
                    <h3>用户名: {{ user.username }}</h3>
                    <h3>登录状态: {{ user.isLoggedIn ? '已登录' : '未登录' }}</h3>
                </el-col>
                <el-col :span="8">
                    <h3>个人信息</h3>
                    <p>{{ user.personalInfo }}</p>
                </el-col>
                <el-col :span="8">
                    <h3>权限组</h3>
                    <ul>
                        <li v-for="group in user.permissionGroups" :key="group.id">
                            {{ group.name }}
                        </li>
                    </ul>
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
                uid: '12345',
                username: 'JohnDoe',
                isLoggedIn: true,
                personalInfo: '用户的个人信息',
                permissionGroups: [
                    { id: 1, name: 'Group A' },
                    { id: 2, name: 'Group B' },
                    { id: 3, name: 'Group C' }
                ],
                reviews: [
                    { user: 'user1', content: '评价1', time: '2023-05-20' },
                    { user: 'user2', content: '评价2', time: '2023-05-21' },
                    { user: 'user3', content: '评价3', time: '2023-05-22' }
                ]
            }
        };
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
