

## identity

### username&password

+ 记住账号密码  
  `git config --global credential.helper store`
  
+ 清除本地的修改  
  `git stash`
  
+ 删除远端提交的文件
  `git rm -r --cached .idea `
  
+ 合并不同仓库的不同分支  
  [链接](https://www.zybuluo.com/aqa510415008/note/1428756)  
  `在merge时，注意merge的目标是否正确`
  
  
### Author identity unknown
+ 解决方法   
```
在git命令行中重新输入命令:  
先输入：$ git config --global user.name “你的名字”
回车后，
再输入：$ git config --global user.email “你的邮箱地址”
```



## rebase and merge
[博客](https://zhuanlan.zhihu.com/p/93635269)
### 基本原则
+ 下游分支更新上游分支内容的时候使用 `rebase`
+ 上游分支合并下游分支内容的时候使用 `merge`
+ 更新当前分支的内容时一定要使用 `--rebase` 参数
### 例子
现有上游分支 master，基于 master 分支拉出来一个开发分支 dev，在 dev 上开发了一段时间后要把 master 分支提交的新内容更新到 dev 分支，此时切换到 dev 分支，使用 git rebase master等 dev 分支开发完成了之后，要合并到上游分支 master 上的时候，切换到 master 分支，使用 git merge dev

### 注意事项
+ 更新当前分支代码的时候一定要使用 `git pull origin xxx --rebase`
+ 合并代码的时候按照最新分支优先合并为原则
+ 要经常从上游分支更新代码，如果长时间不更新上游分支代码容易出现大量冲突


## error
### 10054
+ 原因：上传的文件太大，缓存不够，默认只有1M
+ 解决方法：`git config http.postBuffer 524288000`
`git config --global http.sslVerify "false"`

## Ignore

### .gitignore did not work

```bash
mv .idea ../.idea_backup
rm .idea # in case you forgot to close your IDE
git rm -r .idea 
git commit -m "Remove .idea from repo"
mv ../.idea_backup .idea
```



