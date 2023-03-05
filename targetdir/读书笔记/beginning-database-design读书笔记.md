---
categories:
- 读书笔记
date: 2022-11-29 22:26:44
password: null
sticky: 100
tags:
- key
- primary
- fields
- information
- field
title: beginning-database-design读书笔记
---

> 

<!--more-->

# Chapter 2: Guided Tour of the Development Process

用用例(use case)抽象出模型

- 类
- 关系

For data retrieval or reporting tasks, ask questions about **which attributes might be used for sorting, grouping, or selecting data.(or mis-spell)** These attributes may be candidates for additional classes.

1. Express the problem in terms of what a user might want to achieve. For a database problem, this will typically be in terms of the data to be stored and the information that needs to be retrieved. Sketch some **initial use cases and a data model**.
2. **Think about other possible uses of the information and how the data might be usefully ordered or grouped.** Undertake an iterative analysis process of reconsidering the data model and the use cases, until you are satisfied that you have a complete and precise understanding of the problem. For larger problems, this stage may include making some simplifying or other pragmatic choices. The bulk of this book will concentrate on this phase of the process.
3. Choose the type of product to manage the data and create an appropriate design.
   **For a relational database, this will involve designing tables, keys, and foreign keys.** Different structures will be required if the project is to be implemented in some other type of product such as a programming language or a spreadsheet. The design phase is discussed more fully in Chapters 7 to Chapter 9.
4. Build the application. For a relational database, this will include setting up the tables and developing forms and reports to satisfy the use cases. The mechanics of how to do this in any particular product is outside the scope of this book, but there are numerous how–to books available that will help you.

# Chapter 3: Initial Requirements and Use Cases

steps:

- What does the user do?
- What data are involved?
- What is the main objective(主体) of the system?
- What data are needed to satisfy this objective?(明确系统的范围)
- What are the input(maintain) use cases?
- What is the first data model?
- What are the output use cases?



# Chapter 4: Learning from the Data Model 

questions:

- **Optionality:** Should it be 0 or 1? 

- **Cardinality of 1:** Might it occasionally be 2?

- **Cardinality of 1:** What about historical data?

  是否保存? 如何保存?

- **Many–Many:** Are we missing anything?

  中间类

# Chapter 5: Developing a Data Model 

Some useful questions to ask when considering whether to represent information as an attribute, class, or relationship are summarized here:

- “Am I likely to want to **summarize, group, or select** using a given piece of information?” For example, might you want to select teams based on grade? If so, consider making the piece of information into a class.
- “Am I likely now or in the future to **store other data about this piece of information**?” For example, might you want to keep information such as phone and address about a captain? Does (or should) this information already exist in another class? If so, consider representing the piece of information as a relationship between the classes.

不要存在冗余路径(route), 不要存在关系闭环(closed path)

With two routes for the same information, we risk getting two different answers unless the data is very carefully maintained.

## fan trap:

<img src="https://tva1.sinaimg.cn/large/008vxvgGly1h8mdqk6ceaj30js0iu3zb.jpg" alt="截屏2022-11-29 22.44.54" style="zoom:33%;" />

增加新的关系

## chasm trap:

![截屏2022-11-29 22.46.14](https://tva1.sinaimg.cn/large/008vxvgGly1h8mdrxfi6nj30n20lyjs9.jpg)

增加一个新的 object(null)

## 三元关系

增加relationship: connection class

- Any attributes in the new class must depend on a particular combination of objects from *each* of the participating classes; such as, what do I need to know about a particular *member* playing on a particular *team* in a particular *match*?
- Consider what information might be pertinent to two objects from *pairs* of the contributing classes; for example, what do I need to know about a particular member and a particular team *independent* of any match? 这种需要单独增加两个类之间的联系

## 两个 class 之间有多个 relationship

## self relationship

# Chapter 6: Generalization and Specialization

## 继承

- If different objects have mutually exclusive values for some attributes (e.g., administrators have grades but technicians have dates), consider specialized subclasses.
- When you think *this is like that except for...* consider subclasses.
- When two classes have a similar relationship with another class, consider a new generalized superclass (e.g., if both students and staff are assigned parking spaces, consider a generalized class for people).

特化: 继承,  *Software entities (e.g. classes) should be open for extension and closed for modi**fi**cation*.

泛化: 提炼出基类

基类都应该是抽象的

多继承的问题: 多个基类会排列组合产生很多的子类

## 组合 聚合

# Chapter 7: From Data Model to Relational Database Design

## Domains and Constraints

domain 作用域是数据库, constraints 作用域是表

后加的数据可以为 null, 避免强制填入不恰当的数据

A good rule of thumb is th-at any data that you are likely to want to **search for, sort by, or extract** in some way should be in a field all by itself.

## referential integrity

each *value* in a foreign key field must exist as values in the primary key field of the table being referred to 

## 关系

### 1-many 关系

For a 1–Many relationship, the key field from the table representing the class **at the 1 end is added as a foreign key** in the table representing the class at the Many end.

### many-many 关系

拆分为两个 1-many 关系, 增加关系类, 主键是两个外键的组合

### 1-1 关系

两侧分别作为外键会有不同的影响(主键不会重复, 但外键可能重复)

### 继承关系

将父类作为外键插入子类表



# Chapter 8: Normalization

## 定义

### key

The key fields functionally determine all the other fields in the table. 

### primary key

A primary key has no subset of the fields that is also a key.

### candidate key

A candidate key is a key where no subset of the fields is also a key.

## 范式

### 第一范式

A table is not in first normal form if it is keeping **multiple values for a piece of information**.

解决方法:

remove the multivalued information from the table. Create a new table with that information and the primary key of the original table.

### 第二范式

A table is in second normal form if it is in first normal form AND **we need ALL the fields in the key** to determine the values of the non–key fields.

解决方法

remove those non–key fields that are not dependent on the whole of the primary key. Create another table with these fields and the part of the primary key on which they do depend.

### 第三范式

A table is in third normal form if it is in second normal form AND no non–key fields depend on a field(s) that is not the primary key.

解决方法

If a table is not in third normal form, remove the non–key fields that are dependent on a field(s) that is not the primary key. Create another table with this field(s) and the field on which it does depend.

### boyce codd 范式

A table is in Boyce–Codd normal form if every determinant could be a primary key.

A table in Boyce–Codd normal form is one in which every determinant could be a primary key.

即不存在多余的依赖关系

*A table is based on
 the key,
 the whole key,
 and nothing but the key (so help me Codd)*



# Chapter 9: More on Keys and Constraints 

- Where a primary key is made up of several concatenated fields, **it is worth considering a generated ID number to reduce the size of the foreign keys referencing the table.**

- Unique constraints can be used to enforce a 1–1 relationship.

- A constraint on the value of a field may be more appropriate than a relationship to another (very simple) table.

  但是这会导致比较难增加新的枚举值(如果是table 只需要 insert row)

- You have three options when you wish to delete a row that it is being referenced by a foreign key:

  - Disallow the deletion.
  - Make the field referencing the deleted row NULL (“nullify delete”).
  - Remove all rows that reference the deleted row (“cascade delete”).



































