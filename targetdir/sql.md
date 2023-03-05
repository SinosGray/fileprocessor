---
categories:
- null
date: 2022-10-23 21:55:00
password: null
sticky: 100
tags:
- select
- num
- order
- email
- name
title: mysql必知必会读书笔记
---

> 

<!--more-->

# 基本语法

## primary key:

- 不允许修改或更新
- 不能重用(如果删除, 他的主键不能赋给以后的新行)
- 不允许 null 值

```sql
select A, B
from t
order by A, B;
```

仅在多个行有相同的 A 值时, 才按照 B 排序

```sql
select A, B
from t
order by A DESC
# 默认升序, desc 降序, 每个 desc 只作用于一个列
```

```sql
select A, B
from t
where A = 10 and B = 1;
# where A < 10;
# where A bwtween 1 and 2;
# where A is null
# where A = 10 or B = 1;
# and 优先级高于 or
# where A in ('A', 'a');
# where not A = 10;
# where A like '_[^Bb][Aa]A%'
```

```sql
select concat(A, ',', B) as C, 
			 A*B as D
from t;
```

## 聚集函数

- avg
- count
- max
- min
- sum

​	只包含不同的值: distinct

## 分组

除聚集计算语句之外, select 语句中的每个列都必须在 group by 语句中出现

```sql
select A, count(*) as amount
from t
where B > 1
group by A
having count(*)>2
order by A;
```

## 子查询

作为子查询的 select 只能查询单个列

```sql
select A
from t
where B in
(select C from t0);

SELECT cust_name, cust_state, 
(SELECT COUNT(*) 
 FROM Orders 
 WHERE Orders.cust_id = Customers.cust_id) As orders 
FROM Customers 
ORDER BY cust_name;
# 该子查询会执行 查询到的客户数量 次
```

## join

### 内部联结

```sql
SELECT vend_name, prod name, prod price
FROM Vendors, Products 
WHERE Vendors.vend_id = Products.vend_id;

# or

SELECT vend_name, prod_name, prod_price
FROM Vendors INNER JOIN Products 
ON Vendors.vend_id = Products.vend_id;
```

没有联结条件返回的会是笛卡尔积

### 别名

```sql
SELECT cust_name, cust_contact 
FROM Customers As C, Orders As O, OrderItems AS OI 
WHERE C.cust_id = O.cust_id 
AND OI.order_num = O.order_num 
AND prod_id = 'RGAN01'；
```

### 自连接

```sql
SELECT c1.cust_id, c1.cust_name, c1.cust_contact 
FROM Customers As c1, Customers As c2 
WHERE c1.cust_name = c2.cust_name 
AND c2.cust_contact = 'Jim Jones'；
```

### 自然联结

重复的列需要手动处理

```sql
SELECT C.*, O.order_num, O.order_date, OI.prod_id, OI.quantity, OI.item_price 
FROM Customers As C, Orders As O, OrderItems As OI 
WHERE C.cust_id = O.cust_id 
AND OI.order_num = O.order_num 
AND prod_id = 'RGAN01';
```

### 外部联结

联结包含了在相关表中没有关联行的行

