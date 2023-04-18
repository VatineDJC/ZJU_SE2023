import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path';

export default defineConfig({
    plugins: [vue()],
    resolve: {
        alias: {
            "@": path.resolve(__dirname, "src"),
            "comps": path.resolve(__dirname, "src/components"),
        },
    },
    css:{},
    server: {
        proxy: {
            // 接口地址代理
            '/api': {
                target: 'http://0.0.0.0:8886', // 接口的域名
                secure: false, // 如果是https接口，需要配置这个参数
                changeOrigin: true, // 如果接口跨域，需要进行这个参数配置
                rewrite: path => path.replace(/^\/api/, '')
            },
        }
    },
    host:"0.0.0.0"
})
