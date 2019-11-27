# linux notebook
1. 实时查看日志文件更新
    * tail -f app.log

## 磁盘分区与自动挂载
    1. fdisk -l: 查看磁盘分区情况
    2. fidsk /dev/sda: 对磁盘进行分区
    3. mkfs -t ext4 /dev/sda4: 对分区格式化, 只有格式化之后才能进行挂载
    4. mount /dev/sda /new_empty_dir: 手动挂载
        * umount /dev/sda
    5. vim /etc/fstab: 设置开机自动挂载分区
        * /dev/sda4 /home ext4 defaults 0 2: 将分区挂载在/home目录下, 之前的挂载磁盘内容会被覆盖, 所以最好提前做好备份工作
    6. fdisk默认为mbr文件系统分区限制为2TB, 可以用parted对gpt文件系统分区
    7. mbr文件系统默认主分区加上扩展分区不超过4, 扩展分区不超过1, 扩展分区包含逻辑分区, 逻辑分区的个数没有限制

3. 复制
    * cp -a: 复制常用的命令相当于cp -pdr, 即连同文件的属性一起复制, 若来源为连结档的属性则复制连结档的属性而非本身, 递归的持续复制

4. 打开mongo服务:
    * cd /usr/local/mongodb/bin/
    * ./mongod --smallfiles

5. 清屏命令:
    * printf "\033c"

6. 后台运行
    * nohup python3 *.py >out.log 2>&1 &: 即使关闭终端, 程序依然可以在服务器上运行, 并将日志记录在out.log
    * nohup python3 *.py >/dev/null 2>&1 &: 将日志记录丢弃

7. 查看系统进程
    * htop: 友好的系统进程查看命令
    * lsof -p pid | wc -l: 可以查看进程打开的文件数
        * lsof: 显示该进程打开文件
        * wc: 计算文件数
    * lsof -u username: 列出某个用户打开的文件信息
    * lsof -c mysql: 列出某个程序进程打开的文件信息
    * lsof -i :3306: 列出谁在使用某个端口

## 关闭系统进程
* killall -9 'python3': 关闭所有包含进程名python3的进程
* kill: 用来删除执行中的程序或者工作. kill 可将指定的信息送至程序, 预设的信息为 SIGTERM(15), 可将指定程序终止, 若无法终止该程序, 可使用 SIGKILL(9) 信息尝试强制删除程序.  (一般先用 ps -ef 查找某个进程, 得到它的进程号, 然后再使用 kill -9 进程号 强制终止该进程.)
    * 语法: kill (选项) (参数)
        * 选项: -l <信息编号>: 若不加<信息编号>选项, 则会列出全部的信息名称
        * 参数: 进程或作业识别号, 指定要删除的进程或作业
        * 常用的信号:
            * HUP 1 终端断线
            * INT 2 中断 (同 ctrl + c)
            * QUIT 3 退出 (同 ctrl + \\)
            * TERM 15 终止
            * KILL 9 强制终止
            * CONT 18 继续(与STOP相反, fg/bg命令)
            * STOP 19 暂停(同 ctrl + z)
    * 例: ps -ef | grep vim 然后 kill -9 pid

9. selenium
    * 双核 1 g: 最佳是跑5个selenium

10. 创建文件夹
    * mkdir -p: no error if existing, make parent directories as needed

## 修改文件所属
* chown: Change the owner and/or group of each FILE to OWNER and/or GROUP
    * chown root /u: change the owner of /u to "root"
    * chown root:staff /u: likewise, but also change its group to "staff"
    * chown -hR root /u: change the owner of /u and subfiles to "root"

## 修改文件权限
* chmod: chmod [-R] xyz {file or directory}

12. 设置环境变量
    * export: 用于 **临时** 设置或者显示环境变量
        * export LANG=en_US.UTF-8: 保证输出不会在 linux 终端上显示乱码
        * export -p: 列出当前环境变量
    * 修改 /etc/profile: 用于 **永久** 设置环境变量, 对所有用户有效
        * 例如: `export PATH="$PATH:/home/xyz/Tesseract/bin"`: 添加了一个系统路径, 因为 linux 里面系统路径分隔符为 ':'
    * 修改 ~/.bashrc 文件永久设置环境变量, 仅对单独用户有效
    * 在 su 模式下, 可以用 source 命令, source /etc/profile 使得设置立即生效, 否则正常重启后生效
    * source: source filename: 在当前 bash 环境下读取并执行 filename 中的命令

