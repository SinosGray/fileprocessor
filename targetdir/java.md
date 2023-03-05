---
categories:
- language
date: 2020-01-25 12:31:30
tags:
- java
- public
- father
- book
- string
title: java
---

# Java 背景

> 简单介绍java的基础知识

<!--more-->

- Java SE(Java Platform,Standard Edition)，应该先说这个，因为这个是标准版本。
  Java EE (Java Platform，Enterprise Edition)，java 的企业版本
  Java ME(Java Platform，Micro Edition)，java的微型版本, 移动设备和嵌入式

  JavaSE 可以开发和部署在桌面、服务器、嵌入式环境和实时环境中使用的 Java 应用程序。是EE，和ME的基础。一般就是指JDK（Java Development Kit**（**JDK）是[太阳微系统](https://zh.wikipedia.org/wiki/昇陽電腦)针对[Java](https://zh.wikipedia.org/wiki/Java)开发人员发布的免费[软件开发工具包](https://zh.wikipedia.org/wiki/软件开发工具包)（SDK，Software development kit））。就是Java的基础语法（变量、方法、类之间的调用、关系，继承、接口、线程之类的），工具包（java.util.*  ）,或者其他的一些封装

  PS：

  1. java程序设计语言

  2. JVM java虚拟机

  3. java API类库

  4. 辅助工具如javac

     1+2+3+4=jdk（java开发的环境），2+3=jre（java运行的环境）

  JavaEE，其实是一套规范，就是用java语言做企业开发（目前看来就是开发一些动态网站，或者对外提供调用服务的网站，或者其他没接触过的。。。）中的一整套规范，比如类怎么封装，网页的请求要用什么方法处理，语言编码一类的处理，拦截器啊什么的定义，请求返回得有什么信息。。。（具体看servlet的接口就知道了）
  比如：tomcat就是按照这套规范开发的容器软件，还有什么weblogic，JBoss、Resin等等
  正因为我们开发网站（使用JSP，Servelet。。或者封装了这些的框架：SSH。。。）可以放在tomcat，也可以放在JBoss。。。。，因为都是按照一个规范开发的东西，实际使用的还是JavaSE的那些东西，多出来的就是EE的一些规范类的封装代码。

  JavaME 是微型版本，顾名思义，使用在手机啊，小设备啊上面的Java版本，特点就是小，相比JavaSE精简了很大一部分东西，（增加了一些小设备上的专有API，？？？这个不是很确定），
  我在2009年培训的时候，这个还写过游戏，还用在移动啊什么的开发上，可是后来你们应该知道了。。。安卓时代来临了。

  安卓中既然用的是Java，那么Java的语法应该都是适用的。所以SE是核心基础。其他的都是使用方法方式不同。

  文件名必须与公共的类名一致，文件后缀为.java
  如果有多个类，且没有public类，文件名可与任一类名相同
  一个JAVA源文件最多只能有一个public类
  如果一个Java源文件包含多个class，那么编译后会产生多个.class文件

# java基础

## 基础

- 工具

  javac 编译, java 运行, jdb 调试

- 版本

  java SE 桌面, java EE 服务器, java ME 嵌入式移动设备

```java
public class xxx{
  public static void main(String[] args){
    ......;
    int[] array = new int[7];//数组定义
    for(double value : myList) {
    	sum += value;
    }
  }
}
```

- JVM

  java源码编译后生成.class 文件, 由字节码构成

- 源文件.java -> 编译后.class

- 栈: 方法调用和局部变量

- 堆: 所有的对象

- i/o

  ```java
  Scanner scanner = new Scanner(System.in);
  //构造函数Scanner的参数类型也可为java.io.File
  //这是Scanner就从文件而不是标准输入流读取数据
  double d = scanner.nextDouble( ); 
  方法：
      nextByte( )、nextShort( )、nextInt( )
      nextLong( )、nextFloat( )、nextDouble( )
      next( ) 读入一个字符串
  
  ```

- 标识符: 标识符是由字母、数字、下划线(\_)、美元符号(\$)组成的字符序列, 标识符必须以字母、下划线(_)、美元符号($)开头。不能以数字开头。

## 数据类型

- 整数: byte 8, short 16, int 32, long 64

- 小数: float 32, double 64

- boolean 未明确定义, char 16

- 数组也是对象

- 主数据包装

  Boolean Character Byte Short Integer Long Float Double

  `Integer wrap = new Integer(i);`

  `int unwrap = wrap.intValue();`

  `int x = Integer.parseInt("2");`

- 默认int double, 比如`char c = (char)12;` 必须强制类型转换
- 1e2 是double类型, 1e2f是float类型
- switch(exp), exp结果只呢个为byte, char, short, int , enum 等不大于int的类型
- bool-exp ? exp-true : exp-false
- ASCII : \u0041 \u后面必须是4位16进制数

## 函数

- 对象作为参数, 传入的是对象(指针)的拷贝
- 实例变量(类中声明)不定义会有初始值(0, null), 局部变量不会有, 编译会报错
- 对象比较: == 是否指向同一对象, .equals() 完全相等

## 实用类

### ArrayList

`ArrayList<String> list = new ArrayList<String>();`

不能使用[]

如何引入 ArrayList?

1. `import java.util.ArrayList;`
2. `java.util.ArrayList<String> list = new java.util.ArrayList<String>()`

## 类

### 继承

| **访问权限** | **本类** | **本包** | **子类** | **它包** |
| ------------ | -------- | -------- | -------- | -------- |
| public       | √        | √        | √        | √        |
| protected    | √        | √        | √        | X        |
| 包级(默认)   | √        | √        | X        | X        |
| private      | √        | X        | X        | X        |

所有类都继承自Object, Object 不是抽象类

```java
//object 方法
equals();
getClass();
hashCode(); //唯一 id
toString();
```

`public class classson extends classfather{}`

调用父类方法

```java
public void method(){
  super.method();
  ...;
}
```

- 权限:

  public 会被继承, private 不会被继承

- final 修饰方法: 不可被覆盖

- 覆盖 override: 参数一样, 返回类型一样或者是之前返回类型的子类, 权限需要更开放(public 不能覆盖成 private)

- 重载 overload: 参数不一样, 返回可以不一样, 但不能只改变返回类型, 权限任意改变

- 覆盖特性：一旦父类中的实例方法被子类覆盖，同时用父类型的引用变量引用了子类对象，这时不能通过这个父类型引用变量去访问被覆盖的父类方法(即这时被覆盖的父类方法不可再被发现)。因为实例方法具有多态性（晚期绑定）

  在子类类体函数中可以使用super调用被覆盖的父类方法。

  ˜隐藏特性：指父类的变量（实例变量、静态变量）和静态方法在子类被重新定义，但由于类的变量和静态方法没有多态性，因此通过父类型引用变量访问的一定是父类变量、静态方法(即被隐藏的可再发现)。

- 根据引用判断还是根据确实类型判断?

  ```java
  public class Father {
      public void m(){
          System.out.println("father");
      }
  }
  
  public class Son extends Father{
      public static void main(String[] args) {
          Son son = new Son();
          Father father = son;
          son.m();
          father.m();
          //father.m_only(); 无法通过编译
      }
      @Override
      public void m() {
          System.out.println("son");
      }
      public void m_only(){
          System.out.println("son only");
      }
  }
  ```

  输出: son son

- 强制类型转换:  `Dog d = (Dog)o;`
  检查是否可以转换: `if(o isstanceof Dog)`
  
- 不支持多重继承, 请使用接口

### 多态

父类引用 = 子类对象

那么我们可以根据以上情况总结出多态成员访问的特点：
**成员变量**
编译看左边(父类),运行看左边(父类)
**成员方法**
编译看左边(父类)，运行看右边(子类)。动态绑定
**静态方法**
编译看左边(父类)，运行看左边(父类)。
(静态和类相关，算不上重写，所以，访问还是左边的)
**只有非静态的成员方法,编译看左边,运行看右边**

**不能使用子类特有的成员属性和子类特有的成员方法。**

因此一旦引用变量o指向了B类型对象（A o = new B()），
o.m()调用的永远是B的m，再也无法通过o调用A的m，哪怕强制转换都不行:((A)o).m();调用的还是B的m

### 抽象类

`abstract public class abclass{}` 必须被继承

- 抽象方法: `public abstract void func();` 不可以在非抽象类中声明抽象方法, 必须被**覆盖**, 函数体为空

### 接口 interface

`public class sonClass extends fatherClass implements interfaceClass1, interfaceClass2`

纯的抽象类

继承接口以后必须要实现接口的抽象方法

接口中的所有数据字段隐含为public static final

接口体中的所有方法隐含为public abstract

一个接口可以继承多个接口

eg. Comparable 接口, 实现public int compareTo(Object o);

### 构造函数

新建数组不会实例化数组内容

只有在没有任何构造函数时, 编译器才会自动生成无参构造函数

![截屏2021-04-25 上午1.56.01](https://tva1.sinaimg.cn/large/008i3skNgy1gpvddcdaxyj311k0f4wun.jpg)

父类的构造函数必须在子类之前完成

调用父类构造函数`super();`, 且必须为第一个语句
调用其他本身的构造函数`this();`, 且必须为第一个语句
但不能同时调用

### 初始化块

•初始化块是Java类中可以出现的第四种成员（前三种包括属性、方法、构造函数），分为实例初始化块和静态初始化块。

•实例初始化模块（instance initialization block，IIB）是一个用大括号括住的语句块，直接嵌套于类体中，不在方法内。

•它的作用就像把它放在了类中每个构造方法的最开始位置。用于初始化对象。**实例初始化块先于构造函数执行**

•作用：如果多个构造方法共享一段代码，并且每个构造方法不会调用其他构造方法，那么可以把这段公共代码放在初始化模块中。

•一个类可以有多个初始化模块，模块按照在类中出现的顺序执行

```java
public class Book{
  private static int numOfObjects;
  private String title
  private int id;
  public Book(String title){
    numOfObjects++;
    this.title = title;
  }
  public Book(int id){
    numOfObjects++;
    this.id = id
  }
}

//等价于
  
public class Book{
  private static int numOfObjects;
  private String title
  private int id;
  public Book(String title){
    this.title = title;
  }
  public Book(int id){
    this.id = id
  }
  
  {
    numOfObjects++;
  }
}

//执行次序

public class Book{
  private int id = 0;		//执行次序：1
  public Book(int id){		//执行次序：4
    this.id = id		
  }
  {
     //实例初始化块			//执行次序：2
  }
  {
     //实例初始化块			//执行次序：3
  }
}

public class Book{
  private static int id = 0;	//执行次序：1
  public Book(int id){
	 this.id = id 		    		
  }
  static {
     //静态初始化块			//执行次序：2
  }
  static {
     //静态初始化块			//执行次序：3
  }
}

```

### super

super不能用于静态上下文（即静态方法和静态初始化块里不能使用super），this也不能用于静态上下文

super.data（如果父类属性在子类可访问）

super.method(parameters)（如果父类方法在子类可访问）

不能使用super.super.p()这样的super链

如果子类中没有显式地调用父类的构造函数，那么将自动调用父类不带参数的构造函数，因为编译器会偷偷地在子类构造函数第一条语句前加上super() ；

### final

final 变量: 不能被改变

final 方法: 不能被覆盖

final class: 不能被继承

### 静态

`Math.abs();`

静态方法无法调用非静态变量, 不能调用非静态方法

静态变量: 每个类一个

静态变量会在该类任何对象初始化前初始化
静态变量会在该类任何静态方法执行前就初始化

常量 = final + static 必须初始化

## 异常

```java
try{
  MyClass a = new MyClass();
  ...
}catch(Exception e){
  ...
}finally{
  ...
}

public void method() throws Exception{
  ...
}
```

抛出的异常数量要与 catch 相匹配

catch 从小到大

## i/o

### 序列化

Serializable 接口

```java
ObjectOutputStream os = new ObjectOutputStream(new FileOutputStream("filename"));
os.writeObject(...);
os.close();
```

跳过序列化: transient

### 文件

```java
import java.io.*;
public class Son{
    public static void main(String[] args) {
        try {
            FileWriter writer = new FileWriter("filename");
            writer.write("str");
            writer.close();
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
```

## 线程

1. 实现 Runnable 类
2. `Thread thread = new Thread(runnable);`
3. `thread.start();`

Runnable 类
`public void run(){...}`

`synchronized` 修饰方法, 只能被单一线程存取

## 网络

```java
import java.io.*;
import java.net.*;
public class MySocketDemo{
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket("127.0.0.1", 8899);
        
        InputStreamReader stream = new InputStreamReader(socket.getInputStream());
        BufferedReader reader = new BufferedReader(stream);
        String msg = reader.readLine();
        
        PrintWriter writer = new PrintWriter(socket.getOutputStream());
        writer.println("msg");
        
        ServerSocket sever = new ServerSocket(8899);
        Socket severSocket = sever.accept();
    }
}
```

## 泛型

### Collections

```java
public class ToBeCompared{
  ArrayList<Song> songList = new ArrayList<Song>();
  class Comparer implements Comparator<Song>{
    public int compare(Song one, Song two){
      return one.xxxx/compareTo(two.xxx);
    }
  }
  public void go(){
    Comparer com = new Comparer();
    Collections.sort(songList, com);
  }
}
```

`Class<? extends Person> clz2;`
引用clz2可以指向Person及其子类的类型信息



## 打包

JAR: java archive

`java -jar xxx.jar`

# tips

- Math.random()生成 0-1 的值

- 数字格式化 `String s = String.format("%,.2f aha", 492.23);`

- package就是cpp中的namespace
  package语句必须出现在.java文件第一行，前面不能有注释行也不能有空白行，该.java文件里定义的所有内容（类、接口、枚举）都属于package所定义的包里。如果.java文件第一行没有package语句，则该文件定义的所有内容位于default包（缺省名字空间），但不推荐。

- hashcode https://zhuanlan.zhihu.com/p/78249480
- 数组长度为length而不是length()
- 

















