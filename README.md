# accountbook_server

> account book server project

## 安装运行步骤

### 1. 创建虚拟环境并安装依赖
``` bash
$ pipenv install
```

### 2. 运行虚拟环境
``` bash
$ pipenv shell
```

### 3. 创建数据库并执行迁移
启动`MySQL`服务, 创建数据库`accountbook`:
``` sql
CREATE DATABASE accountbook DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
```
检查数据库连接配置, 执行建表迁移:
``` bash
$ python manage.py migrate
```

### 4. 运行服务
``` bash
$ python manage.py runserver
```
