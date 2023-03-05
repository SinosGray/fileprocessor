---
categories:
- 读书笔记
date: 2022-09-24 21:37:50
password: null
sticky: 100
tags:
- const
- int
- class
- static
- rhs
title: effective_cpp读书笔记
---

> 

<!--more-->

# 序

声明, 签名(参数, 返回类型), 定义(内存的地点)

构造函数 explicit 禁止隐式类型转换

copy 构造函数: 对象如何以值传递

# 少用 define

旧式编译器也许不支持上述语法，它们不允许 static 成员在其声明式上获得初值。此外所谓的 “in-class 初值设定”也只允许对**整数常量**进行。如果你的编译器不支持上述语法，你可以将初值放在定义式：

```cpp
class CostEstimate {
  private: 
  static const double FudgeFactor; //static class 常量声明 
  //位于头文件内 
}; 
const double / /static class 常量定义 CostEstimate::FudgeFactor = 1.35; //位于实现文件内
```

the enum hack

```cpp
class C{
  private:
  enum{num = 5};
  int scores[num];
}
```

用 inline 函数代替 define

```cpp
template<typename T>
inline void callWithMax(const T& a, const T&b){
  f(a>b?a:b);
}
```

# 尽可能使用 const

编译器强制实行约束

迭代器的 const 和指针一样

const_iterator 等价于 const T*

const iterator 等价于 T* const

```cpp
class C{
    int i;
    const C& operator = (const C c){
        i = c.i;
        return *this;
    }
};

int add(int& a){
    return 10;
}

int main(){
    const int ci = 10;
    int i = ci;
    C c;
    C newc = c;
  	add(ci);//error add(int a)可行
}
```

￥# const 成员函数

在函数声明最后加 const `const int add(int a)const{}`

可以重载

不会对这个类的对象的数据成员作出任何改变, 即在 const 成员函数中无法赋值

| 对象可否调用函数 | const 对象 | noconst 对象 |
| ---------------- | :--------: | :----------: |
| const 成员函数   |    yes     |     yes      |
| noconst 成员函数 |     no     |     yes      |

const 成员函数也不要提供修改途径(比如返回引用), 虽然可以通过编译

可以通过声明成员变量为 `mutable` 在 const 函数中改变对象的数据

# 对象使用前初始化

对于内置类型进行手动初始化, 对于其他类型确保构造函数对每一个成员都进行初始化

赋值!=初始化

对象成员变量的初始化发生在进入构造函数本体之前(使用初始化列表)

\1) If the constructor is for the most-derived class, virtual bases are initialized in the order in which they appear in depth-first left-to-right traversal of the base class declarations **(left-to-right refers to the appearance in base-specifier lists)**

\2) Then, direct bases are initialized in left-to-right order as they appear in this class's base-specifier list

\3) Then, non-static data member are initialized in order of declaration in the class definition.

\4) Finally, the body of the constructor is executed

```cpp
class C{
public:
    C(int i, int j, int k):b(i), a(j), c(k){
        std::cout<<a<<b<<c;
    }
    int a;
    int b;
    int c;
    
};

int main(){
    int a = 0;
    C c(a++, a++, a++);
}
//102
```



```cpp
ABEntry::ABEntry(int a):A(a), Father(a), otherFunc(){
}
```

non-local static 对象初始化: 由于 c++ 未规定这类变量的初始化顺序, 如果别的编译单元使用该对象, 可能得到未初始化的对象

因此, 需要将 non-local static 对象放到专属函数中, 使其变成 local-static 对象, 函数返回 reference

```cpp
ClassC& c(){
	static D d;
  return d;
}
```



# 默认函数

空类: 拷贝构造该函数, 拷贝操作符, 析构函数, 如果没有任何构造函数: 默认构造函数

默认拷贝: 将来源对象的每一个 non-static 成员变量拷贝到目标对象。

```cpp
class C{
public:
    string& s;
    C(string str):s(str){}
};

int main(){
    string str = "?";
    string str2 = "!";
    C c(str);
    C c2(str2);
    c = c2;//error 未定义拷贝运算符
}
//含引用, const 成员 都是如此
```

# virtual 析构函数

析构函数的运作方式是, 最深层派生(most derived)的那个 class 其虚构函数最先被调用, 然后是调用其每一个 base class 的析构函数

# 构造函数析构函数不应该调用 virtual 函数

构造函数中调用虚函数, 在基类构造函数执行时会调用基类的虚函数而不会下降到派生类

析构函数调用虚函数, 派生对象的成员变量呈现未定义状态, 编译器会无视他们, 进入基类析构函数后对象就成了一个基类对象

# operator= 返回 *this 引用, 处理自我赋值

实现连锁赋值

自我赋值:

```cpp
C& C::operator=(const C& rhs){
  if(this == &rhs) return *this;
}

//copy and swap
C& C::operator=(const C& rhs){
  C tmp(rhs);
  swap(tmp, *this);
  return *this;
}
```

# 将resource放到对象中

auto_ptr

# 对象在进入构造函数体时就已经完成初始化?



# 小心返回 reference





















￥
