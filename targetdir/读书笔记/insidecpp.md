---
categories:
- 读书笔记
date: 2022-11-08 14:49:47
password: null
sticky: 100
tags:
- vtable
- class
- offset
- virtual
- member
title: insidecpp
---

> 深入理解 cpp 对象模型读书笔记(这本书原文有非常非常非常多的错误, 建议看侯捷译文)

<!--more-->

# Chapter 1. Object Lessons

##  Layout Costs for Adding Encapsulation  

主要的 overhead 来自于 virtual 机制

## 1.1 The C++ Object Model 

slot 模型

table 模型

**c++ 模型:**

- nonstatic member 在 object 内
- static member, nonstatic 和 static function 在 object 外
- 每个类有一个 vtb(?)
- 每个 object 中有 vptr 指向 vtb(多继承不止一个, 继承自几个父类就有几个 vtb)
- type_info 存储在 vtb 中用来支持 runtime 类型检查(RTTI)
- base class member 直接存储在 derived object 中
- 虚基类: The original model of virtual base class support **added a pointer into the class object for each associated virtual base class.** Alternative models have evolved that either introduce **a virtual base class table or augment the existing virtual table to maintain the location of each virtual base class** 

## 1.2. A Keyword Distinction  

关于 struct 和 class

The data members within a single access section are guaranteed within C++ to be laid out in the order of their declaration. 

**c++中多个 access setion 的 data layout 不确定**

**同样, base class 和 derived class 的成员 layout 顺序也不确定**

**virtual机制也会影响 layout**

The layout of data contained in multiple access sections, however, is left undefined. In the following declaration, for example, the C trick may or may not work, depending on whether the protected data members are placed before or after those declared private:

```cpp
class stumble {
public:
   // operations ...
protected:
   // protected stuff
private:
   /* private stuff */
   char pc[ 1 ];
};
```

因为 layout 可能产生的变化, 在 c++中使用 c 风格的最好方法是包含而不是继承

## 1.3. An Object Distinction

In the OO paradigm, the programmer manipulates an unknown instance of a bounded but infinite set of types. 

The actual type of the object addressed is not resolved in principle until **runtime** at each particular point of execution.

 In C++, this is achieved only through the manipulation of objects through **pointers and references**.

 In contrast, in the ADT paradigm the programmer manipulates **an instance of a fixed, singular type that is completely defined at the point of compilation**. 

一个指针可能指向他和他的子类中的任一种实例

```cpp
void rotate(
   X datum,
   const X *pointer,
   const X &reference )
{
   // cannot determine until run-time
   // actual instance of rotate() invoked
   (*pointer).rotate();
   reference.rotate();
   // always invokes X::rotate()
   datum.rotate();
}
main() {
   Z z; // a subtype of X
   rotate( z, &z, z );
return 0; }
```

内存对 object 的要求: nonstatic memeber 大小, padding, vitual 机制

**不同类型的指针区别在于**: That is, the type of a pointer instructs the compiler as to how to interpret the memory found at a particular address and also just how much memory that interpretation should span

eg:

- An integer pointer addressing memory location 1000 on a 32-bit machine spans the address space 1000—1003.
- The ZooAnimal pointer, if we presume a conventional 8-byte String (a 4-byte character pointer and an integer to hold the string length), spans the address
  space 1000—1015.(还有其他成员)
- ust out of curiosity, what address space does a **void*** pointer that holds memory location 1000 span? That's right, we don't know. That's why a pointer of type void* can only hold an address and not actually operate on the object it addresses.

### static_cast

`static_cast` is used for cases where you basically want to reverse an implicit conversion, with a few restrictions and additions. `static_cast` performs no runtime checks. This should be used if you know that you refer to an object of a specific type, and thus a check would be unnecessary. Example:

```cpp
void func(void *data) {
// Conversion from MyClass* -> void* is implicit
MyClass *c = static_cast<MyClass*>(data);
}

int main() {
MyClass c;
start_thread(&func, &c)  // func(&c) will be called
.join();
}
```

In this example, you know that you passed a `MyClass` object, and thus there isn't any need for a runtime check to ensure this.

### dynamic_cast

`dynamic_cast` is useful when you don't know what the dynamic type of the object is. **It returns a null pointer if the object referred to doesn't contain the type casted to as a base class** (when you cast to a reference, a `bad_cast` exception is thrown in that case).

```cpp
if (JumpStm *j = dynamic_cast<JumpStm*>(&stm)) {
...
} else if (ExprStm *e = dynamic_cast<ExprStm*>(&stm)) {
...
}
```

You can **not** use `dynamic_cast` for downcast (casting to a derived class) if the argument type is not polymorphic. For example, the following code is not valid, because `Base` **doesn't contain any virtual function:**

(如果有 virtual 可以转换)

```cpp
struct Base { };
struct Derived : Base { };
int main() {
Derived d; Base *b = &d;
dynamic_cast<Derived*>(b); // Invalid
}
```

