# git 笔记

## git fetch 和 git pull 的差别
1. git fetch 相当于是从远程获取最新到本地, 不会自动 merge, 如下指令:
    > git fetch origin master // 将远程仓库的 master 分支下载到本地当前 branch 中  
    > git log -p master origin/master // 比较本地 master 分支和 origin/master 分支的qubie  
    > git merge origin/master // 进行合并  
2. 也可以用以下的指令:  
    > git fetch origin master:tmp // 从远程仓库 master 分支获取最新, 在本地建立 tmp 分支  
    > git diff tmp // 将当前分支和 tmp 进行对比  
    > git merge tmp // 合并 tmp 分支到当前分支  
3. git pull: 相当于是从远程获取最新版本并 merge 到本地  
    > git pull origin master  
4. 在实际使用中 git fetch 更加安全一点

## 创建 ssh key
- `ssh-keygen -t rsa -C "1587753354@qq.com"`
- 然后从用户目录下的 .ssh 文件下， 将 rsa.pub 里面的内容粘贴到 git_hub 的 ssh-key 下.
