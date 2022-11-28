[toc]

# MONGODB


> 注意：$是显示问题，请忽略反斜杠(pycharm中)

## NOSQL and SQL

+ NoSql：非关系型数据库，不仅仅是关系型数据库
  > 存储灵活，读取性能高，易扩展   
  > 数据重复
+ Sql：关系型数据库
+ MongoDB MySQL Redis 区别和使用场景
  - MySQL 是关系型数据库，支持事务
  - MongoDB Redis 非关系型数据库，不支持事务
    1. 希望速度快的时候，选择MongoDB或者Redis
    2. 数据量过大的时候，选择频繁使用的数据存入Redis，其他数据存入MongoDB
    3. MongoDB不用提前建表建数据库，使用方便，字段数量不确定的时候使用MongoDB
    4. 后续需要用到数据之间的关系，考虑MySQL
  
+ 爬虫数据去重
  - 使用数据库建立关键字段（一个或多个）建立索引进行去重
  - 根据url地址进行去重
    1. 使用场景：url对应的数据不会改变
    2. url存在redis中
    3. 拿到url地址，判断url在Redis的URL的集合中是否存在
  - 布隆过滤器
    1. 使用多个加密算法得到多个值，
    2. 将对应位置设置为1
    3. 通过判断对应位置的值，来判断URL是否抓取过
  