An "up-cast" (cast to the base class) is always valid with both `static_cast` and `dynamic_cast`, and also without any cast, as an "up-cast" is an implicit conversion (assuming the base class is accessible, i.e. it's a `public` inheritance).

see also

```cpp
class L {
public: int m;
 //virtual void f(){};
};
class A : public L {public:  int a;};
class B : L {public:  int b; };
class C : public A , B {public:  int c; };

int main() {
 C c;
 C* pc = &c;
 A* pa = (A*)pc;

 C* pcc = static_cast<C*>(pa);
 //如果有 virtual 用 dynamic_cast 和 static_cast 都行
 //没有 virtual 就只能 static_cast
}
```

### Regular Cast

These casts are also called C-style cast. A C-style cast is basically identical to trying out a range of sequences of C++ casts, and taking the first C++ cast that works, without ever considering `dynamic_cast`. Needless to say, this is much more powerful as it combines all of `const_cast`, `static_cast` and `reinterpret_cast`, but it's also unsafe, because it does not use `dynamic_cast`.

In addition, C-style casts not only allow you to do this, but they also allow you to safely cast to a private base-class, while the "equivalent" `static_cast` sequence would give you a compile-time error for that.

Some people prefer C-style casts because of their brevity. I use them for numeric casts only, and use the appropriate C++ casts when user defined types are involved, as they provide stricter checking.

base = derived

**When a base class object is directly initialized or assigned with a derived class object,** the derived object is **sliced** to fit into the available memory resources of the base type. There is nothing of the derived type remaining. Polymorphism is not present, and an observant compiler can resolve an invocation of a virtual function through the object at compile time, thus by-passing the virtual mechanism. This can be a significant performance win if the virtual function is defined as inline.



# Chapter 2. The Semantics of Constructors  

**Global objects** are guaranteed to have **their associated memory "zeroed out" at program start-up.** 

Local objects allocated on the program stack and heap objects allocated on the free-store do not have their associated memory zeroed out; rather, the memory retains the arbitrary bit pattern of its previous use.

> 大原则: 用户定义了构造函数就 compiler 就不生成隐含默认构造函数

## 2.1. Default Constructor Construction  

compiler 只做 implement 需要的事情, 只有当 implementation 需要的时候才会生成 default constructor

例如 int, 指针等不会被implicit默认构造函数初始化(值为随机值)

以上这种默认构造属于 trivial

一下几种情况默认构造函数是 nontrivial

### 含有有默认构造函数的成员

```cpp
class C{
  //public:
  C(){cout<<"?";}
};
struct Base {
    C c;
};

int main() {
    Base b;
  //ERROR: call to implicitly-deleted default constructor of 'Base'
  //但是书上说会生成隐含默认构造函数, 这个函数会初始化 C 但是不会初始化 int 指针等类型的成员. 有点矛盾?
}
//问题解决: C 的构造函数要是 public 就不会报错, 和书上一致
```

The language requires that the (member) constructors be invoked in the order of member declaration within the class.(before user code)

#### 关于初始化顺序

```cpp
int main() {
    using namespace std;
    class C1 {
      public:
        C1() { cout << "C1"; }
    };

    class C2 {
      public:
        C2() { cout << "C2"; }
    };

    class Base {
        C2 c2;
        C1 c;

      public:
        Base() : c2() { cout << "Base"; }
    };

    class Derive : Base {
        C1 c;

      public:
        Derive() { cout << "Derive"; }
    };
    Derive d;
}
//C2C1BaseC1Derive
//可见, 隐含成员构造和构造列表的顺序都取决于成员声明的顺序
//同时, 基类初始化在成员初始化之前
```

### 基类有默认构造函数

### 类中有虚函数

1. 类里声明或者继承了一个虚函数
2. 基类链里有虚函数

这种情况需要对 vptr 进行初始化

### 有虚基类

Virtual base class implementations vary widely across compilers. However, what is common to each implementation is the need to make the virtual base class location within each derived class object available at runtime.**

例如在 cfront 中

```cpp
class X { public: int i; };
class A : public virtual X   { public: int j; };
class B : public virtual X   { public: double d; };
class C : public A, public B { public: int k; };
// cannot resolve location of pa->X::i at compile-time
void foo( const A* pa ) { pa->i = 1024; }
main() {
   foo( new A );
   foo( new C );
   // ...
}

// possible compiler transformation
void foo( const A* pa ) { pa->__vbcX->i = 1024; }
```



## 2.2. Copy Constructor Construction  

三种情况:

```cpp
class X { ... };
   X x;

// explicit initialization of one class object with another
X xx = x;

//as argument
foo(x);

//as return 
X foo_bar(){
  X xx;
  return xx;
}
```

### default memberwise initialization

Default memberwise initialization **copies the value of each built-in or derived data member** (such as a pointer or an array) from the one class object to another. A **member class object, however, is not copied; rather, memberwise initialization is recursively applied**.

### bitwise copy semantics

```cpp
class Word {
public:
   Word( const char* );
   ~Word() { delete [] str; }
private:
   int   cnt;
	 char *str; 
};
//不需要生成 copy 构造函数, 不涉及函数调用

class Word {
public:
   Word( const String& );
   ~Word();
private:
   int    cnt;
   String str;
};
//生成 copy 构造函数来调用 string 的拷贝构造函数
```

一下四种情况的 class 不存在 bitwise copy semantics

1. 含有成员, 他有拷贝构造函数(无论是自定义的还是编译器组装的)
2. 继承自有拷贝构造函数的类(自定义的或编译器的)
3. 声明了虚函数
4. 继承链里有虚基类

### 有虚函数的重置 vptr

只要引入了 vptr 就不存在逐位拷贝语义, 需要拷贝构造函数来初始化 vptr

如果是 derived = base, vptr 不能直接复制, 必须要正确初始化 vptr

### 关于虚基类 subobject

构造函数需要: 初始化 vptr, 定位 基类 subobject

还是 derived = base

## 2.3. Program Transformation Semantics 

参数传入 和 结果返回 copy 构造函数

```cpp
void foo( X x0 );
// Pseudo C++ code compiler generated temporary
X __temp0;
// compiler invocation of copy constructor
__temp0.X::X ( xx );
// rewrite function call to take temporary
foo( __temp0 );

void bar();
// Pseudo C++ Code
void bar( X& __result ){
	 X xx;
   // compiler generated invocation of default constructor
   xx.X::X();
   // compiler generated invocation
   // of copy constructor
   __result.X::X( xx );
   return; 
}

// Pseudo C++ Code 不再调用 copy 构造函数, NRV
void bar( X &__result )
{
   __result.X::X( y, z );
   return; 
}

//测试
class B {
  public:
    B() {std::cout<<"default"<<std::endl;}
    B(const B& b) { std::cout << "copy" << std::endl; }
};

B fun(B b) { return b; }
int main() {
    using namespace std;

    B b;
    B b_copy = fun(b);
    cout<<endl;
    fun(b);
}
/*
default
copy
copy

copy
copy
*/
```

## 2.4. Member Initialization List

必须使用初始化列表:

reference, const, invoke base or member 带参构造函数

在函数体内的用赋值初始化会导致

- 先调用默认构造函数
- 再调用赋值
- 摧毁临时对象

The compiler iterates over the initialization list, **inserting the initializations in the proper order within the constructor prior to any explicit user code.**其顺序是根据声明顺序而不是 list 的顺序

最好不要在 list 里调用成员函数, 因为不清楚这个成员函数是否依赖其他成员

**问: this 指针何时初始化?**



# Chapter 3. The Semantics of Data

空类对象; sizeof == 1

## 3.1. The Binding of a Data Member  

**the analysis of the member function's body is delayed until the entire class declaration is seen.** 

This is not true of the argument list of the member function, however. **Names within the argument list are still resolved in place at the point they are first encountered.** 

Nonintuitive bindings between extern and nested type names, therefore, can still occur. In the following code fragment, for example, the type of length in both member function signatures resolves to that of the global typedef—that is, to int. When the subsequent declaration of the nested typedef of length is encountered,
the Standard requires that the earlier bindings be flagged as illegal:

```cpp
typedef int length;
class Point3d
{
public:
   // oops: length resolves to global
   // ok: _val resolves to Point3d::_val
   mumble( length val ) { _val = val; }
   length mumble() { return _val; }
   // ...
private:
   // length must be seen before its first
   // reference within the class.  This
   // declaration makes the prior reference illegal.
   typedef float length;
   length _val;
   // ...
};
```



## 3.2. Data Member Layout

The Standard requires **within an access section** (the private, public, or protected section of a class declaration) only that **the members be set down such that "later members have higher addresses within a class object"** . That is, the members are not required to be set down contiguously. What might intervene between the declared members? Alignment constraints on the type of a succeeding member may require padding. This is true both of C and C++, and in this case, the member layout of the two languages is in current practice the same.

The Standard also allows the **compiler the freedom to order the data members within multiple access sections** within a class in whatever order it sees fit. 

即一个 access session 里是根据生命顺序 layout, 不同 session 之间是取决于编译器的

多个 session 不占用额外空间

## 3.3. Access of a Data Member

### static member

实例和指针访问效率相同

### nonstatic member

Access of a nonstatic data member requires **the addition of the beginning address of the class object with the offset location of the data member.** 

```cpp
c.m_y;
-->
&c + (&C::m_y - 1) ;
???
//注意里面的 -1 是为了让编译系统区分
//a pointer to data member that is addressing the first member of a class and no member.
```

nonstatic member 的 offset 在编译时就知道, 访问时间与 c 无异

当有虚基类的时候, 访问会慢

## 3.4. Inheritance and the Data Member 

> (原文有较大问题请看侯捷译文) 

继承可能会导致 padding, 这些 padding 如果被优化会导致 base = derived 无法实现

多重继承时, derived 和第二及后续 base 的关系是不自然的

Base* bp = &derived_object; 起始地址是一样的

Seconde_base* bsp = &derived_object; 起始地址不一样需要调整

但是除了直接offset调整, 还需要增加是否为空的判断, 否则可能得到一个 sizeof 值

### 虚继承的菱形继承问题

A class containing one or more virtual base class subobjects, such as istream, is divided into two regions: **an invariant region and a shared region**. **Data within the invariant region remains at a fixed offset from the start of the object regardless of subsequent derivations**. So members within the invariant region can be accessed directly. **The shared region represents the virtual base class subobjects. The location of data within the shared region fluctuates with each derivation.** **So members within the shared region need to be accessed indirectly.** What has varied among implementations is the method of indirect access. 

即独立区域是直接访问, 共享区域是间接访问

a pointer to each virtual base class is inserted within each derived class object. 

一种方法是 is to place not the address but the offset of the virtual base class within the virtual function table.

把到共享区的 offset 存在各个基类的 vptr[-1]里

![IMG_4316F8EDE31A-1](https://tva1.sinaimg.cn/large/008vxvgGly1h81e4fo2zpj316y0u00vt.jpg)

## 3.5. Object Member Efficiency  

几个表格

## 3.6. Pointer to Data Members

```cpp
string Student::*p = &Student::m_name;
Student s;
s.*p;
成员指针的值是 object 中成员的 offset + 1
+1 是为了区分一个指针指向的是 没有 member 还是 第一个 member
但是实际编译器里并没有体现+1, 这条可以忽略
both the compiler (and the user) must remember to subtract 1 before
actually using the value to address a member.

```

一些表格

# Chapter 4. The Semantics of Function  

## 4.1. Varieties of Member Invocation

member function 会被编译器内化为nonmember函数的形式

虚函数可以被声明为 inline, 当通过 object 直接调用时不会触发多态, 会使用 inline

## 4.2. Virtual Member Functions

(纯虚函数如果没有被实现是不会分配虚函数 index 的)

虚函数在 runtime 期间的调用

- 我不知道 ptr 所指的真正类型, 但是我知道 ptr指向一个 vtb
- 我不知道哪个func()是哪个函数, 但我知道所有的 func()在 vtb 中都有一个相同的 index

### 多重继承下的 virtual

```cpp
Base2 *pbase2 = new Derived;
//编译时会改写为
Derived *tmp = new Derived;
Base2 *pbase2 = tmp? tmp+sizeof(Base1):0;
```

多重继承下 一个 derived class 内含有 n-1 个额外的vtb, n 表示 base 个数, 所以单一继承不会有多余的 vtb 产生

![截屏2022-11-12 09.57.52](https://tva1.sinaimg.cn/large/008vxvgGly1h824194s4kj30w20sm0ww.jpg)

多重继承影响虚拟机制的情况有以下三种

1. 用 base2 指针调用 derived virtual function

2. 用 derived 指针调用 base2 virtual function

3. ```cpp
   Base2 *pb2_1 = new Derived;
   Base2 *pb2_2 = pb2_1->clone();
   ```

## 4.3. Function Efficiency  

inline 为程序优化提供更多可能

表格

## 4.4. Pointer-to-Member Functions 

不涉及虚拟的成员函数指针

```cpp
double(Point::*pmf)() = &Point::x;
(origin.*pmf)();
```

虚拟成员函数指针

它的值只是索引而不是真实地址

```cpp
(*ptr->vptr[(int)pmf])(ptr);
```

## 4.5. Inline Functions

处理一个 inline 函数两个各个阶段

1. 分析函数定义(分析其复杂度, 判断是否能成为 inline)
2. 判断在调用处是否可以扩展

```cpp
inline int
min( int i, int j )
{
   return i < j ? i : j;
}

inline int
bar()
{
   int minval;
   int val1 = 1024;
   int val2 = 2048;
/*(1)*/minval = min( val1, val2 );
/*(2)*/minval = min( 1024, 2048 );
/*(3)*/minval = min( foo(), bar()+1 );
   return minval;
}

(1) simple argument substitution
minval = val1 < val2 ? val1 : val2;
(2) constant folding following substitution
minval = 1024;
(3) side-effects and introduction of temporary(避免表达式重复求值)
int t1;
int t2;
minval =
   ( t1 = foo() ), ( t2 = bar() + 1 ),
   t1 < t2 ? t1 : t2;
```

inline 函数可能会导致大量的扩展码(局部变量)

# Chapter 5. Semantics of Construction, Destruction, and Copy. 

Presence of a Pure Virtual destructor

Presence of a Virtual Specification

Presence of const within a Virtual Specification

## 5.1. Object Construction without Inheritance 

## 5.2. Object Construction under Inheritance  

编译器扩充构造函数:

1. virtual base 构造函数
2. 所有的 base 构造函数(按照声明顺序)
3. vptr
4. 成员初始化列表, 未出现在初始化列表的 member 默认构造函数

在自我拷贝时要注意判断筛选(释放资源前)

```cpp
if(this == &rhs) return *this;
```

虚拟多继承中对于virtual base class 的构造函数调用(会被调用多次?) 可以被安排到 most_derived 的构造函数中

vptr 初始化位置在 base 构造函数之后, 初始化列表之前

在 class 的 constructor 的 member initialization list 中调用该 class 的一个虚拟函数，安全吗？就实际而言，将该函数运行于其 class's data member 的初始化行动中，总是安全的。vptr保证能够在 member initialization list 被扩展之前，由编译器正确设定好．但是在语意上这可能是不安全的，因为函数本身可能还得依 赖未被设立初值的 members.

## 5.3. Object Copy Semantics  

> 关于几种拷贝
>
> **Member-wise Copy**
>
> Is when you visit each member and explicitly copy it, i**nvoking its copy constructor**. It is the proper way of copying things. If done right, it is tantamount to a deep-copy, because each member whose copy constructor you invoke will (or should) in turn perform member-wise copy of its own members, and so on. The opposite is bit-wise copy, which is a hack, see below.
>
> **Bit-wise Copy**
>
> Is a specific form of shallow copy. It is when you **simply copy the bits of the source class to the target class, using `memcpy()`** or something similar. **Constructors are not invoked**, so you tend to get a class which *appears* to be all right but things start breaking in horrible ways as soon as you start using it. This is the opposite of member-wise copy, and is a quick and dirty hack that can sometimes be used when we know that there are no constructors to be invoked and no internal structures to be duplicated. For a discussion of what may go wrong with this, see this Q&A: [C++ bitwise vs memberwise copying?](https://stackoverflow.com/questions/15123516/c-bitwise-vs-memberwise-copying)
>
> **Shallow Copy**
>
> **Refers to copying just the immediate members of an object,** without duplicating whatever structures are pointed by them. It is what you get when you do a bit-wise copy.
>
> (Note that there is no such thing as "shadow copy". I mean, there is such a thing, in file systems, but that's probably *not* what you had in mind.)
>
> **Deep Copy**
>
> Refers to not only copying the immediate members of an object, but also duplicating whatever structures are pointed by them. It is what you normally get when you do member-wise copy.
>
> **To summarize:**
>
> There are two categories:
>
> - Shallow Copy
> - Deep Copy
>
> Then, there are two widely used techniques:
>
> - Bit-wise Copy (a form of Shallow Copy)
> - Member-wise Copy (a form of Deep Copy, if done right.)
>
> As for the hear-say about someone who said something and someone who said something else: bit-wise copy is definitely always shallow copy. Member-wise copy is usually deep copy, but you may of course foul it up, so you may be thinking that you are making a deep copy while in fact you are not. Proper member-wise copy relies on having proper copy constructors.
>
> Finally:
>
> **The default copy constructor will do a bit-wise copy if the object is known to be trivially copyable, or a member-wise copy if not.** However, the compiler does not always have enough information to perform a proper copy of each member. For example, a pointer is copied by making a copy of the pointer, not by making a copy of the pointed object. That's why you should generally not rely on the compiler providing you with a default copy constructor when your object is not trivially copyable.
>
> A user-supplied constructor may do whatever type of copy the user likes. Hopefully, the user will choose wisely and do a member-wise copy.

只有当默认行为导致语义不安全是才需要设计一个拷贝运算符

默认拷贝运算符 在以下情况下不会表现出 bitwise copy 语义

1. member 有拷贝运算符
2. base 有拷贝运算符
3. 有 虚函数
4. 继承自 virtual base

注意虚拟继承的拷贝运算符

## 5.4. Object Efficiency.  

一些表格

## 5.5. Semantics of Destruction

如果 class 没有定义 destructor，那么只有在 class 内带的 member object （或 是 class 自己的 base class）拥有 destructor 的情况下，编译器才会自动合成出一 个来．否则，destructor 会被视为不需要，也就不需被合成（当然更不需要被调用）．

析构函数扩展顺序:(存疑)

1. 析构函数体
2. member 析构函数, 声明逆序
3. 有 vptr, 重设相关的 vtb
4. nonvirtual base, 声明逆序
5. virtual base

# Chapter 6. Runtime Semantics  

## 6.1. Object Construction and Destruction  

### global

C++ 保证，一定会在 main 函数中第一次用到 identity 之前，把 identity 构造 出来，而在 main 函数结束之前把 identity 摧毁掉。像 identity 这样的所谓 global object 如果有 constructor 和 destructor 的话，我们说它需要静态的初始化 操作和内存释放操作。

![截屏2022-11-12 22.24.49](https://tva1.sinaimg.cn/large/008vxvgGly1h82pmhob14j30pg0buab2.jpg)

### local static

编译器的策略之一就是，无条件地在程序起始（startup）时构造出对象来． 然而这会导致所有的 local static class obiects 都在程序起始时被初始化，即使它们 所在的那个函数从不曾被调用过。因此，只在 identity 被调用时才把 matidentity 构造起来，是比较好的做法（现在的 C++ Standard 已经强制要求这 一点）。

### array of object

如果定义了构造函数, 会依次调用

析构函数同上

## 6.2. Operators new and delete  

new 步骤

1. 分配内存
2. 设立初值

```cpp
int *pi;
if(pi = __new(sizeof(int)))
	*pi = 5;
```

delete 步骤

```cpp
if(pi!=0)
  __delete(pi);
//此时 pi 不会被清零
```



## 6.3. Temporary Objects

临时性对象的被摧毁，应该是对完整表达式（full-expression）求值过程中的 最后一个步骤．该完整表达式造成临时对象的产生(Section 12.2).

⋯凡含有表达式执行结果的临时性对象，应该存留到 object 的初始化操作 完成为止。

如果一个临时性对象被绑定于一个 reference，对象将残留，直到被初始化之 reference 的生命结束，或直到临时对象的生命范時（scope)结束——视哪一种情 先到达而定.

# Chapter 7. On the Cusp of the Object Model  

## 7.1. Templates  

?

## 7.2. Exception Handling  

## 7.3. Runtime Type Identification  

## 7.4. Efficient, but Inflexible?

# 关于作用域



# 多继承

## 多个基类

```cpp
//成员函数
C* pc;
pc->bf(2);
//需要变换 this 指针
bf_F1B( (B*) ( (char*) pc + delta(B) ), 2);

//同理类型转换
C* pc;
B* pb;
pb = (B*)pc;
//变换
pb = (B*) ( (char*) pc + delta(B));

//为了避免 0 指针
C* pc = 0;
B* pb = 0;
pb = pc;
pb = (pc==0)? 0 : (B*) ( (char*) pc + delta(B));
```

```cpp
//涉及到歧义时
pc->A::f();
pc->B::f();
```

## 虚函数

```cpp
struct vtbl_entry {
    void (*fct)();
	  int delta;
};
-----------------
|                | vtbl:
| vptr ..........>--------------------- 
| A part         | |C::f| 0           |
|                | --------------------
-----------------
|                | vtbl:
| vptr ..........>--------------------- 
| B part         | |C::f| -delta(B)   |
|                | |B::g| 0           | 
----------------- --------------------- 
|                |
| C part         | 
|                |
-----------------
  
pb->f();    
// call of C::f:
// register vtbl_entry* vt = &pb->vtbl[index(f)];
// (*vt->fct) ( (B*) ( (char*)pb + vt->delta) )
// 这意味着每个基类都需要一个 vptr

```

## multiple inclusion

下面这段代码是编译通过的

```cpp
class L {public: int m; };
class A : public L {public:  int a;};
class B : L {public:  int b; };
class C : A , B {public:  int c; };

int main() {
    C c;
    C* pc = &c;
    L* pl = (L*)(A*)pc;
}
```

## 虚基类

In other words, there must be a way of specifying that a base class must give rise to **only one object in the final derived class even if it is mentioned as a base class several times**. To distinguish this usage from independent multiple inheritance such base classes are specified to be virtual:

```cpp
class L {
  public: int m;
    //virtual void f(){};
};
class A : public L {public:  int a;};
class B : L {public:  int b; };
class C : public A , B {public:  int c; };

int main() {
    C c;
    C* pc = &c;
    A* pa = (A*)pc;
    
    C* pcc = static_cast<C*>(pa);
    //如果有 virtual 用 dynamic_cast 和 static_cast 都行
    //没有 virtual 就只能 static_cast
}
```



```cpp
-----------------
.........  |
. | AW part| g
v |        |
. ----------------- 
.........  |
. | BW part| f
v |        |
. -----------------
. |        |
. | CW part| h
v |        |        vtbl:
. ----------------- ------------------------------
.>| vptr .........> |BW::f | delta(BW)-delta(W) | 
  |        |        |AW::g | -delta(W)          |
  | W part | fghk   |CW::h | -delta(W)          |
  |        |        | W::k | 0                  |
  ----------------- ------------------------------
//the delta stored with a function pointer in a vtbl is the delta of the class defining the function minus the delta of the class for which the vtbl is constructed.
这个表似乎有点问题, delta 和 vptr 没弄明白
```



```cpp
class W {
    virtual void f();
    virtual void g();
    virtual void h();
    virtual void k();
};
class AW : virtual W { void g(); ... };
class BW : virtual W { void f(); ... };
class CW : AW , BW { void h(); ... };
CW* pcw = new CW;
pcw->f();        // BW::f()
pcw->g();        // AW::g()
pcw->h();        // CW::h()
((AW*)pcw)->f(); // BW::f();
```

## 构造函数与析构函数

Constructors are executed in the order they appear in the list of bases **except that a virtual base is always constructed before classes derived from it.** A virtual base is always constructed (once only) by its "most derived" class. For example:

```cpp
class V { V(); V(int); ... };
class A: virtual V { A(); A(int); ... }; 
class B: virtual V { B(); B(int), ... };
class C : A, B     { C(); C(int), ... };

V v(1); A a(2); B b(3); C c(4);
```

## overhead

The overhead in using this scheme is:

1. One subtraction of a constant for each use of a member in a base class that is included as the second

   or subsequent base.

2. One word per function in each vtbl (to hold the delta).

3. One memory reference and one subtraction for each call of a virtual function.

4. One memory reference and one subtraction for access of a base class member of a virtual base class.

Note that overheads [1] and [4] are only incurred where multiple inheritance is actually used,
 but overheads [2] and [3] are incurred for each class with virtual functions and for each virtual function call even when multiple inheritance is not used. 
Overheads [1] and [4] are only incurred when members of a second or subsequent base are accessed ‘‘from the outside’’; a member function of a virtual base class does not incur special overheads when accessing members of its class.

This implies that except for [2] and [3] you pay only for what you actually use; [2] and [3] impose a minor overhead on the virtual function mechanism even where only single inheritance is used. This latter overhead could be avoided by using an alternative implementation of multiple inheritance, but I don’t know of such an implementation that is also faster in the multiple inheritance case and as portable as the scheme described here.

Fortunately, these overheads are not significant. The time, space, and complexity overheads imposed on the compiler to implement multiple inheritance are not noticeable to the user.



# memory layout

http://www.vishalchovatiya.com/memory-layout-of-cpp-object/

## object

```cpp
class X {
    int     x;
    float   xx;
public:
    X() {}
    ~X() {}
    void printInt() {}
    void printFloat() {}
};
```

```
      |------------------------| <------ X class object memory layout
      |        int X::x        |
      |------------------------|  stack segment
      |       float X::xx      |       |   
      |------------------------|       |
      |                        |      \|/
      |                        |    
      |                        |
------|------------------------|----------------
      |         X::X()         | 
      |------------------------|       |   
      |        X::~X()         |       |
      |------------------------|      \|/
      |      X::printInt()     |  text segment
      |------------------------|
      |     X::printFloat()    |
      |------------------------|
      |                        |            
```

## +virtual func + static member

```cpp
class X {
    int         x;
    float       xx;
    static int  count;
public:
    X() {}
    virtual ~X() {}
    virtual void printAll() {}
    void printInt() {}
    void printFloat() {}
    static void printCount() {}
};
```

```
      |------------------------| <--- X class object memory layout
      |        int X::x        |
stack |------------------------|
  |   |       float X::xx      |                      
  |   |------------------------|      |---|--------------------------|
  |   |         X::_vptr       |------|   |       type_info X        |
 \|/  |------------------------|          |--------------------------|
      |           o            |          |    address of X::~X()    |
      |           o            |          |--------------------------|
      |           o            |          | address of X::printAll() |
      |                        |          |--------------------------|
      |                        |
------|------------------------|------------
      |  static int X::count   |      /|\
      |------------------------|       |
      |           o            |  data segment           
      |           o            |       |
      |                        |      \|/
------|------------------------|------------
      |        X::X()          | 
      |------------------------|       |   
      |        X::~X()         |       |
      |------------------------|       | 
      |      X::printAll()     |      \|/ 
      |------------------------|  text segment
      |      X::printInt()     |
      |------------------------|
      |     X::printFloat()    |
      |------------------------|
      | static X::printCount() |
      |------------------------|
      |                        |
```



## +inheritance

```cpp
class X {
    int     x;
    string str;
public:
    X() {}
    virtual ~X() {}
    virtual void printAll() {}
};

class Y : public X {
    int     y;
public:
    Y() {}
    ~Y() {}
    void printAll() {}
};
```

```
      |------------------------------| <---- Y class object memory layout
      |          int X::x            |
stack |------------------------------|
  |   |              int string::len |
  |   |string X::str ----------------|
  |   |            char* string::str |         
 \|/  |------------------------------|      |--|--------------------------|
      |           X::_vptr           |------|  |       type_info Y        |
      |------------------------------|         |--------------------------|
      |          int Y::y            |         |    address of Y::~Y()    |
      |------------------------------|         |--------------------------|
      |               o              |         | address of Y::printAll() |
      |               o              |         |--------------------------|
      |               o              |              
------|------------------------------|--------
      |           X::X()             | 
      |------------------------------|       |   
      |           X::~X()            |       |
      |------------------------------|       | 
      |         X::printAll()        |      \|/ 
      |------------------------------|  text segment
      |           Y::Y()             |
      |------------------------------|
      |           Y::~Y()            |
      |------------------------------|
      |         Y::printAll()        |
      |------------------------------|
      |      string::string()        |
      |------------------------------|
      |      string::~string()       |
      |------------------------------|
      |      string::length()        |
      |------------------------------|
      |                              |
```

## + multiple inheritance

```cpp
class X {
public:
    int     x;
    virtual ~X() {}
    virtual void printX() {}
};

class Y {
public:
    int     y;
    virtual ~Y() {}
    virtual void printY() {}
};

class Z : public X, public Y {
public:
    int     z;
    ~Z() {}
    void printX() {}
    void printY() {}
    void printZ() {}
};
```



```
      |------------------------------| <----- Z class object memory layout
stack |          int X::x            |         
  |   |------------------------------|           |--------------------------|      
  |   |          X:: _vptr           |---------->|       type_info Z        |
  |   |------------------------------|           |--------------------------|
 \|/  |          int Y::y            |           |    address of Z::~Z()    |
      |------------------------------|           |--------------------------|
      |          Y:: _vptr           |------|    |   address of Z::printX() |
      |------------------------------|      |    |--------------------------|
      |          int Z::z            |      |    |--------GUARD_AREA--------|    
      |------------------------------|      |    |--------------------------|
      |              o               |      |--->|       type_info Z        |
      |              o               |           |--------------------------|
      |              o               |           |    address of Z::~Z()    |
      |                              |           |--------------------------|
------|------------------------------|---------  |   address of Z::printY() |
      |           X::~X()            |       |   |--------------------------|  
      |------------------------------|       |          
      |          X::printX()         |       |        
      |------------------------------|       |         
      |           Y::~Y()            |      \|/        
      |------------------------------|  text segment
      |          Y::printY()         |                
      |------------------------------|                
      |           Z::~Z()            |                
      |------------------------------|                
      |          Z::printX()         |                
      |------------------------------|                
      |          Z::printY()         |                
      |------------------------------|                
      |          Z::printZ()         |                
      |------------------------------|                
      |                              |                           
```

## + virtual inheritance

```cpp
class X { int x; };
class Y : public virtual X { int y; };
class Z : public virtual X { int z; };
class A : public Y, public Z { int a; };
```

```
                  |                |          
 Y class  ------> |----------------| <--- A class object memory layout
sub-object        |   Y::y         |          
                  |----------------|       |--------------------------| 
                  |   Y::_vptr_Y   |--|    |    offset of X           | 
 Z class  ------> |----------------|  |--> |--------------------------|     
sub-object        |   Z::z         |       |//offset(20) starts from Y|     
                  |----------------|       |--------------------------|  
                  |   Z::_vptr_Z   |--|       
                  |----------------|  |        
 A sub-object --> |   A::a         |  |    |--------------------------| 
                  |----------------|  |    |    offset of X           | 
 X class -------> |   X::x         |  |--> |--------------------------|          
 shared           |----------------|       |//offset(12) starts from Z|           
 sub-object       |                |       |--------------------------|           
```



# GCC virtual table

## VTable Notes on Multiple Inheritance in GCC C++ Compiler v4.0.1

[http://www.cse.wustl.edu/~mdeters/seminar/fall2005/mi.html#basics]
The Basics: Single Inheritance

## Simple Multiple Inheritance

Now consider multiple inheritance:

> ```
> class A {
> public:
>   int a;
>   virtual void v();
> };
> 
> class B {
> public:
>   int b;
>   virtual void w();
> };
> 
> class C : public A, public B {
> public:
>   int c;
> };
> ```

In this case, objects of type C are laid out like this:

> ```
>                            +-----------------------+
>                            |     0 (top_offset)    |
>                            +-----------------------+
> c --> +----------+         | ptr to typeinfo for C |
>       |  vtable  |-------> +-----------------------+
>       +----------+         |         A::v()        |
>       |     a    |         +-----------------------+
>       +----------+         |    -8 (top_offset)    |
>       |  vtable  |---+     +-----------------------+
>       +----------+   |     | ptr to typeinfo for C |
>       |     b    |   +---> +-----------------------+
>       +----------+         |         B::w()        |
>       |     c    |         +-----------------------+
>       +----------+
> ```

*...but why?* Why two vtables in one? Well, think about typesubstitution. If I have a pointer-to-C, I can pass it to a functionthat expects a pointer-to-A or to a function that expects apointer-to-B. If a function expects a pointer-to-A and I want to passit the value of my variable `c` (of type pointer-to-C), I'malready set. Calls to `A::v()` can be made through the(first) vtable, and the called function can access the member`a` through the pointer I pass in the same way as it canthrough *any* pointer-to-A.

However, if I pass the value of my pointer variable `c` to a function that expects a pointer-to-B, we *also* need asubobject of type B in our C to refer it to. This is why we have thesecond vtable pointer. We can pass the pointer value`(c + 8 bytes)` to the function that expectsa pointer-to-B, and it's all set: it can make calls to`B::w()` through the (second) vtable pointer, and accessthe member `b` through the pointer we pass in the same wayas it can through any pointer-to-B.

Note that this "pointer-correction" needs to occur for called methodstoo. Class C inherits `B::w()` in this case. When`w()` is called on through a pointer-to-C, the pointer(which becomes the **this** pointer inside of `w()` needsto be adjusted. This is often called *this pointer adjustment*.

In some cases, the compiler will generate a *thunk* to fix up theaddress. Consider the same code as above but this time C overrides B'smember function `w()`:

> ```
> class A {
> public:
>   int a;
>   virtual void v();
> };
> 
> class B {
> public:
>   int b;
>   virtual void w();
> };
> 
> class C : public A, public B {
> public:
>   int c;
>   void w();
> };
> ```

C's object layout and vtable now look like this:

```
                           +-----------------------+
                           |     0 (top_offset)    |
                           +-----------------------+
c --> +----------+         | ptr to typeinfo for C |
      |  vtable  |-------> +-----------------------+
      +----------+         |         A::v()        |
      |     a    |         +-----------------------+
      +----------+         |         C::w()        |
      |  vtable  |---+     +-----------------------+
      +----------+   |     |    -8 (top_offset)    |
      |     b    |   |     +-----------------------+
      +----------+   |     | ptr to typeinfo for C |
      |     c    |   +---> +-----------------------+
      +----------+         |    thunk to C::w()    |
                           +-----------------------+
```



Now, when `w()` is called on an instance of C through apointer-to-B, the thunk is called. What does the thunk do? Let'sdisassemble it (here, with gdb):

> ```
> 0x0804860c <_ZThn8_N1C1wEv+0>:  addl   $0xfffffff8,0x4(%esp)
> 0x08048611 <_ZThn8_N1C1wEv+5>:  jmp    0x804853c <_ZN1C1wEv>
> ```

So it merely adjusts the **this** pointer and jumps to`C::w()`. All is well.

But doesn't the above mean that B's vtable always points to this`C::w()` thunk? I mean, if we have a pointer-to-B that is legitimately a B (not a C), we don't want to invoke the thunk, right?

## **attention!!!!**

<u>**Right. The above embedded vtable for B in C is special to the B-in-C case.B's regular vtable is normal and points to `B::w()` directly.**</u>



The Diamond: Multiple Copies of Base Classes (non-virtual inheritance)

Okay. Now to tackle the really hard stuff. Recall the usual problem ofmultiple copies of base classes when forming an inheritance diamond:

> ```
> class A {
> public:
>   int a;
>   virtual void v();
> };
> 
> class B : public A {
> public:
>   int b;
>   virtual void w();
> };
> 
> class C : public A {
> public:
>   int c;
>   virtual void x();
> };
> 
> class D : public B, public C {
> public:
>   int d;
>   virtual void y();
> };
> ```

Note that D inherits from both B and C, and B and C both inherit from A.This means that D has *two* copies of A in it. The object layoutand vtable embedding is what we would expect from the previous sections:

> ```
>                            +-----------------------+
>                            |     0 (top_offset)    |
>                            +-----------------------+
> d --> +----------+         | ptr to typeinfo for D |
>       |  vtable  |-------> +-----------------------+
>       +----------+         |         A::v()        |
>       |     a    |         +-----------------------+
>       +----------+         |         B::w()        |
>       |     b    |         +-----------------------+
>       +----------+         |         D::y()        |
>       |  vtable  |---+     +-----------------------+
>       +----------+   |     |   -12 (top_offset)    |
>       |     a    |   |     +-----------------------+
>       +----------+   |     | ptr to typeinfo for D |
>       |     c    |   +---> +-----------------------+
>       +----------+         |         A::v()        |
>       |     d    |         +-----------------------+
>       +----------+         |         C::x()        |
>                            +-----------------------+
> ```

Of course, we expect A's data (the member `a`) to exist twicein D's object layout (and it is), and we expect A's virtual member functionsto be represented twice in the vtable (and `A::v()` is indeedthere). Okay, nothing new here.

The Diamond: Single Copies of Virtual Bases

But what if we apply *virtual* inheritance? C++ virtual inheritanceallows us to specify a diamond hierarchy but be guaranteed only one copyof virtually inherited bases. So let's write our code this way:

> ```
> class A {
> public:
>   int a;
>   virtual void v();
> };
> 
> class B : public virtual A {
> public:
>   int b;
>   virtual void w();
> };
> 
> class C : public virtual A {
> public:
>   int c;
>   virtual void x();
> };
> 
> class D : public B, public C {
> public:
>   int d;
>   virtual void y();
> };
> ```

All of a sudde 1000 n things get a *lot* more complicated. If we can onlyhave *one* copy of A in our representation of D, then we can nolonger get away with our "trick" of embedding a C in a D (and embeddinga vtable for the C part of D in D's vtable). But how can we handle theusual type substitution if we can't do this?

Let's try to diagram the layout:

> ```
>                                    +-----------------------+
>                                    |   20 (vbase_offset)   |
>                                    +-----------------------+
>                                    |     0 (top_offset)    |
>                                    +-----------------------+
>                                    | ptr to typeinfo for D |
>                       +----------> +-----------------------+
> d --> +----------+    |            |         B::w()        |
>       |  vtable  |----+            +-----------------------+
>       +----------+                 |         D::y()        |
>       |     b    |                 +-----------------------+
>       +----------+                 |   12 (vbase_offset)   |
>       |  vtable  |---------+       +-----------------------+
>       +----------+         |       |    -8 (top_offset)    |
>       |     c    |         |       +-----------------------+
>       +----------+         |       | ptr to typeinfo for D |
>       |     d    |         +-----> +-----------------------+
>       +----------+                 |         C::x()        |
>       |  vtable  |----+            +-----------------------+
>       +----------+    |            |    0 (vbase_offset)   |
>       |     a    |    |            +-----------------------+
>       +----------+    |            |   -20 (top_offset)    |
>                       |            +-----------------------+
>                       |            | ptr to typeinfo for D |
>                       +----------> +-----------------------+
>                                    |         A::v()        |
>                                    +-----------------------+
> ```

Okay. So you see that A is now embedded in D in essentially thesame way that other bases are. But it's embedded in D rather than inits directly-derived classes.

Construction/Destruction in the Presence of Multiple Inheritance

How is the above object constructed in memory when the object itself isconstructed? And how do we ensure that a partially-constructed object(and its vtable) are safe for constructors to operate on?

Fortunately, it's all handled very carefully for us. Say we're constructinga new object of type D (through, for example, `new D`).First, the memory for the object is allocated in the heap and a pointerreturned. D's constructor is invoked, but before doing any D-specificconstruction it call's A's constructor on the object (after adjusting the**this** pointer, of course!). A's constructor fills in the A partof the D object as if it were an instance of A.

> ```
> d --> +----------+
>       |          |
>       +----------+
>       |          |
>       +----------+
>       |          |
>       +----------+
>       |          |       +-----------------------+
>       +----------+       |     0 (top_offset)    |
>       |          |       +-----------------------+
>       +----------+       | ptr to typeinfo for A |
>       |  vtable  |-----> +-----------------------+
>       +----------+       |         A::v()        |
>       |    a     |       +-----------------------+
>       +----------+
> ```

Control is returned to D's constructor, which invokes B's constructor.(Pointer adjustment isn't needed here.) When B's constructor is done,the object looks like this:

> ```
>                                              B-in-D
>                           +-----------------------+
>               
> 1000
>             |   20 (vbase_offset)   |
>                           +-----------------------+
>                           |     0 (top_offset)    |
>                           +-----------------------+
> d --> +----------+        | ptr to typeinfo for B |
>       |  vtable  |------> +-----------------------+
>       +----------+        |         B::w()        |
>       |    b     |        +-----------------------+
>       +----------+        |    0 (vbase_offset)   |
>       |          |        +-----------------------+
>       +----------+        |   -20 (top_offset)    |
>       |          |        +-----------------------+
>       +----------+        | ptr to typeinfo for B |
>       |          |   +--> +-----------------------+
>       +----------+   |    |         A::v()        |
>       |  vtable  |---+    +-----------------------+
>       +----------+
>       |    a     |
>       +----------+
> ```

*But wait... B's constructor modified the A part of the object by changingit's vtable pointer!* How did it know to distinguish this kind of B-in-Dfrom a B-in-something-else (or a standalone B for that matter)? Simple.The *virtual table table* told it to do this. This structure,abbreviated VTT, is a table of vtables used in construction. In our case,the VTT for D looks like this:

> ```
>                                                                   B-in-D
>                                                +-----------------------+
>                                                |   20 (vbase_offset)   |
>             VTT for D                          +-----------------------+
> +-------------------+                          |     0 (top_offset)    |
> |    vtable for D   |-------------+            +-----------------------+
> +-------------------+             |            | ptr to typeinfo for B |
> | vtable for B-in-D |-------------|----------> +-----------------------+
> +-------------------+             |            |         B::w()        |
> | vtable for B-in-D |-------------|--------+   +-----------------------+
> +-------------------+             |        |   |    0 (vbase_offset)   |
> | vtable for C-in-D |-------------|-----+  |   +-----------------------+
> +-------------------+             |     |  |   |   -20 (top_offset)    |
> | vtable for C-in-D |-------------|--+  |  |   +-----------------------+
> +-------------------+             |  |  |  |   | ptr to typeinfo for B |
> |    vtable for D   |----------+  |  |  |  +-> +-----------------------+
> +-------------------+          |  |  |  |      |         A::v()        |
> |    vtable for D   |-------+  |  |  |  |      +-----------------------+
> +-------------------+       |  |  |  |  |
>                             |  |  |  |  |                         C-in-D
>                             |  |  |  |  |      +-----------------------+
>                             |  |  |  |  |      |   12 (vbase_offset)   |
>                             |  |  |  |  |      +-----------------------+
>                             |  |  |  |  |      |     0 (top_offset)    |
>                             |  |  |  |  |      +-----------------------+
>                             |  |  |  |  |      | ptr to typeinfo for C |
>                             |  |  |  |  +----> +-----------------------+
>                             |  |  |  |         |         C::x()        |
>                             |  |  |  |         +-----------------------+
>                             |  |  |  |         |    0 (vbase_offset)   |
>                             |  |  |  |         +-----------------------+
>                             |  |  |  |         |   -12 (top_offset)    |
>                             |  |  |  |         +-----------------------+
>                             |  |  |  |         | ptr to typeinfo for C |
>                             |  |  |  +--
> 1000
> -----> +-----------------------+
>                             |  |  |            |         A::v()        |
>                             |  |  |            +-----------------------+
>                             |  |  |
>                             |  |  |                                    D
>                             |  |  |            +-----------------------+
>                             |  |  |            |   20 (vbase_offset)   |
>                             |  |  |            +-----------------------+
>                             |  |  |            |     0 (top_offset)    |
>                             |  |  |            +-----------------------+
>                             |  |  |            | ptr to typeinfo for D |
>                             |  |  +----------> +-----------------------+
>                             |  |               |         B::w()        |
>                             |  |               +-----------------------+
>                             |  |               |         D::y()        |
>                             |  |               +-----------------------+
>                             |  |               |   12 (vbase_offset)   |
>                             |  |               +-----------------------+
>                             |  |               |    -8 (top_offset)    |
>                             |  |               +-----------------------+
>                             |  |               | ptr to typeinfo for D |
>                             +----------------> +-----------------------+
>                                |               |         C::x()        |
>                                |               +-----------------------+
>                                |               |    0 (vbase_offset)   |
>                                |               +-----------------------+
>                                |               |   -20 (top_offset)    |
>                                |               +-----------------------+
>                                |               | ptr to typeinfo for D |
>                                +-------------> +-----------------------+
>                                                |         A::v()        |
>                                                +-----------------------+
> ```

D's constructor passes a pointer into D's VTT to B's constructor (in thiscase, it passes in the address of the first B-in-D entry). And, indeed,the vtable that was used for the object layout above is a special vtableused just for the construction of B-in-D.

Control is returned to the D constructor, and it calls the C constructor(with a VTT address parameter pointing to the "C-in-D+12" entry). WhenC's constructor is done with the object it looks like this:

> ```
>                                                                            B-in-D
>                                                         +-----------------------+
>                                                         |   20 (vbase_offset)   |
>                                                         +-----------------------+
>                                                         |     0 (top_offset)    |
>                                                         +-----------------------+
>                                                         | ptr to typeinfo for B |
>                     +---------------------------------> +-----------------------+
>                     |                                   |         B::w()        |
>                     |                                   +-----------------------+
>                     |                          C-in-D   |    0 (vbase_offset)   |
>                     |       +-----------------------+   +-----------------------+
> d --> +----------+  |       |   12 (vbase_offset)   |   |   -20 (top_offset)    |
>       |  vtable  |
> 1000
> --+       +-----------------------+   +-----------------------+
>       +----------+          |     0 (top_offset)    |   | ptr to typeinfo for B |
>       |    b     |          +-----------------------+   +-----------------------+
>       +----------+          | ptr to typeinfo for C |   |         A::v()        |
>       |  vtable  |--------> +-----------------------+   +-----------------------+
>       +----------+          |         C::x()        |
>       |    c     |          +-----------------------+
>       +----------+          |    0 (vbase_offset)   |
>       |          |          +-----------------------+
>       +----------+          |   -12 (top_offset)    |
>       |  vtable  |--+       +-----------------------+
>       +----------+  |       | ptr to typeinfo for C |
>       |    a     |  +-----> +-----------------------+
>       +----------+          |         A::v()        |
>                             +-----------------------+
> ```

As you see, C's constructor again modified the embedded A's vtable pointer.The embedded C and A objects are now using the special construction C-in-Dvtable, and the embedded B object is using the special construction B-in-Dvtable. Finally, D's constructor finishes the job and we end up with thesame diagram as before:

> ```
>                                    +-----------------------+
>                                    |   20 (vbase_offset)   |
>                                    +-----------------------+
>                                    |     0 (top_offset)    |
>                                    +-----------------------+
>                                    | ptr to typeinfo for D |
>                       +----------> +-----------------------+
> d --> +----------+    |            |         B::w()        |
>       |  vtable  |----+            +-----------------------+
>       +----------+                 |         D::y()        |
>       |     b    |                 +-----------------------+
>       +----------+                 |   12 (vbase_offset)   |
>       |  vtable  |---------+       +-----------------------+
>       +----------+         |       |    -8 (top_offset)    |
>       |     c    |         |       +-----------------------+
>       +----------+         |       | ptr to typeinfo for D |
>       |     d    |         +-----> +-----------------------+
>       +----------+                 |         C::x()        |
>       |  vtable  |----+            +-----------------------+
>       +----------+    |            |    0 (vbase_offset)   |
>       |     a    |    |            +-----------------------+
>       +----------+    |            |   -20 (top_offset)    |
>                       |            +-----------------------+
>                       |            | ptr to typeinfo for D |
>                       +----------> +-----------------------+
>                                    |         A::v()        |
>                                    +-----------------------+
> ```

Destruction occurs in the same fashion but in reverse. D's destructoris invoked. After the user's destruction code runs, the destructorcalls C's destructor and directs it to use the relevant portion of D'sVTT. C's destructor manipulates the vtable pointers in the same wayit did during construction; that is, the relevant vtable pointers nowpoint into the C-in-D construction vtable. Then it runs the user'sdestruction code for C and returns control to D's destructor, whichnext invokes B's destructor with a reference into D's VTT. B'sdestructor sets up the relevant portions of the object to refer intothe B-in-D construction vtable. It runs the user's destruction codefor B and returns control to D's destructor, which finally invokes A'sdestructor. A's destructor changes the vtable for the A portion ofthe object to refer into the vtable for A. Finally, control returnsto D's destructor and d 1000 estruction of the object is complete. Thememory once used by the object is returned to the system.

Now, in fact, the story is somewhat more complicated. Have you everseen those "in-charge" and "not-in-charge" constructor and destructorspecifications in GCC-produced warning and error messages or inGCC-produced binaries? Well, the fact is that there can be twoconstructor implementations and up to three destructor implementations.

An "in-charge" (or *complete object*) constructor is one thatconstructs virtual bases, and a "not-in-charge" (or *baseobject*) constructor is one that does not. Consider our aboveexample. If a B is constructed, its constructor needs to call A'sconstructor to construct it. Similarly, C's constructor needs toconstruct A. However, if B and C are constructed as part of aconstruction of a D, their constructors *should not* constructA, because A is a virtual base and D's constructor will take care ofconstructing it exactly once for the instance of D. Consider thecases:

- If you do a `new A`, A's "in-charge" constructor isinvoked to construct A.
- When you do a `new B`, B's "in-charge" constructor isinvoked. It will call the "not-in-charge" constructor for A.
- `new C` is similar to `new B`.
- A `new D` invokes D's "in-charge" constructor. Wewalked through this example. D's "in-charge" constructor calls the"not-in-charge" versions of A's, B's, and C's constructors (in thatorder).

An "in-charge" destructor is the analogue of an "in-charge"constructor---it takes charge of destructing virtual bases. Similarly,a "not-in-charge" destructor is generated. But there's a third one aswell. An "in-charge deleting" destructor is one that *deallocates*the storage as well as destructing the object. So when is one called in preferenceto the other?

Well, there are two kinds of objects that can be destructed---those allocated on thestack, and those allocated in the heap. Consider this code (given our diamond hierarchywith virtual-inheritance from before):

> ```
> D d;            // allocates a D on the stack and constructs it
> D *pd = new D;  // allocates a D in the heap and constructs it
> /* ... */
> delete pd;      // calls "in-charge deleting" destructor for D
> return;         // calls "in-charge" destructor for stack-allocated D
> ```

We see that the actual delete operator isn't invoked by the code doingthe delete, but rather by the in-charge deleting destructor for theobject being deleted. Why do it this way? Why not have the callercall the in-charge destructor, then delete the object? Then you'd haveonly two copies of destructor implementations instead of three...

Well, the compiler *could* do such a thing, but it would be morecomplicated for other reasons. Consider this code (assuming a virtual destructor,which you always use, right?...*right?!?*):

> ```
> D *pd = new D;  // allocates a D in the heap and constructs it
> C *pc = d;      // we have a pointer-to-C that points to our heap-allocated D
> /* ... */
> delete pc;      // call destructor thunk through vtable, but what about delete?
> ```

If you didn't have an "in-charge deleting" variety of D's destructor, thenthe delete operation would need to adjust the pointer just like the destructorthunk does. Remember, the C object is embedded in a D, and so ourpointer-to-C above is adjusted to point into the middle of our D object.We can't just delete this pointer, since it isn't the pointer that wasreturned by `malloc()` when we constructed it.

So, if we didn't have an in-charge deleting destructor, we'd have to havethunks to the delete operator (and represent them in our vtables), or somethingelse similar.

Thunks, Virtual and Non-Virtual

This section not written yet.

Multiple Inheritance with Virtua 1000 l Methods on One Side

Okay. One last exercise. What if we have a diamond inheritance hierarchywith virtual inheritance, as before, but only have virtual methods along oneside of it? So:

> ```
> class A {
> public:
>   int a;
> };
> 
> class B : public virtual A {
> public:
>   int b;
>   virtual void w();
> };
> 
> class C : public virtual A {
> public:
>   int c;
> };
> 
> class D : public B, public C {
> public:
>   int d;
>   virtual void y();
> };
> ```

In this case the object layout is the following:

> ```
>                                    +-----------------------+
>                                    |   20 (vbase_offset)   |
>                                    +-----------------------+
>                                    |     0 (top_offset)    |
>                                    +-----------------------+
>                                    | ptr to typeinfo for D |
>                       +----------> +-----------------------+
> d --> +----------+    |            |         B::w()        |
>       |  vtable  |----+            +-----------------------+
>       +----------+                 |         D::y()        |
>       |     b    |                 +-----------------------+
>       +----------+                 |   12 (vbase_offset)   |
>       |  vtable  |---------+       +-----------------------+
>       +----------+         |       |    -8 (top_offset)    |
>       |     c    |         |       +-----------------------+
>       +----------+         |       | ptr to typeinfo for D |
>       |     d    |         +-----> +-----------------------+
>       +----------+
>       |     a    |
>       +----------+
> ```


