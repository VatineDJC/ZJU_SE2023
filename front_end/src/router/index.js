//导入方法
import {createRouter, createWebHashHistory} from "vue-router";
import mainView from "@/views/MainView.vue";
import enrollView from "@/views/EnrollView.vue";
import loginView from "@/views/LoginView.vue"
import changepassView from "@/views/ChangePassView.vue"

//创建路由实例
const loginRoutes = [
    {
        path: "/",
        redirect: "/login"
    },
    {
        path: "/enroll",
        name:"enroll",
        component: enrollView
    },
    {
        path: "/login",
        name: "login",
        component: loginView
    },
    {
        path: "/main",
        name: "main",
        component: mainView
    }
        ,
    {
        path: "/changepwd",
        name: "changepwd",
        component: changepassView
    }
]
//用于在main.js导入的默认配置
export const loginRouter = createRouter({
    history: createWebHashHistory(),
    routes: loginRoutes
})
