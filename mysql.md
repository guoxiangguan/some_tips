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

## create 语句
* create table table_name select * from table_name;: 复制表结构以及数据
* create table table_name like table_nme;: 仅复制表结构

## update 语句
* UPDATE table_name SET field1=new-value1, field2=new-value2 [WHERE Clause];: 更新表字段
### 批量更新例子:
- update table1 as a, table2 as b, set a.url = b.url where a.line_id = b.line_id;
- update table1 as a set a.flag = '非定向';

## 事务
* 用来做大范围修改的一个最佳的选择, 防止误操作造成不可挽回的错误
```
set autocommit=0; # 禁止自动提交
begin; # 开始事务
savepoint point0; # 建立事务保存点
rollback to point0; # 回滚到 point0;
rollback; # 回滚到初始状态
commit; # 确认提交事务
```
