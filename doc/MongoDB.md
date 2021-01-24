# MONGODB


> 注意：$是显示问题，请忽略反斜杠(pycharm中)

## NOSQL and SQL

+ NoSql：非关系型数据库，不仅仅是关系型数据库
  > 存储灵活，读取性能高，易扩展   
  > 数据重复
+ Sql：关系型数据库

## 服务

- 启动：mongod --config /usr/local/etc/mongod.conf --fork
- mongodb shell: mongo host:port/db
  > shell是一个功能文完备的JavaScript解释器   
  > 参数 mongo --nodb 不连接到任何数据库
  > --norc 禁止加载.mongorc.js
  > conn = new Mongo("host:port") 连接到想要的mongod
- 关闭：在shell中
  db.adminCommand({"shutdown":1})
  > 
- 备份  
  mongodump -h dbhost -d dbname -o dbdirectory  
  > -h：服务器地址，也可以指定端口号  
  > -d：需要备份的数据库名称  
  > -o：备份数据存放的位置  
  ```shell
  mongodump -h localhost:27017 -d test1 -o ~/Desktop/test.bak
  ```
  
- 恢复  
  mongorestore -d test1 --dir test
  > -d：目标数据库地址  
  > --dir：备份文件
## 数据类型

- null：空值或者不存在
- 布尔(Boolean)：ture false
- 数字(Integer): 默认使用64位浮点型数值
  > 整型可以使用NumberInt类（表示4字节带符号整数）  
  > NumberLong(表示8字节带符号整数)
- 字符串(string)：UTF-8
- 日期：毫秒数 new Date(), 对应datetime.datetime
- timestamp：时间戳
- 正则表达式：{"x":/foobar/i}
- 数组(Arrays)：多个值存储到一个键
- 内嵌文档
- 对象id：Object ID，文档属性_id，保证文档唯一性
  > 12字节16进制数
- 二进制数据
- 代码：JavaScript代码

## 定制shell

### shell初始化脚本

> 在用户主目录下创建 .mongorc.js文件

### prompt变量

>
>

## 命令

> `db`表示当前数据库

### database

+ show databases
  > 查看当前数据库
+ use db_name
  > 使用某个数据库
+ db
  > 查看当前数据库
+ db.dropDatabase()
  > 删除当前数据库

### 集合

+ db.createCollection(name, options)
  > 手动创建集合
  > options = {capped:True, size:10}  
  > capped: 默认为fault表示不设置上限，true表示设置上   
  > size: 上限大小，超出上限时，会将之前的数据删除，单位：`字节`

+ show collections
  > 查看集合
+ db.collection_name.drop()
  > 删除集合
### 文档

#### 增删改

+ 插入：db.collection_name.insert(data)   
  ```shell
  db.test1000.insert({name:'xiaohong',age:20})
  ```
+ 保存：db.collection_name.save(data)
  ```shell
  > db.test1.insert({_id:1000,name:'xiao',age:20})
  WriteResult({ "nInserted" : 1 })
  # _id存在报错
  db.test1.insert({_id:1000,name:'ming',age:30})
  WriteResult({
      "nInserted" : 0,
      "writeError" : {
          "code" : 11000,
          "errmsg" : "E11000 duplicate key error collection: test.test1 index: _id_ dup key: { _id: 1000.0 }"
      }
  })
  db.test1.find()
  { "_id" : 1000, "name" : "xiao", "age" : 20 }
  
  # _id存在执行更新操作
  db.test1.save({_id:1000,name:'ming',age:30})
  WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
  db.test1.find()
  { "_id" : 1000, "name" : "ming", "age" : 30 }
  ```
  