RIGHT指出的是OUTER JOIN右边的表， 而LEFT指出的是OUTER JOIN左边的表, 使用LEFT OUTER JOIN从FROM子句的左边表(Customers表）中选择所有行

```sql
SELECT Customers.cust_id, Orders.order_num 
FROM Customers INNER JOIN Orders 
ON Customers.cust_id = Orders.cust_id;

SELECT Customers.cust_id, Orders.order_num 
FROM Customers LEFT OUTER JOIN Orders 
ON Customers.cust_id = Orders.cust_id;

SELECT Customers.cust_id, Orders.order_num 
FROM Customers, Orders 
WHERE Customers.cust_id *= Orders.cust_id;
```

### 带聚集函数的联结

```sql
SELECT Customers.cust_id, 
 COUNT (Orders.order_num) As num_ord 
FROM Customers INNER JOIN Orders 
ON Customers.cust_id = Orders.cust_id 
GROUP BY Customers.cust_id;
```

## 组合查询 union

- union 中每个查询必须包含相同的列, 表达式, 或聚集函数
- 默认去除重复行, union all 不去除
- 只能有一个 order by

```sql
SELECT cust_name, cust_contact, cust_email 
FROM Customers 
WHERE cust_state IN ('IL','IN'，'MI');

SELECT cust_name, cust_contact, cust_email 
FROM Customers 
WHERE custname = 'Fun4All';

SELECT cust_name, cust_contact, cust_email 
FROM Customers 
WHERE cust_state IN('IL', 'IN','MI'） 
UNION 
SELECT cust_name, cust_contact, cust_email FROM Customers 
WHERE cust_name = " Fun4A11’;
```

## 插入

```sql
INSERT INTO Customers 
VALUES('1000000006', 'Toy Land', '123 Any Street', 'New York', 'NY', '11111', 'USA', NULL, NULL);

INSERT INTO Customers
(cust_id, cust_name, cust_address, cust_City, cust_state, cust_zip, cust_country, cust_contact, cust_email) VALUES('1000000006', 'Toy Land', '123 Any Street', 'New York', 'NY', '11111', 'USA', NULL, NULL);

INSERT INTO Customers 
(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country) 
VALUES('1000000006', 'Toy Land', '123 Any Street', 'New York', 'NY', '11111', 'USA');
# 忽略的列必须允许为 null, 或者在表定义中给出默认值

INSERT INTO Customers
(cust_id, cust_contact, cust_email, cust_name, cust_address, cust_city, cust_state, cust_zip, cust country) 
SELECT cust_id, cust_contact, cust_email, cust_name, cust_address, cust_city, cust_state, cust_zip， cust_country 
FROM CustNew;

# 复制创建一个表
CREATE TABLE CustCopy As 
SELECT * 
FROM Customers;
```

## 更新

```sql
UPDATE Customers 
SET cust_contact = 'Sam Roberts' 
cust_email ='sam@toyland.com' 
WHERE cust_id = '1000000006';

DELETE FROM Customers 
WHERE cust_id = '1000000006';
```

## 创建操作表

```sql
CREATE TABLE Products
(
  prod_id CHAR(10) NOT NULL, 
  vend_id CHAR(10) NOT NULL, 
  prod_name CHAR (254) NOT NULL DEFAULT ''; 
  prod_price DECIMAL(8, 2) NOT NULL, 
  prod_desc VARCHAR (1000) NULL 
);
# 是否允许 null, 默认允许 null

DROP TABLE Custcopy;

ALTER TABLE Vendors 
ADD vend_phone CHAR(20);

ALTER TABLE Vendors 
DROP COLUMN vend_phone;
```

## 视图 view

- 重用SQL语句。 
- 简化复杂的SQL操作。在编写查询后，可以方便地重用它而不必知道它的基本查询细节。
- 使用表的组成部分而不是整个表。 
- 保护数据。可以给用户授予表的特定部分的访问权限而不是整个表的访问权限。 
- 更改数据格式和表示。视图可返回与底层表的表示和格式不同的数据。

- 与表一样，视图必须唯一命名（不能给视图取与别的视图或表相 同的名字)。 
- 为了创建视图，必须具有足够的访问权限。这些限制通常由数据 库管理人员授予。 
- 视图可以嵌套，即：可以利用从其他视图中检索数据的查询来构 造一个视图。所允许的嵌套层数在不同的DBMS中有所不同（嵌 套视图可能会严重降低查询的性能，因此在产品环境中使用之前， 应该对其进行详细的测试）。
- 许多DBMS禁止在视图查询中使用ORDER BY子句。
-  有的DBMS要求命名返回的所有列，如果列是计算字段，则需 使用别名（关于列别名的更多信息，请参阅第7章)。 
- 视图不能索引，也不能有关联的触发器或默认值。 
- 有的DBMS把视图作为只读的查询，这表示可以从视图检索数据， 但不能将数据写回底层表。详情请参阅具体的DBMS文档。 
- 有的DBMS允许创建这样的视图，它不允许进行导致行不再属于视图的插入或更新。例如，有这样一个视图，它只检索带有电子 邮件地址的客户。如果更新某个客户，删除他的电子邮件地址， 这将使该客户不再属于视图。这是默认行为，而且是允许的，但在具体的DBMS上可能能够防止这种情况发生。

```sql
CREATE VIEW Productcustomers As 
SELECT cust_name, cust_contact, prod_id 
FROM Customens, Orders, OrderItems 
WHERE Customers.cust_id = Orders.cust_id 
AND OrderItems.order_num = Orders.order_num;

DROP VIEW Viewname:
```

## 存储过程

```sql
CREATE PROCEDURE MailingListcount 
(Listcount OUT NUMBER) 
IS 
BEGIN 
	SELECT * FROM Customers 
	WHERE NOT cust email IS NULL; 
	Listcount:= SQL%ROWCOUNT;
END;

EXECUTE AddNewProduct('JTS01', 'Stuffed Eiffel Tower'， 6.49， 'Plush stuffed toy with the btext La Tour Eiffel in red white and blue'）
```

## 事务管理

保证成批的 sql 操作要么完全执行, 要么完全不执行

## 游标

## 外键

```sql
CREATE TABLE Orders
(
	order_num INTEGER NOT NULL PRIMARY KEY,
  orden_date DATETIME NOT NULL, 
  cust_id CHAR(10) NOT NULL REFERENCES Customers(cust_id)
);
```

## 检查约束

```sql
CREATE TABLE OrderItems( 
  order_num INTEGER NOT NULL,
  order_item INTEGER NOT NULL, 
  prod_id CHAR(10) NOT NULL,
  quantity INTEGER NOT NULL CHECK (quantity > 0),
  item_price MONEY NOT NULL 
);
```

## 索引

解决方法是使用索引。可以在一个或多个列上定义索引，使DBMS 保存其内容的一个排过序的列表。

## 触发器

```sql
CREATE TRIGGER customer_state 
ON Customers 
FOR INSERT, UPDATE
AS 
UPDATE Customers 
SET cust_state = Upper(cust_state) 
WHERE Customers.cust_id = inserted.cust_id;
```































