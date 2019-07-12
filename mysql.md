# mysql 学习笔记
## limit 用法
* limit offset, `length`: limit 接受一个或两个数字参数, 第一个参数指定返回记录行的偏移量, 第二行返回记录行的最大数目
    * mysql> select * from table limit 5, 10; // 检索记录行 6-15
    * 为了检索从某一偏移量到记录集的结束所有的记录行, 可以指定第二个参数为 -1
    * 如果只给定一个参数, 它表示返回最大的记录行数目
    * mysql> select * from table limit 5; // 检索前5个记录行

## delete 语句
* 可以使用 delete from 命令来删除 mysql 数据表中的记录
* 语法:
    * delete from table_name [where clause]
* 注意:
    * 如果没有指定 where 子句, mysql 表中的所有记录将被删除
    * 可以在 where 子句中指定任何条件

## where 语句
* select * from table_name where id <> 5;
    * 在 mysql 中 <> 是 != 的意思