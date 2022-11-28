# Shell Command

## tar

> 压缩

```sh
tar -czvf file.tar.gz directory
```

> 解压

```sh
tar -xzvf projects.tar.gz -C /tmp/
```

## sort

>结果排序

```sh
# -n 按照大小顺序排列  -k 2 根据第二列
ps -ef | sort -n -k 2
```

## grep

> 筛选结果

