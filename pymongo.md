# pymongo notebook
## 在使用多线程时的注意事项
* On Unix systems the multiprocessing module spawns processes using fork(). Care must be taken when using instances of MongoClient with fork(). Specifically, instances of MongoClient must not be copied from a parent process to a child process. Instead, the parent process and each child process must create their own instances of MongoClient. 
```python
    # Each process creates its own instance of MongoClient.
    def func():
        db = pymongo.MongoClient().mydb
        # Do something with db.
    proc = multiprocessing.Process(target=func)
    proc.start()
```

## collection 操作
### 重命名
* `collection.rename('new_name')`: 集合的重命名
### 正则查询
* `collection.find({'key':{'$regex': "rep"}})`

