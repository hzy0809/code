## crontab

> 系统定时任务

+ 脚本添加任务

```bash
crontab -l | { cat; echo "10 * * * * echo 'hello'"; } | crontab -
```

### crontab命令

> cron服务提供crontab命令来设定cron服务的，以下是这个命令的一些参数与说明:

+ crontab -u //设定某个用户的cron服务，一般root用户在执行这个命令的时候需要此参数 

+ crontab -l //列出某个用户cron服务的详细内容

+ crontab -r //删除没个用户的cron服务

+ crontab -e //编辑某个用户的cron服务
　　> 比如说root查看自己的cron设置:crontab -u root -l
    再例如，root想删除fred的cron设置:crontab -u fred -r
    在编辑cron服务时，编辑的内容有一些格式和约定，输入:crontab -u root -e
    进入vi编辑模式，编辑的内容一定要符合下面的格式:*/1 * * * * ls >> /tmp/ls.txt
    
+ 任务调度的crond常驻命令
    crond 是**linux**用来定期执行程序的命令。当安装完成操作系统之后，默认便会启动此 任务调度命令。crond命令每分锺会定期检查是否有要执行的工作，如果有要执行的工作便会自动执行该工作。
    
### cron文件语法

        分   小时   日    月    星期   命令
         
        0-59  0-23  1-31  1-12   0-6   command   (取值范围,0表示周日一般一行对应一个任务)

+   记住几个特殊符号的含义:

  `*`代表取值范围内的数字,
  `/`代表”每”,
  `-`代表从某个数字到某个数字,
  `,`分开几个离散的数字

## bash

+ 参数默认值

```bash
echo ${HOME:=/tmp}
```

## find

```bash
# -mtime +30 查找30天谴的文件
# -name "*.txt" 查找后缀为txt的文件
# -exec rm -rf 执行命令
# {} \; 固定写法
# find 目录
find /home/weblogic/rc-server-tomcat-8081/logs -mtime +30 -name "*.txt" -exec rm -rf {} \;
```

