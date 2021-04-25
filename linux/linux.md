### 命令
#### xargs
xargs命令是给其他命令传递参数的一个过滤器，也是组合多个命令的一个工具。
```shell
redis-cli -n "db" -h 'host' -p 'port' -a 'password' keys '*' 
| xargs redis-cli -n "db" -h 'host' -p 'port' -a 'password' del
```
- 将前一阶段的结果作为参数传入`xargs`后的命令中