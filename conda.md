# conda notebook
## 环境
    创建一个新环境，其中包含指定版本的python
        conda create --name new_env python=3.7

    查看所有环境的列表
        conda info --envs

    激活新环境
        conda activate new_env

    查看当前环境中python版本
        python --version

    停用当前环境返回基础环境
        conda activate

## 管理包
    检查Anaconda储存库(需要连接到internet)是否提供了某安装包
        conda search moudle

    将软件包安装到环境中
        conda install moudle
        当conda没有相应的安装包的时候也可以
            pip install moudle -i https://pypi.douban.com/simple

    检查安装的程序是否在此环境中
        conda list