# MONGODB

## 服务

- 启动：mongod --config /usr/local/etc/mongod.conf --fork
- mongodb shell: mongo host:port/db
  > shell是一个功能文完备的JavaScript解释器   
  > 参数 mongo --nodb 不连接到任何数据库
  > --norc 禁止加载.mongorc.js
  > conn = new Mongo("host:port") 连接到想要的mongod
- 关闭：在shell中
  > db.adminCommand({"shutdown":1})
  
## 数据类型

- null：空值或者不存在
- 布尔：ture false
- 数字: 默认使用64位浮点型数值
  > 整型可以使用NumberInt类（表示4字节带符号整数）  
  > NumberLong(表示8字节带符号整数)
- 字符串：UTF-8
- 日期：毫秒数 new Date()  
- 正则表达式：{"x":/foobar/i}
- 数组   
- 内嵌文档
- 对象id
- 二进制数据
- 代码：JavaScript代码

## 定制shell

### shell初始化脚本
> 在用户主目录下创建 .mongorc.js文件

### prompt变量
> 