# python3.7

## dictionary view objects
* The objects returned by dict.keys(),dict.values(),and dict.items() are view objects.They provide a dynamic view on the dictionary's entries,which means that when the dictionary changes,the view reflects these changes.

## 全局变量和局部变量

### 一般写程序变量的命名规则
* 全局变量变量名大写
* 局部变量变量名小写
* 函数优先读取局部变量，能读全局变量，无法对全局变量重新赋值操作，#全局变量是不可变的类型
* 全局变量是可变类型，函数可以对全局变量进行操作
* 函数中有global关键字，变量本质就是全局变量，可读取全局变量，也可操作全局变量

## 多线程 concurrent.futures.ThreadPoolExecuter

    ```python
    f_list = []
    with concurrent.futures.ThreadPoolExecuter(max_workers=nums) as executer:
        executer.map(func, list_of_args) # 有顺序的平均分配任务
        f_list = [executer.submit(func, args) for args in args_list] # 一个线程的任务处理完立刻取下一个任务,是无序的,不平均的,一般而言这样是比较合理的
    wait(f_list)
    print('done')
    ```

## 日志的配置
    ```python
    # 日志配置
    logger = logging.getLogger('moudle_name')
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler('moudel_name.log')
    fh.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(sh)
    ```

## 生成器
* 用yield关键字或者括号包含表达式, 用next()获取其中的值, 或者用for循环来获取其中的值.
* 可以借用itertools.islice()方法来获取生成器切片.

## python 使用 pymysql DBUtils 创建连接池, 提升性能
```python
import pymysql
from DBUtils.PooledDB import PooledDB
pool = PooledDB(pymysql, 5, host='ip', user='user', passwd='passwd', db='db', port=3306, setsession=['SET AUTOCOMMIT = 1']) # 5为连接池最小连接数, setsession=['SET AUTOCOMMIT = 1']是用来设置线程池是否打开自动更新的配置，0为False，1为True
conn = pool.connection()
```
* 常用配置:
    ```python
    pool = PooledDB(pymysql, mincached=10, maxcached=20, maxshared=10, maxconnections=200, blocking=True,
            maxusage=100, host=HOST, user=USER, passwd=PASSWD, db='spider_test', port=PORT, setsession=['SET AUTOCOMMIT = 1'], charset=CHARSET)
    ```
* 优点:
    1. 在程序创建连接的时候, 可以从一个空闲的连接中获取, 不需要重新初始化连接, 提升获取连接的速度
    2. 关闭连接的时候, 把连接放回连接池, 而不是真正的关闭, 所以可以减少频繁地打开和关闭连接

## configparser
### 简介
* configparser用于配置文件解析, 可以解析特定格式的配置文件, 多数此类配置文件名格式为***.ini

```
    #### ini 文件示例 ####
    [section1]
    name = wang
    age = 18

    [section2]
    name:python
    age = 19

    #### 文件格式说明 ####
    [xxx] 代表节点
    xx = xx 或者 xx : xx 代表参数
```
### 使用
```python
    import configparser       # 导入模块
    config = configparser.ConfigParser()   # 创建对象
    config.read("user.ini", encoding="utf-8")  # 读取配置文件，如果配置文件不存在则创建
    # 查看
    secs = config.sections()  # 获取所有的节点名称
    print(secs)
    # ['section1', 'section2']
    options = config.options('section1')  # 获取指定节点的所有key
    print(options)
    # ['name', 'age']
    item_list = config.items('section1')  # 获取指定节点的键值对
    print(item_list）
    #[('name', 'wang'), ('age', '18')]
    val = config.get('section1', 'name')  # 获取指定节点的指定key的value
    print(val)
    #　wang
    val = config.getint('section1', 'age')  # 获取节点section1的age属性，属性需要是int型，否则ValueError
    print(val）
    # 18
    val = config.has_section('section1')  # 检查指定节点是否存在，返回True或False
    print(val)
    # True
    val = config.has_option('section1', 'age')  # 检查指定节点中是否存在某个key，返回True或False
    print(val)
    #True

    # 增删改
    config.add_section("node")  # 添加一个节点，节点名为node, 此时添加的节点node尚未写入文件
    config.write(open('user.ini', "w"))  # 将添加的节点node写入配置文件

    config.remove_section("node")  # 删除一个节点，节点名为node, 删掉了内存中的节点node
    config.write(open("user.ini", "w"))  # 将删除节点node后的文件内容回写到配置文件

    config.set("section1", "k1", "v1")  # 在已存在的节点中添加一个键值对k1 = v1 ,如果该节点不存在则报错,如果key已经存在，则修改value
    # configparser.NoSectionError: No section: 'section'
    config.write(open("user.ini", "w"))
```

