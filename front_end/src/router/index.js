//导入方法
import {createRouter, createWebHashHistory} from "vue-router";
import mainView from "@/views/MainView.vue";
import enrollView from "@/views/EnrollView.vue";
import loginView from "@/views/LoginView.vue"
import changepassView from "@/views/ChangePassView.vue"
import historyOrderView from "@/views/HistoryOrderView.vue"
import userManageView from "@/views/UserManage.vue"
import homeView from "@/views/HomeView.vue"
import historyOrder from "@/views/HistoryOrders.vue"
import chatView from "@/views/ChatPageView.vue"
//创建路由实例
const loginRoutes = [
    {
        path: "/",
        redirect: "/usermanage"
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
    },
    {
        path: "/history",
        name: "history",
        component: historyOrderView
    },
    {
        path: "/historyorder",
        name: "historyorder",
        component: historyOrder
    },
    {
        path: "/usermanage",
        name: "usermanage",
        component: userManageView
    },
    {
        path: "/home",
        name: "home",
        component: homeView
    },
    {
        path: "/chat",
        name: "chat",
        component: chatView
    }
]
//用于在main.js导入的默认配置
export const loginRouter = createRouter({
    history: createWebHashHistory(),
    routes: loginRoutes
})
