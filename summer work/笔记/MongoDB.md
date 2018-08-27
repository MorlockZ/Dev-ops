## 初步学习MongoDB
#### 什么是MongoDB？
MongoDB 将数据存储为一个文档，数据结构由键值(key=>value)对组成。MongoDB 文档类似于 JSON 对象。字段值可以包含其他文档，数组及文档数组。
#### MongoDB的下载与启动
1. 下载MongoDB 
>apt-get install mongodb
2. systemctl stop mongodb 关闭mongodb服务
3. systemctl disable mongodb 关闭mongodb的自启动
4. systemctl start mongodb 启动mongodb 服务
5. 启动：
      1. 输入tmux，进入页面输入mongod --dbpath /path，Ctrl+b+d，保存及退出。
      2. 命令行模式：mongo，即可正式运行

#### Mongo 基本使用
1. 创建库
>use +名字

2. 创建表
  
  db.createCollection("名字")
  >{"ok":1}

3. 修改数据表名

db.Account.renameCollection("Account1")
>{ "ok" : 1 }

4. 查看全部表记录
 db.Account.find()
>{ "_id" : ObjectId("4df08553188e444d001a763a"), "AccountID" : 1, "UserName" : "libing", "Password" : "1", "Age" : 26, "Email" : "libing@126.com", "RegisterDate" : "2011-06-09 16:31:25" }
{ "_id" : ObjectId("4df08586188e444d001a763b"), "AccountID" : 2, "UserName" : "lb", "Password" : "1", "Age" : 25, "Email" : "libing@163.com", "RegisterDate" : "2011-06-09 16:36:95" }
 
5. 在 MongoDB 中，你不需要创建集合。当你插入一些文档时，MongoDB 会自动创建集合。

> db.mycol2.insert({"name" : "菜鸟教程"})

6. 添加多个字段
>db.zww.insert({"name":"zhangsan","age":18})

7. 查询出来的数据转化为json。
t = json.dumps(r, ensure_ascii=False) 
如果不加 ensure_ascii=False  输出的 t 如果有汉字的话都默认给转换成一堆编码 如果加上的话 就都能正常显示变成了汉字