## connect vpn
* openconnect vpn-ct.ecnu.edu.cn

## linux 和 windows 文件交互
* rz: windows 到 linux, sz: linux 到windows
* apt install lrzsz
## grep
* ls /dir | grep filename: 搜索 /dir 下包含 filename 的文件
* grep match_pattern file_name 或 grep "match_pattern" file_name: 在文件中搜索一个单词, 命令会返回一个包含 "match_pattern" 的文本行
* grep -c: 计算符合范本样式的行数
   - grep -c '入库' tmp.log: 计算文件 'tmp.log' 包含 '入库' 字符的行数.
* grep test *file: 在当前的目录中, 查找后缀有 file 字样的文件, 并且文件中包含 test 字符串的文件, 并打印出该字符串的行
* grep -r update /etc/acpi: 以递归的方式查找符合条件的文件
* grep -v: 反向查找, 不符合范本样式的文件

## ps
* ps: report a snapshot of the current processes
* ps -e: Select all processes. Identical to -A.
* ps -f: Do full-format listing.
## 缓存
* echo 3 > /proc/sys/vm/drop_caches: 清除缓存中的数据

## apt
* lsb_release -c: 显示系统代号
* /etc/apt/sources.list: apt 源的设置, 一般需要替换为阿里镜像源
* apt update: 访问源列表里的每一个网址, 并读取软件列表, 然后保存在本地
* apt upgrade: 将本地已安装软件与最近下载的软件列表里的软件对比, 更新
* dpkg -i: 安装本地软件包

## 死机
* ctrl + alt + prtsc + reisub: 安全的重启, 不会丢失数据

## du
* du -h --max-depth=1: 查看文件夹大小, 递归深度为1
* du -sh file: 等价于 du -h --max-depth=0, 只查看 file 的大小, 不看子目录或者子文件

## df
- 用来检查 linux 服务器的文件系统的磁盘占用情况. 可以利用该命令来获取磁盘被占用了多少空间, 目前还剩下多少空间等信息.
- df -h 方便阅读方式显示.

## tar
* tar -cvf log.tar log2012.log: 仅打包, 不压缩(注: 需要 log.tar 存在)
* tar -zcvf log.tar.gz log2012.log: 打包后, 以 gzip 压缩
* tar -jcvf log.tar.bz2 log2012.log: 打包后, 以 bzip2 压缩
* tar -ztvf log.tar.gz: 查阅 log.tar.gz 包内的文件
* tar -zxvf log.tar.gz: 将 log.tar.gz 解压缩

/etc
* vim /etc/motd: 可以让使用者登录后获取一些讯息

## zip & unzip
* zip 命令可以将常用的文件压缩成常用的 zip 格式, unzip 命令则用来解压缩 zip 文件.
1. 我想把一个文件abc.txt和一个目录dir1压缩成为yasuo.zip:
    * `zip -r yasuo.zip abc.txt dir1`
2. 我下载了一个yasuo.zip文件，想解压缩：
    * `unzip yasuo.zip`
    - -d<目录> 指定文件解压缩后所要存储的目录
3. 我当前目录下有abc1.zip，abc2.zip和abc3.zip，我想一起解压缩它们：
    - `unzip abc\?.zip`
4. 我有一个很大的压缩文件large.zip，我不想解压缩，只想看看它里面有什么：
    - `unzip -v large.zip`
5. 我下载了一个压缩文件large.zip，想验证一下这个压缩文件是否下载完全了:
    -  `unzip -t large.zip`
6. 我用-v选项发现music.zip压缩文件里面有很多目录和子目录，并且子目录中其实都是歌曲mp3文件，我想把这些文件都下载到第一级目录，而不是一层一层建目录：
    - `unzip -j music.zip` 


## ssh
- 开启 ssh: service sshd restart/start