+ 根据数据本省进行去重
  - 选择特定的字段，使用加密算法（md5,sha1）将字段进行加密生成字符串，存入Redis
  - 如果后续新来的数据，加密后的字符串存在于Redis集合中，即数据存在，进行更新，否则插入数据

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
  手动创建集合
  - options = {capped:True, size:10}  
  - capped: 默认为fault表示不设置上限，true表示设置上   
  - size: 上限大小，超出上限时，会将之前的数据删除，单位：`字节`

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
  > db.test1.insert({_id:1000,name:'ming',age:30})
  WriteResult({
      "nInserted" : 0,
      "writeError" : {
          "code" : 11000,
          "errmsg" : "E11000 duplicate key error collection: test.test1 index: _id_ dup key: { _id: 1000.0 }"
      }
  })
  > db.test1.find()
  { "_id" : 1000, "name" : "xiao", "age" : 20 }
  
  # _id存在执行更新操作
  > db.test1.save({_id:1000,name:'ming',age:30})
  WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
  > db.test1.find()
  { "_id" : 1000, "name" : "ming", "age" : 30 }
  ```
  
+ 更新：db.collection_name.update(`<query>`,`<update>`,`{multi:<boolean>`})
  - query:查询条件  
  - update：更新操作  
  - multi：可选，默认为`fault`只更新第一条记录，`true`更新所有满足条件的文档
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
  
  # 删除某一字段{$unset{}}
  db.CheXing_2096.updateMany({},{$unset:{'properties.BaoHanTaoTu_36123':1,'properties.TuPian_new_36113':1}})
  
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
  - 删除，默认情况为删除满足条件的所有数据   
  - justOne:只删除一条
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
+ 更新field($rename)

  ```shell
  {
  	_id:1
  	name:{
  		firstname:a
  		secondname:b
  	}
  }
  
  # 将name改为name1,更改单条
  db.collection.update({_id:1},{$rename:{name:name1}})
  
  # 更改collection中的全部
db.collection.updateMany({},{$rename:{name:name1}})
  
  # 更改多层属性
  db.collection.updateMany({},{$rename:{'name.firstname':'name.fname'}}
  
  # 当更改的字段不存在于collection中时，该操作符不做任何事情
  
  ```
  
  

#### 查询

+ 查询db.collection_name.find(`<query>`)
  - findOne()：查询，只返回第一个  
  - .pretty()：将结果格式化  
  - .limit()：限定数量  
  - .skip()：跳过指定数量`limit和skip顺序可以交换，建议先skip`  
  - .sort()：排序`1升序 -1降序`  
  - .count()：数量
  - .distinct()：消除重复
  - 投影：控制返回字段 db.collection_name.find({},{`字段：1`})
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
  - 等于：默认
  - 小于：$lt
  - 小于等于：$lte
  - 大于：$gt
  - 大于等于：$gte
  - 不等于：$ne
  - 范围：$in
  - not范围：$nin
  ```shell
  db.stu.find({age:{$lte:18}})
  db.stu.find({age:{$in:[18,28,38]}})
  ```
+ 逻辑运算符
  - and：多个条件即可
  - or：$or,值为数组，数组中每个元素为json
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
    {$group:{_id:	                   {country:'$country',province:'$province',userid:'$userid'}}},
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

+ $out:将结果存储到新的collection

  `会清空new collection中已有的数据，并且复制结果集的索引到新的集合中`

  ```shell
  db.collection.aggregate(
    [
      {$match:{}},
      {$out:'new collection'}
    ]
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




### 索引

> 提升查询速度

+ 建立索引
db.collection_name.ensureIndex({属性：1},{'unique':true})
  - `1`表示升序，`-1`表示降序
  - unique可选，表示索引值唯一
    1. 使用数据库建立关键字的唯一索引进行去重
  
  ```shell
  > for(i=0;i<100000;i++){
      db.t255.insert({name:'test'+i,age:i})
    }
  WriteResult({ "nInserted" : 1 })
  > db.t255.count()
  100000
  
  # .explain('executionStats') 查询状态
  > db.t255.find({name:'test10000'}).explain('executionStats')
  {
      "queryPlanner" : {
          "plannerVersion" : 1,
          "namespace" : "test.t255",
          "indexFilterSet" : false,
          "parsedQuery" : {
              "name" : {
                  "$eq" : "test10000"
              }
          },
          "winningPlan" : {
              "stage" : "COLLSCAN",
              "filter" : {
                  "name" : {
                      "$eq" : "test10000"
                  }
              },
              "direction" : "forward"
          },
          "rejectedPlans" : [ ]
      },
      "executionStats" : {
          "executionSuccess" : true,
          "nReturned" : 1,
          "executionTimeMillis" : 43,  # 查询时间
          "totalKeysExamined" : 0,
          "totalDocsExamined" : 100000,
          "executionStages" : {
              "stage" : "COLLSCAN",
              "filter" : {
                  "name" : {
                      "$eq" : "test10000"
                  }
              },
              "nReturned" : 1,
              "executionTimeMillisEstimate" : 2,
              "works" : 100002,
              "advanced" : 1,
              "needTime" : 100000,
              "needYield" : 0,
              "saveState" : 100,
              "restoreState" : 100,
              "isEOF" : 1,
              "direction" : "forward",
              "docsExamined" : 100000
          }
      },
      "serverInfo" : {
          "host" : "h-job.local",
          "port" : 27017,
          "version" : "4.4.3",
          "gitVersion" : "913d6b62acfbb344dde1b116f4161360acd8fd13"
      },
      "ok" : 1
  }
  
  # 建立索引
  > db.t255.ensureIndex({name:1})
  {
      "createdCollectionAutomatically" : false,
      "numIndexesBefore" : 1,
      "numIndexesAfter" : 2,
      "ok" : 1
  }
  
  {
      "queryPlanner" : {
          "plannerVersion" : 1,
          "namespace" : "test.t255",
          "indexFilterSet" : false,
          "parsedQuery" : {
              "name" : {
                  "$eq" : "test10000"
              }
          },
          "winningPlan" : {
              "stage" : "FETCH",
              "inputStage" : {
                  "stage" : "IXSCAN",
                  "keyPattern" : {
                      "name" : 1
                  },
                  "indexName" : "name_1",
                  "isMultiKey" : false,
                  "multiKeyPaths" : {
                      "name" : [ ]
                  },
                  "isUnique" : false,
                  "isSparse" : false,
                  "isPartial" : false,
                  "indexVersion" : 2,
                  "direction" : "forward",
                  "indexBounds" : {
                      "name" : [
                          "[\"test10000\", \"test10000\"]"
                      ]
                  }
              }
          },
          "rejectedPlans" : [ ]
      },
      "executionStats" : {
          "executionSuccess" : true,
          "nReturned" : 1,
          "executionTimeMillis" : 5,  # 查询速度提高
          "totalKeysExamined" : 1,
          "totalDocsExamined" : 1,
          "executionStages" : {
              "stage" : "FETCH",
              "nReturned" : 1,
              "executionTimeMillisEstimate" : 0,
              "works" : 2,
              "advanced" : 1,
              "needTime" : 0,
              "needYield" : 0,
              "saveState" : 0,
              "restoreState" : 0,
              "isEOF" : 1,
              "docsExamined" : 1,
              "alreadyHasObj" : 0,
              "inputStage" : {
                  "stage" : "IXSCAN",
                  "nReturned" : 1,
                  "executionTimeMillisEstimate" : 0,
                  "works" : 2,
                  "advanced" : 1,
                  "needTime" : 0,
                  "needYield" : 0,
                  "saveState" : 0,
                  "restoreState" : 0,
                  "isEOF" : 1,
                  "keyPattern" : {
                      "name" : 1
                  },
                  "indexName" : "name_1",
                  "isMultiKey" : false,
                  "multiKeyPaths" : {
                      "name" : [ ]
                  },
                  "isUnique" : false,
                  "isSparse" : false,
                  "isPartial" : false,
                  "indexVersion" : 2,
                  "direction" : "forward",
                  "indexBounds" : {
                      "name" : [
                          "[\"test10000\", \"test10000\"]"
                      ]
                  },
                  "keysExamined" : 1,
                  "seeks" : 1,
                  "dupsTested" : 0,
                  "dupsDropped" : 0
              }
          }
      },
      "serverInfo" : {
          "host" : "h-job.local",
          "port" : 27017,
          "version" : "4.4.3",
          "gitVersion" : "913d6b62acfbb344dde1b116f4161360acd8fd13"
      },
      "ok" : 1
  }
  ```

+ db.collection_name.getIndexes()
查看所有索引
  
  ```shell
  > db.t255.getIndexes()
  [
      {
          "v" : 2,
          "key" : {
              "_id" : 1
          },
          "name" : "_id_"
      },
      {
          "v" : 2,
          "key" : {
              "name" : 1
          },
          "name" : "name_1"
      }
  ]
  ```

+ db.collection_name.ensureIndex({name:1,age:1})  
联合索引  
> 通过联合索引确定数据的唯一性

+ db.collection_name.dropIndex('索引名称')
删除索引
  

### 实践

+ count
1. `db.collection.countDocuments(filter_condition)`
2. count
   ```
   db.collection.aggregate(
   [
   {$match:filter_condition},
   {$count:'number'}
   ]
   )
   ```
3. count
   ```
   db.colletcion.aggregate(
   [
   {$match:filter_condition},
   {$group:{_id:null,count:{$sum:1}}},
   {$project:{_id:0}}
   ]
   )
   ```
4. 收集id,批量删除
    ```shell
    var ids=[]
    db.CheXing_2096.find(
       {'properties.ChanPinKuId_36095':{$exists:0},'properties.CheXingMingCheng_35936':{$exists:0}}
    ).forEach(function(doc){
        ids.push({
                'deleteOne':{'filter':{'_id':doc._id}}
            })
        })
    print(ids)
    db.CheXing_2096.bulkWrite(ids)
    db.CheXing_2096_Meta.bulkWrite(ids)
    ```
   
5. 关联查询，循环删除
    ```shell
    db.CheXing_2096.aggregate(
    [
        {$lookup:{
            "localField": "_id",
            "from": 'CheXing_2096_Meta',
            "foreignField": "_id",
            "as": "Meta"
            }},
        {$match:{'Meta':{$size:0}}},
        {$project:{_id:1}}
    ]
    ).forEach(function(doc){
        db.CheXing_2096.deleteOne({_id:doc._id})
        })
    ```
   
6. 循环更新

    ```shell
    var op = []
    db.TuPian_2734.aggregate(
    [
    {$match:{'properties.SuoShuTaoTu4_43775':{$exists:1}}},
    {$match:{'properties.SuoShuTaoTu4_43775':{$type:4}}},
    {$project:{_id:1,'properties.SuoShuTaoTu4_43775':1}},
    ]
    ).forEach(
    function(doc){
        op.push(
        {
            'updateOne':{'filter':{'_id':doc._id},'update':{'$set':{'properties.SuoShuTaoTu4_43775':doc.properties.SuoShuTaoTu4_43775[doc.properties.SuoShuTaoTu4_43775.length-1]}}}
        }
        )
    }  
    )
    db.TuPian_2734.bulkWrite(op)
    ```
7. 连接查询

    ```shell
    db.TaoTu2_2175.aggregate(
        [
            {$lookup:{
                from:'TuPian_2100',
                localField:'properties.BaoHanTuPian2_36687', 
                foreignField:'_id', # TaoTu2_2175.properties.BaoHanTuPian2_36687=TuPian_2100._id
                as:'tupian'
                }},
             {$unwind:'$tupian'},
             {$project:{_id:1,pic_id:'$tupian._id',difference:{$eq:['$tupian.properties.SuoShuTaoTu4_36362','$_id']}}},
             {$match:{difference:true}}, # TuPian_2100.properties.SuoShuTaoTu4_36362 = TaoTu2_2175._id
             {$limit:10000}
        ]
    )
    ```
   
8. 列表插入数据
    ```javascript
    var op = []
    db.GuPiaoRiHangQing_2530.aggregate(
    [
        {$lookup:{
            from:'GuPiao1_2527',
            localField:'properties.GuPiao_39608', 
            foreignField:'_id', 
            as:'GuPiao'
            }},
        {$unwind:'$GuPiao'},
        {$project:{_id:1,'properties.RiQi_39156':1,'gupiao':'$GuPiao._id','rihangqing':'$GuPiao.properties.GuPiaoRiHangQing_39609','difference':{$in:['$_id','$GuPiao.properties.GuPiaoRiHangQing_39609']}}},
        {$match:{'difference':false}}
    ]
    ).forEach(
        function(doc){
            op.push(
            {
                'updateOne':{'filter':{'_id':doc.gupiao},'update':{'$push':{'properties.GuPiaoRiHangQing_39609':doc._id}}}
            }
            );
            if(op.length >= 1000){
                db.GuPiao1_2527.bulkWrite(op);
                print(op);
                op = [];
                }
        })
        if(op.length > 0){
            print(op);
            db.GuPiao1_2527.bulkWrite(op);
            }
    ```
   
9. 连接条件查询
```javascript
db.data_review_log.aggregate([
{$match:{concept_id:80,task_id:3,update_time:{$gt:new Date('2021-07-16')}}},
{$sort:{update_time:-1}},
{$group:{_id:'$entity_id',update_time:{$first:'$update_time'},count:{$sum:1}}},
{$lookup:{
    from:'data_review_log',
    let:{entity_id:'$_id',update_time:'$update_time'},
    pipeline: [
              { $match:
                 { $expr:
                    { $and:
                       [
                         { $eq: [ "$entity_id",  "$$entity_id" ] },
                         { $gt: [ "$update_time", "$$update_time" ] }
                       ]
                    }
                 }
              }
           ],
     as: "log_data"
    }},
   {$project:{_id:1,log_data:1,log_size:{$size:'$log_data'}}},
   {$match:{log_size:{$gte:1}}},
//    {$group:{_id:null,count:{$sum:1}}}
   {$unwind:'$log_data'},
   {$group:{_id:'$log_data.task_id'}},
   {$sort:{_id:-1}}
])
```