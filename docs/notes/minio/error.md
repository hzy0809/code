# deploy

## run command

```bash
server --console-address ":9001" http://minio{1...4}/data{1...2}
```

+ `http://minio{1...4}/data{1...2}`是一个`server pool`
+ `server pool`定义`minio{1...4}`为四台连续的主机地址，可以通过配置`hosts`文件映射来实现