+ 更新：db.collection_name.update(`<query>`,`<update>`,`{multi:<boolean>`})
  > 更新  
  > query:查询条件  
  > update：更新操作  
  > multi：可选，默认为`fault`只更新第一条记录，`true`更新所有满足条件的文档
  ```shell
  > db.test1.find()
  { "_id" : 1000, "name" : "ming", "age" : 30 }
  
  # 替换
  > db.test1.update({name:'ming'},{name:'hong'})
  WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
  > db.test1.find()
  { "_id" : 1000, "name" : "hong" }
  > db.test1.update({name:'hong'},{name:'ming',age:18})
  WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
  > db.test1.find()
  { "_id" : 1000, "name" : "ming", "age" : 18 }
  
  # 更新单一字段{$set{}}
  > db.test1.update({name:'ming'},{$set:{name:'hong'}})
  WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
  > db.test1.find()
  { "_id" : 1000, "name" : "hong", "age" : 18 }
  
  > db.test1.find()
  { "_id" : 1000, "name" : "hong", "age" : 18 }
  { "_id" : ObjectId("600d5d184859990197b20c86"), "name" : "hong", "age" : 30 }
  { "_id" : ObjectId("600d5d1e4859990197b20c87"), "name" : "hong", "age" : 31 }
  { "_id" : ObjectId("600d5d204859990197b20c88"), "name" : "hong", "age" : 32 }
  > db.test1.update({name:'hong'},{$set:{name:'ming'}})
  WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
  > db.test1.find()
  { "_id" : 1000, "name" : "ming", "age" : 18 }
  { "_id" : ObjectId("600d5d184859990197b20c86"), "name" : "hong", "age" : 30 }
  { "_id" : ObjectId("600d5d1e4859990197b20c87"), "name" : "hong", "age" : 31 }
  { "_id" : ObjectId("600d5d204859990197b20c88"), "name" : "hong", "age" : 32 }
  
  # {multi:true}更新所有满足条件的文档
  > db.test1.update({name:'hong'},{$set:{name:'ming'}},{multi:true})
  WriteResult({ "nMatched" : 3, "nUpserted" : 0, "nModified" : 3 })
  > db.test1.find()
  { "_id" : 1000, "name" : "ming", "age" : 18 }
  { "_id" : ObjectId("600d5d184859990197b20c86"), "name" : "ming", "age" : 30 }
  { "_id" : ObjectId("600d5d1e4859990197b20c87"), "name" : "ming", "age" : 31 }
  { "_id" : ObjectId("600d5d204859990197b20c88"), "name" : "ming", "age" : 32 }
  ```
+ 删除：db.collection_name.remove(`<query>`,`<justOne:boolean>`)
  > 删除，默认情况为删除满足条件的所有数据   
  > justOne:只删除一条
  ```shell
  > db.test1.find()
  { "_id" : 1000, "name" : "ming", "age" : 18 }
  { "_id" : ObjectId("600d5d184859990197b20c86"), "name" : "ming", "age" : 30 }
  { "_id" : ObjectId("600d5d1e4859990197b20c87"), "name" : "ming", "age" : 31 }
  { "_id" : ObjectId("600d5d204859990197b20c88"), "name" : "ming", "age" : 32 }
  > db.test1.remove({name:'ming'},{justOne:true})
  WriteResult({ "nRemoved" : 1 })
  > db.test1.find()
  { "_id" : ObjectId("600d5d184859990197b20c86"), "name" : "ming", "age" : 30 }
  { "_id" : ObjectId("600d5d1e4859990197b20c87"), "name" : "ming", "age" : 31 }
  { "_id" : ObjectId("600d5d204859990197b20c88"), "name" : "ming", "age" : 32 }
  > db.test1.remove({name:'ming'})
  WriteResult({ "nRemoved" : 3 })
  > xdb.test1.find()
  >
  ```
#### 查询
+ 查询db.collection_name.find(`<query>`)
  > findOne()：查询，只返回第一个  
  > .pretty()：将结果格式化  
  > .limit()：限定数量  
  > .skip()：跳过指定数量`limit和skip顺序可以交换，建议先skip`  
  > .sort()：排序`1升序 -1降序`  
  > .count()：数量
  > .distinct()：消除重复
  > 投影：控制返回字段 db.collection_name.find({},{`字段：1`})
  ```shell
  # 查询全部
  db.products.find({})
  
  # 查询一条
  db.products.findOne()
  
  # 格式化输出
  db.products.find().pretty()
  
  # 分页
  db.products.find().limit(4)
  db.products.find().skip(2).limit(3)
  
  # 排序
  db.products.find().sort({age:1})
  db.products.find().sort({age:-1})
  db.products.find().sort({age:-1,gender:-1})
  
  统计
  db.stu.count()
  db.stu.count({age:{$gt:18}})
  db.stu.find({name:'a'}).count()
  
  # 消除重复
  # {age:{$gt:18}}筛选条件
  db.stu.distinct('hometown',{age:{$gt:18}})
  
  # 投影
  # {_id:0,name:1} 
  # 显示字段设置为1，不显示字段不写，_id不显示需要设置为0
  db.stu.find({age:{$gt:18}},{_id:0,name:1})
  ```
  
+ 条件运算符
  1. 等于：默认
  2. 小于：$lt
  3. 小于等于：$lte
  4. 大于：$gt
  5. 大于等于：$gte
  6. 不等于：$ne
  7. 范围：$in
  8. not范围：$nin
  ```shell
  db.stu.find({age:{$lte:18}})
  db.stu.find({age:{$in:[18,28,38]}})
  ```
