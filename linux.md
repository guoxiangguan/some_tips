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
    * kill -9 'python3': 关闭所有包含进程名python3的进程

9. selenium
    * 双核 1 g: 最佳是跑5个selenium

10. 创建文件夹
    * mkdir -p: no error if existing, make parent directories as needed

11. 修改文件权限
    * chown: Change the owner and/or group of each FILE to OWNER and/or GROUP
        * chown root /u: change the owner of /u to "root"
        * chown root:staff /u: likewise, but also change its group to "staff"
        * chown -hR root /u: change the owner of /u and subfiles to "root"

12. 设置环境变量
    * export: 用于 **临时** 设置或者显示环境变量
        * export LANG=en_US.UTF-8: 保证输出不会在 linux 终端上显示乱码
        * export -p: 列出当前环境变量
    * 修改 /etc/profile: 用于 **永久** 设置环境变量, 对所有用户有效
        * 例如: `export PATH="$PATH:/home/xyz/Tesseract/bin"`: 添加了一个系统路径, 因为 linux 里面系统路径分隔符为 ':'
    * 修改 ~/.bashrc 文件永久设置环境变量, 仅对单独用户有效
    * 在 su 模式下, 可以用 source 命令, source /etc/profile 使得设置立即生效, 否则正常重启后生效

## connect vpn
* openconnect vpn-ct.ecnu.edu.cn