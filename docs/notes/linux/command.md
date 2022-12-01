# command
## xargs
### example
xargs命令是给其他命令传递参数的一个过滤器，也是组合多个命令的一个工具。
```shell
redis-cli -n "db" -h 'host' -p 'port' -a 'password' keys '*' 
| xargs redis-cli -n "db" -h 'host' -p 'port' -a 'password' del
```
- 将前一阶段的结果作为参数传入`xargs`后的命令中

## grep
### usage

- `-r` or `-R` is recursive,
- `-n` is line number, and
- `-w` stands for match the whole word.
- `-l` (lower-case L) can be added to just give the file name of matching files.
- `-e` is the pattern used during the search
-  `--exclude` 
- `--include`
- `--exclude-dir`

### example

+ 查找目录下.log文件内包含的指定内容

```bash
# grep include *.log recursice line 
grep --include=\*.log -rnw . -e 'REQ_ID:d0b65340-c57c-4159-b2c3-c2eaa7ef6675'
```
