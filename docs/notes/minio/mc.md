# minIO client



## Install

```bash
wget https://dl.min.io/client/mc/release/linux-amd64/mc
chmod +x mc
mc alias set myminio/ http://MINIO-SERVER MYUSER MYPASSWORD
```

## Lifecycle

```bash
# 增加规则
mc ilm add --expiry-days 90 myminio/ksc
# 查看规则
mc ilm ls myminio/ksc
# 修改规则
mc ilm edit --id "c79ntj94b0t6rukh6lr0" --expiry-days 90  myminio/ksc
# 删除规则
mc ilm rm --id "bgrt1ghju" myminio/mydata
# 导出规则
mc ilm export myminio/ksc > minio_mc_rule.json
# 导入规则
mc ilm import myminio/mybucket < bucket-lifecycle.json
# 查看状态
mc stat myminio/gmobile/ff3a2ef68fb0b30e1e5bcb544c372f04
# 查看动作
mc watch --recursive myminio/gmobile
```

## admin

### scanner

```bash
# 查看扫描状态
mc admin scanner status myminio/
```

### trace

```bash
# 查看日志
mc admin trace -a myminio
```

