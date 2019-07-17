# linux notebook
1. 实时查看日志文件更新
    * tail -f app.log
2. 磁盘分区与自动挂载
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
7. 查看系统进程
    * htop: 友好的系统进程查看命令
    * lsof -p pid | wc -l: 可以查看进程打开的文件数
        * lsof: 显示该进程打开文件
        * wc: 计算文件数
8. 关闭系统进程
    * killall -9 'python3': 关闭所有包含进程名python3的进程
9. selenium
    * 双核 1 g: 最佳是跑5个selenium
10. 创建文件夹
    * mkdir -p: no error if existing, make parent directories as needed
11. 修改文件拥有者
    * chown: Change the owner and/or group of each FILE to OWNER and/or GROUP
        * chown root /u: change the owner of /u to "root"
        * chown root:staff /u: likewise, but also change its group to "staff"
        * chown -hR root /u: change the owner of /u and subfiles to "root"
## 修改文件权限
* chmod: chmod [-R] xyz {file or directory}
12. 设置环境变量
    * export: 用于设置或者显示环境变量, 一般是临时的
    * export -p: 列出当前环境变量
    * 修改 ~/.bashrc: 永久性的, 配置当前用户下的环境变量
    * 修改 /etc/profile: 永久性的配置所有用户的环境变量
    * source: source filename: 在当前 bash 环境下读取并执行 filename 中的命令
## connect vpn
* openconnect vpn-ct.ecnu.edu.cn

## linux 和 windows 文件交互
* rz: windows 到 linux, sz: linux 到windows

## 缓存
* echo 3 > /proc/sys/vm/drop_caches: 清除缓存中的数据

## apt
* lsb_release -c: 显示系统代号
* /etc/apt/sources.list: apt 源的设置, 一般需要替换为阿里镜像源
* apt update: 访问源列表里的每一个网址, 并读取软件列表, 然后保存在本地
* apt upgrade: 将本地已安装软件与最近下载的软件列表里的软件对比, 更新
* dpkg -i: 安装本地软件包