+ 逻辑运算符
  1. and：多个条件即可
  2. or：$or,值为数组，数组中每个元素为json
  ```shell
  # and
  db.stu.find({age:18,name:'huang'})
  
  # or 
  db.stu.find({$or:[{age:{$gte:16}},{name:{$in:['huang','ming']}}]})
  ```
  
+ 正则表达式
  > 使用//或$regex编写
  ```shell
  db.products.find({sku:/^abc/})
  db.products.find({sku:{$regex:'789$'}})
  ```
+ 自定义查询
  > $where
  ```shell
  db.stu.find({
      $where:function(){
        return this.age>30}
  })
  ```
  




### 聚合（aggregate）

> 聚合（aggregate）是基于数据处理的聚合管道，每个文档通过一个由多个阶段（stage）组成的管道，可以对每个阶段的管道进行分组、过滤等功能，然后经过一系列的处理，输出相应的结果。  
db.collection_name.aggregate({`管道`:{`表达式`}})
> 
管道
+ $group：分组，用于统计结果  
  - _id表示分组的依据，使用某个字段的格式为'$字段'
  - `$group`对应的字典中有几个键，结果中就有几个键
  - 分组依据需要放在`_id`后面
  - 去不同的字段的值需要使用`$`
  - 去字典嵌套的字典中的值得时候`$_id.country`
  - 能够同时按多个键进行分组`{$group:{_id:{country:'$country',province:'$province',userid:'$userid'}}}`
  ```shell
  # 按照gender进行分组，获取不同组数据的个数和平均年龄
  db.stu.aggregate(
      {$group:{
        _id:'$gender',
        count:{$sum:1},
        avg_age:{$avg:'$age'}}}
  )
  
  # 按照hometown进行分组，获取平均年龄
  db.stu.aggregate(
      {$group:{_id:'hometown',
               mean_age:{$avg:'$age'}}}
  )
  
  # _id:null 将集合中所有文档分为一组
  db.stu.aggregate(
    {$group:{_id:null,
             count:{$sum:1},
             mean_age:{$avg:'$age'}}}
  )
  
  db.tv3.aggregate(
  # 对多个字段进行分组,可以用来去重
    {$group:{_id:{country:'$country',province:'$province',userid:'$userid'}}},
    {$group:{_id:{country:'$_id.country',province:'_id.province'},count:{$sum:1}}},
    {$project:{_id:0,country:'$_id.country',province:'_id.province',count:1}}
  )
  ```
+ $match：过滤数据
  ```shell
  # 选择年龄大于20的学生，统计男性和女性的数量
  db.stu.aggregate(
      {$match:{age:{$gt:20}},
       $group:{_id:'$gender',count:{$sum:1}},
       $project:{_id:0,gender:'$_id',count:1}}
  )
  ```
+ $project：修改输入文档的结构，如重命名、增加、删除字段、创建计算结果
  ```shell
  db.stu.aggregate(
    {$group:{
      _id:'$gender',
      count:{$sum:1},
      avg_age:{$avg:'$age'}}},
    {$project:{
      _id:0   # 不显示_id
      gender:'$_id',
      count:1,
      avg_age:1}}
  )
  ```
+ $sort：排序
  ```shell
  db.stu.aggregate({$sort:{age:1}})
  db.stu.aggregate(
      {$group:{_id:'$gender',count:{$sum:1}}},
      {$sort:{count:-1}}
  )
  ```
+ $limit：限制文档数量
+ $skip：跳过指定的文档数量
  ```shell
  db.stu.aggregate(
    {$group:{_id:'$gender',counter:{$sum:1}}},
    {$sort:{counter:1}},
    {$skip:1},
    {$limit:1}
  )
  ```
+ $unwind：将数组类型的字段进行拆分
  ```shell
  > db.t2.insert({_id:1,item:'t-shirt',size:['S','M','L']})
  WriteResult({ "nInserted" : 1 })
  > db.t2.aggregate({$unwind:'$size'})
  { "_id" : 1, "item" : "t-shirt", "size" : "S" }
  { "_id" : 1, "item" : "t-shirt", "size" : "M" }
  { "_id" : 1, "item" : "t-shirt", "size" : "L" }
  
  # preserveNullAndEmptyArrays 防止空白数据丢失
  > db.inventory.aggregate(
      {$unwind:{path:'$size',preserveNullAndEmptyArrays:true}}
  )
  ```


表达式
> 表达式:'$列名'
+ $sum：计算总和，$sum:1 表示以一倍计数
+ $avg：平均值
+ $min：最小值
+ $max：最大值
+ $push：在结果文档中插入值到一个数组中
+ $first：根据文档的排序获取第一个文档数据
+ $last：获取最后一个文档数据