## os.path.dirname(\_\_file\_\_)
### 返回脚本的路径

* 注意:
    1. 必须是实际存在的.py文件, 如果在命令行执行会引发NameError: name '__file__' is not defined
    2. 在运行的时候如果完整的执行的路径，则返回.py文件的全路径如:
        * `python c:/test/test.py` 则返回路径 c:/test
        * `python test.py` 则返回空

## 装饰器
* 装饰器的本质是一个函数, 可以让其他函数在不改动源代码的情况下增加其他新功能, 比如网站经常需要权限校验等场景

## redis
### 基本操作
* redis-py库提供两个类Redis和StrictRedis来实现redis的命令操作
* 推荐使用 StrictRedis
    ```python
    from redis import StrictRedis
    redis = StrictRedis(host='localhost', port=6379, db=0, password='sth')
    redis.set('name', 'bob')
    print(redis.get('name'))
    ```
* 连接池 ConnectionPool
    ```python
    from redis import StrictRedis, ConnectionPool
    pool = ConnectionPool(host='localhost', port=6379, db=0, password='sth')
    redis = StrictRedis(connection_pool=pool)
    ```
* 键操作

| 方法 | 作用 | 参数说明 | 示例 | 示例说明 | 示例结果 |
| :--:   |:---:   | :---:    |:---:    |:---:      |:--:    |
| `exists(name)` | 判断一个键是否存在 | name: 键名 | `redis.exists('name')` | 是否存在 name 这个键 | True/False |
| `delete(name)` | 删除一个键 | name: 键名 | `redis.delete('name')` | 删除 name 这个键 | 1 |
| `randomkey()` | 获取随机一个键 |
| `rename(src, dst)` | 重命名键 |
| `set(name, value)` | 给数据库中键为 name 的键赋值 value |
| `get(name)` | 返回数据库中键为 name 的 value |

* 列表常用键操作
    * `db.lpush(key, value)` 列表向左推入一个元素, redis的列表更像是一个队列
    * `db.blpop(key, [timeout])` 从列表中弹出第一个元素, 如果没有就会堵塞, 可以设置一个堵塞时间
    * `db.llen(key)` 返回列表的长度
    * **注**: 可以用redis控制并行的线程个数, 在某些场景下很好用, 比如有很多多线程的函数一起运行, 这时候可以使用redis队列控制这些多线程函数总的并行数不超过某个阈值, 具体可见test_ssh_loadhtml.py文件控制多线程爬虫不过度占用服务器的资源的实例.

## 字符串 str
### str.replace(a, b, count=-1)
* 将 str 中的 a 全部替换为 b, 返回一个新的对象, 不会在 str 上进行修改.
### 编码
* 文本字符全部用 str 类型表示, str 可以表示 Unicode 字符集所有的字符
* str --encode--> bytes; bytes --decode--> str;
* encode 负责字符到字节的编码转换, 默认使用 UTF-8 编码转换
* decode 负责字节到字符的编码转换, 默认使用 UTF-8 编码格式转换

## 日期时间 datetime
* 获取当前时间: `datetime.datetime.now()`
* 获取指定时间和日期: `datetime.datetime(2015, 4, 19, 12, 20)`
* 把一个 datetime.datetime 类型转换为 timestamp 只需要简单调用 timestamp() 方法
* 将 timestamp 转换为 datetime.datetime 类型, 使用 datetime.datetime 提供的 fromtimestamp() 方法, 默认是本地时间, 转换到 UTC 标准时间使用 utcfromtimestamp() 方法
* str 转换为 datetime.datetime 类型: `datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')`
* datetime.datetime 转换为 str:
    ```python
    >>> from datetime import datetime
    >>> now = datetime.now()
    >>> print(now.strftime('%a, %b %d %H:%M'))
    Mon, May 05 16:28
    ```
* datetime加减:
    ```python
    >>> from datetime import datetime, timedelta
    >>> now = datetime.now()
    >>> now
    datetime.datetime(2015, 5, 18, 16, 57, 3, 540997)
    >>> now + timedelta(hours=10)
    datetime.datetime(2015, 5, 19, 2, 57, 3, 540997)
    >>> now - timedelta(days=1)
    datetime.datetime(2015, 5, 17, 16, 57, 3, 540997)
    >>> now + timedelta(days=2, hours=12)
    datetime.datetime(2015, 5, 21, 4, 57, 3, 540997)
    ```
