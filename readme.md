## 使用说明

### 数据库使用方法

db_scripts包含了所有数据库表文件和trigger的原始代码，直接复制粘贴到mysql中执行即可。

### 后端使用方法

```bash
python3 app.py
```

后端基于python的flask，使用上述命令运行即可

后端的ip与端口在app.py中更改后可以正常运行，数据库连接位置在src/database.py中更改才可正常运行

### 前端使用方法

```bash
npm install # 安装依赖，只有首次运行时需要
npm run dev # 基于源码直接运行
npm run build # 打包为静态内容并运行
```

前端基于vite+vue3工具链，使用上述命令运行前端服务

前端的ip端口与后端API的连接位置在vite.config.js中更改。