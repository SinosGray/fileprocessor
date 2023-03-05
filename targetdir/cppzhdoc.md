---
categories:
- null
date: 2023-02-02 16:00:23
sticky: 100
tags:
- cppreference
- language
- cpp
- com
- 表达式
title: cppzhdoc
---

> 

<!--more-->

# tips

- `""`运算符
- 



# 类型 type

- 对象类型是除了函数类型、引用类型以及可有 cv 限定的 void 类型以外的（可有 cv 限定的）类型（参阅 [std::is_object](https://zh.cppreference.com/w/cpp/types/is_object)）；
- [标量类型](https://zh.cppreference.com/w/cpp/named_req/ScalarType)是（可有 cv 限定的）算术、指针、成员指针、枚举和 [std::nullptr_t](http://zh.cppreference.com/w/cpp/types/nullptr_t) (C++11 起) 类型（参阅 [std::is_scalar](https://zh.cppreference.com/w/cpp/types/is_scalar)）；
- [平凡类型](https://zh.cppreference.com/w/cpp/named_req/TrivialType)（参阅 [std::is_trivial](https://zh.cppreference.com/w/cpp/types/is_trivial)）、[POD 类型](https://zh.cppreference.com/w/cpp/named_req/PODType)（参阅 [std::is_pod](https://zh.cppreference.com/w/cpp/types/is_pod)）、[字面类型](https://zh.cppreference.com/w/cpp/named_req/LiteralType)（参阅 [std::is_literal_type](https://zh.cppreference.com/w/cpp/types/is_literal_type)）和其他类别，列于[类型特征库](https://zh.cppreference.com/w/cpp/types)中，或作为[具名类型要求](https://zh.cppreference.com/w/cpp/named_req)。

## 静态类型 动态类型

对程序进行编译时分析所得到的表达式的类型被称为表达式的*静态类型*。程序执行时静态类型不会更改。

如果某个[泛左值表达式](https://zh.cppreference.com/w/cpp/language/value_category)指代某个[多态对象](https://zh.cppreference.com/w/cpp/language/object)，那么它的最终派生对象的类型被称为它的动态类型。

[基础类型](https://zh.cppreference.com/w/cpp/language/types)

# 定义

*定义*是完全定义了声明中所引入的实体的[声明](https://zh.cppreference.com/w/cpp/language/declarations)。**除了**以下情况外的声明都是定义：

- 无函数体的函数声明：
- 带有[存储类说明符](https://zh.cppreference.com/w/cpp/language/storage_duration) extern 或者[语言链接](https://zh.cppreference.com/w/cpp/language/language_linkage)说明符（例如 extern "C"）而无初始化器的所有声明：
- 在类定义中的非 inline (C++17 起) [静态数据成员](https://zh.cppreference.com/w/cpp/language/static)的声明：
- 通过[前置声明](https://zh.cppreference.com/w/cpp/language/class#.E5.89.8D.E7.BD.AE.E5.A3.B0.E6.98.8E)或通过在其他声明中使用详细类型说明符）对类名字进行的声明：
- 枚举的[不可见声明](https://zh.cppreference.com/w/cpp/language/enum)：
- [模板形参](https://zh.cppreference.com/w/cpp/language/template_parameters)的声明：
- 并非定义的函数声明中的形参声明：
- [typedef](https://zh.cppreference.com/w/cpp/language/typedef) 声明：
- [别名声明](https://zh.cppreference.com/w/cpp/language/type_alias)：
- [using 声明](https://zh.cppreference.com/w/cpp/language/using_declaration)：

## ODR one definition rule

任何变量、函数、类类型、枚举类型、[概念](https://zh.cppreference.com/w/cpp/language/constraints) (C++20 起)或模板，在每个翻译单元中都只允许有一个定义（其中部分可以有多个声明，但只允许有一个定义）。

非正式地说： 

1. 一个对象在它的值被读取（除非它是编译时常量）或写入，或它的地址被取，或者被引用绑定时，这个对象被 ODR 使用。 

2. 使用“所引用的对象在编译期未知”的引用时，这个引用被 ODR 使用。 
3. 1个函数在被调用或它的地址被取时，被 ODR 使用。 如果一个对象、引用或函数被 ODR 使用，那么程序中必须有它的定义；否则通常会有链接时错误。

## 常量表达式

定义能在编译时求值的[表达式](https://zh.cppreference.com/w/cpp/language/expressions)。

这种表达式能用做非类型模板实参、数组大小，并用于其他要求常量表达式的语境

*常量表达式（constant expression）*是

- 指代下列之一的左值 (C++14 前)泛左值 (C++14 起)*核心常量表达式*
  - 拥有静态存储期且非临时的对象，或
  - 拥有静态存储期的临时对象，但它的值满足下文对纯右值的约束(C++14 起)，或
  - 非[立即](https://zh.cppreference.com/w/cpp/language/consteval) (C++20 起)函数

- 它的值满足下列约束的纯右值*核心常量表达式*
  - 如果它的值是类类型对象，那么它的每个引用类型的非静态数据成员均指代满足上述对左值 (C++14 前)泛左值 (C++14 起)约束的实体
  - 如果它的值具有指针类型，那么它保有
    - 拥有静态存储期的对象的地址
    - 拥有静态存储期的对象的末尾后一位置的地址
    - 非[立即](https://zh.cppreference.com/w/cpp/language/consteval) (C++20 起)函数的地址
    - 空指针值
  - 如果它的值具有成员函数指针类型，那么它不代表[立即函数](https://zh.cppreference.com/w/cpp/language/consteval)(C++20 起)
  - 如果它的值具有类或数组类型，那么每个子对象均满足这些对值的约束

# 对象

C++ 程序可以创建、销毁、引用、访问并操作*对象*。

在 C++ 中，一个对象拥有这些性质：

- 大小（可以使用 [`sizeof`](https://zh.cppreference.com/w/cpp/language/sizeof) 获取）；
- 对齐要求（可以使用 [`alignof`](https://zh.cppreference.com/w/cpp/language/alignof) 获取）；
- [存储期](https://zh.cppreference.com/w/cpp/language/storage_duration)（自动、静态、动态、线程局部）；
- [生存期](https://zh.cppreference.com/w/cpp/language/lifetime)（与存储期绑定或者临时）
- [类型](https://zh.cppreference.com/w/cpp/language/type)；
- 值（可能是不确定的，例如[默认初始化](https://zh.cppreference.com/w/cpp/language/default_initialization)的非类类型）；
- [名字](https://zh.cppreference.com/w/cpp/language/identifiers#.E5.90.8D.E5.AD.97)（可选）。

## 生存期 lifetime

对象的生存期在以下时刻开始：

- 获得拥有它的类型的正确大小与对齐的存储，并且

- 完成它的初始化（如果存在）（包括不经由构造函数或经由[平凡默认构造函数](https://zh.cppreference.com/w/cpp/language/default_constructor#.E5.B9.B3.E5.87.A1.E9.BB.98.E8.AE.A4.E6.9E.84.E9.80.A0.E5.87.BD.E6.95.B0)的[默认初始化](https://zh.cppreference.com/w/cpp/language/default_initialization)），除非

  - 如果该对象是[联合体成员](https://zh.cppreference.com/w/cpp/language/union#.E6.88.90.E5.91.98.E7.94.9F.E5.AD.98.E6.9C.9F)或它的子对象，那么它的生存期在该联合体成员是联合体中的被初始化成员，或它被设为活跃才会开始，或者

  - 如果该对象内嵌于联合体对象，那么它的生存期在平凡特殊成员函数赋值或构造含有它的联合体对象时开始，或者

  - 数组对象的生存期可以因为该对象被 [std::allocator::allocate](https://zh.cppreference.com/w/cpp/memory/allocator/allocate) 分配而开始。

对象的生存期在以下时刻结束：

- 如果该对象是非类类型，那么在销毁该对象时（可能经由伪析构函数调用销毁），或者
- 如果该对象是类类型，那么在[析构函数](https://zh.cppreference.com/w/cpp/language/destructor)调用开始时，或者
- 该对象所占据的存储被释放，或被不内嵌于它的对象所重用时。

对象的生存期与它的存储的生存期相同，或者内嵌于其中，参见[存储期](https://zh.cppreference.com/w/cpp/language/storage_duration)。

[引用](https://zh.cppreference.com/w/cpp/language/reference)的生存期，从它的初始化完成之时开始，并与标量对象以相同的方式结束。

注意：被引用对象的生存期可能在引用的生存期结束之前就会结束，这会造成[悬垂引用](https://zh.cppreference.com/w/cpp/language/reference#.E6.82.AC.E5.9E.82.E5.BC.95.E7.94.A8)。

非静态数据成员和基类子对象的生存期按照[类初始化顺序](https://zh.cppreference.com/w/cpp/language/initializer_list#.E5.88.9D.E5.A7.8B.E5.8C.96.E9.A1.BA.E5.BA.8F)开始和结束。

### 临时对象的生存期

在下列情况中进行纯右值的[实质化](https://zh.cppreference.com/w/cpp/language/implicit_conversion#.E4.B8.B4.E6.97.B6.E9.87.8F.E5.AE.9E.E8.B4.A8.E5.8C.96)，从而能将它作为泛左值使用，即 (C++17 起)创建临时对象：

| [绑定引用到纯右值](https://zh.cppreference.com/w/cpp/language/reference_initialization) |            |
| ------------------------------------------------------------ | ---------- |
| 以花括号初始化器[列表初始化](https://zh.cppreference.com/w/cpp/language/list_initialization) [std::initializer_list](http://zh.cppreference.com/w/cpp/utility/initializer_list)<T> 类型的对象时 | (C++11 起) |
| 函数返回纯右值<br />创建纯右值的[类型转换](https://zh.cppreference.com/w/cpp/language/expressions#.E8.BD.AC.E6.8D.A2)（[包括](https://zh.cppreference.com/w/cpp/language/explicit_cast) T(a,b,c) 和 T{}），<br />[lambda 表达式](https://zh.cppreference.com/w/cpp/language/lambda)(C++11 起)<br />要求对初始化器进行类型转换的[复制初始化](https://zh.cppreference.com/w/cpp/language/copy_initialization)，<br />[将引用绑定](https://zh.cppreference.com/w/cpp/language/reference_initialization)到不同但可以转换的类型，或绑定到位域。 | (C++17 前) |
| 当对类类型的纯右值进行[成员访问](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E6.88.90.E5.91.98.E8.AE.BF.E9.97.AE.E8.BF.90.E7.AE.97.E7.AC.A6)时<br />当对数组纯右值进行[数组向指针](https://zh.cppreference.com/w/cpp/language/array#.E6.95.B0.E7.BB.84.E5.88.B0.E6.8C.87.E9.92.88.E9.80.80.E5.8C.96)转换或者[下标运算](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E4.B8.8B.E6.A0.87.E8.BF.90.E7.AE.97.E7.AC.A6)时<br />对 [`sizeof`](https://zh.cppreference.com/w/cpp/language/sizeof) 和 [`typeid`](https://zh.cppreference.com/w/cpp/language/typeid) 的不求值操作数<br />当纯右值被用作[弃值表达式](https://zh.cppreference.com/w/cpp/language/expressions#.E5.BC.83.E5.80.BC.E8.A1.A8.E8.BE.BE.E5.BC.8F)时<br />如果实现支持的话，在[函数调用表达式](https://zh.cppreference.com/w/cpp/language/operator_other#.E5.86.85.E5.BB.BA.E7.9A.84.E5.87.BD.E6.95.B0.E8.B0.83.E7.94.A8.E8.BF.90.E7.AE.97.E7.AC.A6)中传递或者返回[*可平凡复制* *(TriviallyCopyable)* ](https://zh.cppreference.com/w/cpp/named_req/TriviallyCopyable)的类型的对象（这对应的是在 CPU 寄存器中传递结构体的情况）时 | (C++17 起) |
| 临时对象的实质化通常会尽可能地被推迟，以免创建不必要的临时对象：参见[复制消除](https://zh.cppreference.com/w/cpp/language/copy_elision) | (C++17 起) |

所有临时对象的销毁都是在（词法上）包含创建它的位置的[完整表达式](https://zh.cppreference.com/w/cpp/language/expressions#.E5.AE.8C.E6.95.B4.E8.A1.A8.E8.BE.BE.E5.BC.8F)的求值过程的最后一步进行的，而当创建了多个临时对象时，它们是以被创建的相反顺序销毁的。即便求值过程以抛出异常而终止也是如此。

对此有两种例外情况：

- 可以通过绑定到 const 左值引用或右值引用 (C++11 起)来延长临时对象的生存期，细节见[引用初始化](https://zh.cppreference.com/w/cpp/language/reference_initialization#.E4.B8.B4.E6.97.B6.E9.87.8F.E7.94.9F.E5.AD.98.E6.9C.9F)。
- 在对数组的某个元素使用含有默认实参的默认或复制构造函数进行初始化时，对该默认实参求值所创建或复制的临时对象的生存期将在该数组的下一个元素的初始化开始之前终止。

## 存储期 storage_duration

存储类说明符是一个名字的[声明语法](https://zh.cppreference.com/w/cpp/language/declarations)的*声明说明符序列*的一部分。它与名字的[作用域](https://zh.cppreference.com/w/cpp/language/scope)一同控制名字的两个独立性质：它的“存储期”和它的“链接”。

- `auto` 或 (C++11 前)无说明符 - *自动*存储期。
- `register` - *自动*存储期，另提示编译器将此对象置于处理器的寄存器。(弃用) (C++17 前)
- `static` - *静态*或*线程*存储期和*内部*链接。
- `extern` - *静态*或*线程*存储期和*外部*链接。
- `thread_local` - *线程*存储期
- `mutable` - 不影响存储期或链接。

程序中的所有[对象](https://zh.cppreference.com/w/cpp/language/object)都具有下列存储期之一：

- 自动（automatic）存储期。这类对象的存储在外围代码块开始时分配，并在结束时解分配。未声明为 static、extern 或 thread_local 的所有局部对象均拥有此存储期。
- 静态（static）存储期。这类对象的**存储在程序开始时分配，并在程序结束时解分配。**这类对象只存在一个实例。所有在命名空间（包含全局命名空间）作用域声明的对象，加上声明带有 static 或 extern 的对象均拥有此存储期。有关拥有此存储期的对象的初始化的细节，见非局部变量与静态局部变量。
- ***线程（thread）***存储期。这类对象的存储在线程开始时分配，并在线程结束时解分配。每个线程拥有它自身的对象实例。只有声明为 `thread_local` 的对象拥有此存储期。`thread_local` 能与 `static` 或 `extern` 一同出现，它们用于调整链接。关于具有此存储期的对象的初始化的细节，见[非局部变量](https://zh.cppreference.com/w/cpp/language/initialization#.E9.9D.9E.E5.B1.80.E9.83.A8.E5.8F.98.E9.87.8F)和[静态局部变量](https://zh.cppreference.com/w/cpp/language/storage_duration#.E9.9D.99.E6.80.81.E5.B1.80.E9.83.A8.E5.8F.98.E9.87.8F)。

- ***动态（dynamic）***存储期。这类对象的存储是通过使用[动态内存分配](https://zh.cppreference.com/w/cpp/memory)函数来按请求进行分配和解分配的。关于具有此存储期的对象的初始化的细节，见 [new 表达式](https://zh.cppreference.com/w/cpp/language/new)。



## 多态对象

声明或继承了至少一个虚函数的类类型的对象是多态对象。每个多态对象中，实现都会储存额外的信息（在所有现存的实现中，如果没被编译器优化掉的话，这就是一个指针），它被用于进行[虚函数](https://zh.cppreference.com/w/cpp/language/virtual)的调用，RTTI 功能特性（[`dynamic_cast`](https://zh.cppreference.com/w/cpp/language/dynamic_cast) 和 [`typeid`](https://zh.cppreference.com/w/cpp/language/typeid)）也用它在运行时确定对象创建时所用的类型，而不管使用它的表达式是什么类型。

对于非多态对象，值的解释方式由使用对象的表达式所确定，这在编译期就已经决定了。

## 对齐

每个[对象类型](https://zh.cppreference.com/w/cpp/language/type)都具有被称为*对齐要求（alignment requirement）*的性质，它是一个整数（类型是 [std::size_t](https://zh.cppreference.com/w/cpp/types/size_t)，总是 2 的幂），表示这个类型的不同对象所能分配放置的连续相邻地址之间的字节数。

| 可以用 [`alignof`](https://zh.cppreference.com/w/cpp/language/alignof) 或 [std::alignment_of](https://zh.cppreference.com/w/cpp/types/alignment_of) 来查询类型的对齐要求。可以使用指针对齐函数 [std::align](https://zh.cppreference.com/w/cpp/memory/align) 来获取某个缓冲区中经过适当对齐的指针，还可以使用 [std::aligned_storage](https://zh.cppreference.com/w/cpp/types/aligned_storage) 来获取经过适当对齐的存储区。 | (C++11 起) |
| ------------------------------------------------------------ | ---------- |

每个对象类型在该类型的所有对象上强制该类型的对齐要求；可以使用 [`alignas`](https://zh.cppreference.com/w/cpp/language/alignas) 来要求更严格的对齐（更大的对齐要求） (C++11 起)。

为了使[类](https://zh.cppreference.com/w/cpp/language/class)中的所有非静态成员都符合对齐要求，会在一些成员后面插入一些[填充位](https://zh.cppreference.com/w/cpp/language/object#.E5.AF.B9.E8.B1.A1.E8.A1.A8.E7.A4.BA.E4.B8.8E.E5.80.BC.E8.A1.A8.E7.A4.BA)。

# 实参依赖查找

```cpp
#include <iostream>
	int main()
	{
	    std::cout << "测试\n"; // 全局命名空间中没有 operator<<，但 ADL 检验 std 命名空间，
	                           // 因为左实参在 std 命名空间中
	                           // 并找到 std::operator<<(std::ostream&, const char*)
	    operator<<(std::cout, "测试\n"); // 同上，用函数调用记法
	 
	    // 然而，
	    std::cout << endl; // 错误：'endl' 未在此命名空间中声明。
	                       // 这不是对 endl() 的函数调用，所以不适用 ADL
	 
	    endl(std::cout); // OK：这是函数调用：ADL 检验 std 命名空间，
	                     // 因为 endl 的实参在 std 中，并找到了 std::endl
	 
	    (endl)(std::cout); // 错误：'endl' 未在此命名空间声明。
	                       // 子表达式 (endl) 不是函数调用表达式
	}
```

# 关键字

## cv（const 与 volatile）类型限定符

> 暴论:
> const 在编译时处理, 常量表达式const expression在编译时就可求值

除了[函数类型](https://zh.cppreference.com/w/cpp/language/functions)或[引用类型](https://zh.cppreference.com/w/cpp/language/reference)以外的任何类型 `T`（包括不完整类型），C++ 类型系统中有另外三个独立的类型：*const-限定的* `T`、*volatile-限定的* `T` 及 *const-volatile-限定的* `T`。

注意：[数组类型](https://zh.cppreference.com/w/cpp/language/array)被当做与它的元素类型有相同的 cv 限定。

当对象创建时，所用的 cv 限定符（可以是[声明](https://zh.cppreference.com/w/cpp/language/declarations)中的 *声明说明符序列* 或 *声明符* 的一部分，或者是 [new 表达式](https://zh.cppreference.com/w/cpp/language/new)中的 *类型标识* 的一部分）决定对象的常量性或易变性，如下所示：

- ***常量对象***——类型是 *const-限定的* 对象，或常量对象的非*可变*（mutable）子对象。这种对象不能被修改：直接尝试这么做是**编译时错误**，而间接尝试这么做（例如通过到非常量类型的引用或指针修改常量对象）的行为未定义。
- ***易变对象***——类型是 *volatile-限定的* 对象，或易变对象的子对象，或常量易变对象的*可变*子对象。每次访问（读或写、调用成员函数等）易变类型之泛左值表达式[[1\]](https://zh.cppreference.com/w/cpp/language/cv#cite_note-1)，都当作[优化](https://zh.cppreference.com/w/cpp/language/as_if)方面可见的副作用（即在单个执行线程内，**易变对象访问不能被优化掉，或者与另一[先于或后于](https://zh.cppreference.com/w/cpp/language/eval_order)该易变对象访问的可见副作用进行重排序**。这使得易变对象适用于与[信号处理函数](https://zh.cppreference.com/w/cpp/utility/program/signal)而非另一执行线程交流，参阅 [std::memory_order](https://zh.cppreference.com/w/cpp/atomic/memory_order)）。试图通过非易变类型的[泛左值](https://zh.cppreference.com/w/cpp/language/value_category#.E6.B3.9B.E5.B7.A6.E5.80.BC)访问易变对象（例如，通过到非易变类型的引用或指针）的行为未定义。
- ***常量易变对象***——类型是 *const-volatile-限定的* 对象，常量易变对象的非*可变*子对象，易变对象的常量子对象，或常量对象的非*可变*易变子对象。同时表现为常量对象与易变对象。

每个 cv 限定符（const 和 volatile）在任何 cv 限定符序列中都最多只能出现一次。例如 const const 和 volatile const volatile 都不是合法的 cv 限定符序列。

**非静态成员函数**可以带 cv 限定符序列（const、volatile 或 const 和 volatile 的组合）声明，这些限定符在[函数声明](https://zh.cppreference.com/w/cpp/language/function)中的形参列表之后出现。带有不同 cv 限定符（或无限定）的函数具有不同类型，从而可以相互重载。

在有 cv 限定符的函数体内，*this 有同样的 cv 限定，例如在有 const 限定符的成员函数中只能正常地调用其他有 const 限定符的成员函数。（如果应用了 [`const_cast`](https://zh.cppreference.com/w/cpp/language/const_cast)，或通过不涉及 [`this`](https://zh.cppreference.com/w/cpp/language/this) 的访问路径，那么仍然可以调用没有 const 限定符的成员函数。）

## constexpr

`constexpr` - 指定变量或函数的值可以在[常量表达式](https://zh.cppreference.com/w/cpp/language/constant_expression)中出现

`constexpr` 说明符声明**编译时**可以对函数或变量求值。这些变量和函数（给定了合适的函数实参的情况下）即可用于需要编译期[常量表达式](https://zh.cppreference.com/w/cpp/language/constant_expression)的地方。

声明对象或非静态成员函数 (C++14 前)时使用 constexpr 说明符则同时蕴含 const。声明函数或[静态](https://zh.cppreference.com/w/cpp/language/static)成员变量 (C++17 起)时使用 constexpr 说明符则同时蕴含 inline。如果一个函数或函数模板的某个声明拥有 `constexpr` 说明符，那么它的所有声明都必须含有该说明符。

## decltype

1) 如果实参是没有括号的[标识表达式](https://zh.cppreference.com/w/cpp/language/identifiers)或没有括号的[类成员访问](https://zh.cppreference.com/w/cpp/language/operator_member_access)表达式，那么 `decltype` 产生以该表达式命名的实体的类型。如果没有这种实体或该实参指名了一组重载函数，那么程序非良构。

| 如果实参是指名某个[结构化绑定](https://zh.cppreference.com/w/cpp/language/structured_binding)的没有括号的[标识表达式](https://zh.cppreference.com/w/cpp/language/identifiers)，那么 `decltype` 产生其*被引用类型*（在关于结构化绑定声明的说明中有所描述）。 | (C++17 起) |
| ------------------------------------------------------------ | ---------- |
| 如果实参是指名某个[非类型模板形参](https://zh.cppreference.com/w/cpp/language/template_parameters#.E9.9D.9E.E7.B1.BB.E5.9E.8B.E6.A8.A1.E6.9D.BF.E5.BD.A2.E5.8F.82)的没有括号的[标识表达式](https://zh.cppreference.com/w/cpp/language/identifiers)，那么 `decltype` 生成该模板形参的类型（当该模板形参以占位符类型声明时，类型会先进行任何所需的类型推导）。 | (C++20 起) |

2) 如果实参是其他类型为 `T` 的任何表达式，且

​	a) 如果 *表达式* 的[值类别](https://zh.cppreference.com/w/cpp/language/value_category)是*亡值*，将会 `decltype` 产生 `T&&`；

​	b) 如果 *表达式* 的值类别是*左值*，将会 `decltype` 产生 `T&`；

​	c) 如果 *表达式* 的值类别是*纯右值*，将会 `decltype` 产生 `T`。

| 如果 *表达式* 是返回类类型纯右值的函数调用，或是右操作数为这种函数调用的[逗号表达式](https://zh.cppreference.com/w/cpp/language/operator_other)，那么不会对该纯右值引入临时量。 | (C++17 前) |
| ------------------------------------------------------------ | ---------- |
| 如果 *表达式* 是除了（可带括号的）[立即调用](https://zh.cppreference.com/w/cpp/language/consteval)以外的 (C++20 起)纯右值，那么不会从该纯右值[实质化](https://zh.cppreference.com/w/cpp/language/implicit_conversion#.E4.B8.B4.E6.97.B6.E9.87.8F.E5.AE.9E.E8.B4.A8.E5.8C.96)临时对象：即这种纯右值没有结果对象。 | (C++17 起) |

该类型不需要是[完整类型](https://zh.cppreference.com/w/cpp/language/type#.E4.B8.8D.E5.AE.8C.E6.95.B4.E7.B1.BB.E5.9E.8B)或拥有可用的[析构函数](https://zh.cppreference.com/w/cpp/language/destructor)，而且类型可以是[抽象的](https://zh.cppreference.com/w/cpp/language/abstract_class)。此规则不适用于其子表达式：decltype(f(g())) 中，g() 必须有完整类型，但 f() 不必。

## explicit

1) 指定构造函数或转换函数 (C++11 起)或[推导指引](https://zh.cppreference.com/w/cpp/language/class_template_argument_deduction) (C++17 起)为显式，即它不能用于[隐式转换](https://zh.cppreference.com/w/cpp/language/implicit_conversion)和[复制初始化](https://zh.cppreference.com/w/cpp/language/copy_initialization)。

| 2. explicit 说明符可以与常量表达式一同使用。函数在且只会在该常量表达式求值为 true 时是显式的。 | (C++20 起) |
| ------------------------------------------------------------ | ---------- |

explicit 说明符只能在类定义之内的构造函数或转换函数 (C++11 起)的 *声明说明符序列* 中出现。

## static

### 存储说明

`static` 说明符只能搭配（函数形参列表外的）对象声明、（块作用域外的）函数声明及匿名联合体声明。当用于声明类成员时，它会声明一个[静态成员](https://zh.cppreference.com/w/cpp/language/static)。当用于声明对象时，它指定静态存储期（除非与 `thread_local` 协同出现）。在命名空间作用域内声明时，它指定**内部链接**(名字可从当前翻译单元中的所有作用域使用。 在命名空间作用域声明的下列任何名字均具有内部链接；即未声明为 `static` 的函数具有外部链接)。

***静态（static）***存储期。这类对象的存储在程序开始时分配，并在程序结束时解分配。这类对象只存在一个实例。所有在命名空间（包含全局命名空间）作用域声明的对象，加上声明带有 `static` 或 `extern` 的对象均拥有此存储期。有关拥有此存储期的对象的初始化的细节，见[非局部变量](https://zh.cppreference.com/w/cpp/language/initialization#.E9.9D.9E.E5.B1.80.E9.83.A8.E5.8F.98.E9.87.8F)与[静态局部变量](https://zh.cppreference.com/w/cpp/language/storage_duration#.E9.9D.99.E6.80.81.E5.B1.80.E9.83.A8.E5.8F.98.E9.87.8F)。

**非局部变量**, 所有具有静态[存储期](https://zh.cppreference.com/w/cpp/language/storage_duration)的非局部变量的初始化会作为程序启动的一部分在 [main 函数](https://zh.cppreference.com/w/cpp/language/main_function)的执行之前进行（除非被延迟，见下文）。所有具有线程局部存储期的非局部变量的初始化会作为线程启动的一部分进行，按顺序早于线程函数的执行开始。对于这两种变量，初始化发生于两个截然不同的阶段：

有两种静态初始化的形式：

\1) 如果可能，那么应用[常量初始化](https://zh.cppreference.com/w/cpp/language/constant_initialization)。(设置[静态](https://zh.cppreference.com/w/cpp/language/storage_duration)变量的初值为编译时常量。)

\2) 否则非局部静态及线程局域变量会被[零初始化](https://zh.cppreference.com/w/cpp/language/zero_initialization)。

实践中：

- 常量初始化通常在编译期进行。预先被计算的对象表示会作为程序映像的一部分存储下来。如果编译器没有这样做，那么它仍然必须保证该初始化发生早于任何动态初始化。
- 零初始化的变量将被置于程序映像的 `.bss` 段，它不占据磁盘空间，并在加载程序时由操作系统以零填充。

### 静态局部变量

在块作用域声明且带有 `static` 或 `thread_local` (C++11 起) 说明符的变量拥有静态或线程 (C++11 起)存储期，但在控制首次经过它的声明时才会被初始化（除非它被[零初始化](https://zh.cppreference.com/w/cpp/language/zero_initialization)或[常量初始化](https://zh.cppreference.com/w/cpp/language/constant_initialization)，这可以在首次进入块前进行）。在其后所有的调用中，声明都会被跳过。

如果初始化[抛出异常](https://zh.cppreference.com/w/cpp/language/throw)，那么不认为变量被初始化，且控制下次经过该声明时将再次尝试初始化。

如果初始化递归地进入正在初始化的变量的块，那么行为未定义。

| 如果多个线程试图同时初始化同一静态局部变量，那么初始化严格发生一次（类似的行为也可对任意函数以 [std::call_once](https://zh.cppreference.com/w/cpp/thread/call_once) 来达成）。注意：此功能特性的通常实现均使用双检查锁定模式的变体，这使得对已初始化的局部静态变量检查的运行时开销减少为单次非原子的布尔比较。 | (C++11 起) |
| ------------------------------------------------------------ | ---------- |

块作用域静态变量的析构函数在初始化已成功的情况下[在程序退出时](https://zh.cppreference.com/w/cpp/utility/program/exit)被调用。

在相同[内联函数](https://zh.cppreference.com/w/cpp/language/inline)（可以是隐式内联）的所有定义中，函数局部的静态对象均指代在一个翻译单元中定义的同一对象，只要函数拥有外部链接。

### 静态成员

## inline

inline 说明符，在用于函数的 [声明说明符序列](https://zh.cppreference.com/w/cpp/language/declarations#.E8.AF.B4.E6.98.8E.E7.AC.A6) 时，将函数声明为一个 *内联（inline）函数*。

整个定义都在 [class/struct/union 的定义](https://zh.cppreference.com/w/cpp/language/classes)内且被附着到全局模块 (C++20 起)的函数是隐式的内联函数，无论它是成员函数还是非成员 friend 函数。

| 声明有 constexpr 的函数是隐式的内联函数。弃置的函数是隐式的内联函数：它的（弃置）定义可以在多于一个翻译单元中出现。 | (C++11 起) |
| ------------------------------------------------------------ | ---------- |
| inline 说明符，在用于具有静态存储期的变量（静态类成员或命名空间作用域变量）的 [声明说明符序列](https://zh.cppreference.com/w/cpp/language/declarations#.E8.AF.B4.E6.98.8E.E7.AC.A6) 时，将变量声明为*内联变量*。声明为 constexpr 的静态成员变量（但不是命名空间作用域变量）是隐式的内联变量。 | (C++17 起) |

### 解释

*内联函数*或*内联变量* (C++17 起)具有下列性质：

1. 内联函数或变量 (C++17 起)的定义必须在访问它的翻译单元中可达（不一定要在访问点前）。
2. 带[外部连接](https://zh.cppreference.com/w/cpp/language/storage_duration#.E5.A4.96.E9.83.A8.E8.BF.9E.E6.8E.A5)的 inline 函数或变量 (C++17 起)（例如不声明为 static）拥有下列额外属性：
   1. 内联函数或变量 (C++17 起)在程序中可以有[多于一次定义](https://zh.cppreference.com/w/cpp/language/definition#.E5.8D.95.E4.B8.80.E5.AE.9A.E4.B9.89.E8.A7.84.E5.88.99.EF.BC.88ODR.EF.BC.89)，只要每个定义都出现在不同翻译单元中（对于非静态的内联函数和变量 (C++17 起)）且所有定义等同即可。例如，内联函数或内联变量 (C++17 起)可以在被多个源文件所 #include 的头文件中定义。
   2. 它必须在每个翻译单元中都被声明为 inline 。
   3. 它在每个翻译单元中都拥有相同的地址。

在内联函数中，

- 所有函数定义中的函数局部静态对象在所有翻译单元间共享（它们都指代相同的在某一个翻译单元中定义的对象）
- 所有函数定义中所定义的类型同样在所有翻译单元中相同。

| 命名空间作用域的内联 const 变量默认具有[外部连接](https://zh.cppreference.com/w/cpp/language/storage_duration#.E5.A4.96.E9.83.A8.E8.BF.9E.E6.8E.A5)（这点与非内联非 volatile 的有 const 限定的变量不同） | (C++17 起) |
| ------------------------------------------------------------ | ---------- |

inline 关键词的本意是作为给优化器的指示器，以指示优先采用[函数的内联替换](https://en.wikipedia.org/wiki/inline_expansion)而非进行函数调用，即并不执行将控制转移到函数体内的函数调用 CPU 指令，而是代之以执行函数体的一份副本而无需生成调用。这会避免函数调用的开销（传递实参及返回结果），但它可能导致更大的可执行文件，因为函数体必须被复制多次。

因为关键词 inline 的含义是非强制的，编译器拥有对任何未标记为 inline 的函数使用内联替换的自由，和对任何标记为 inline 的函数生成函数调用的自由。这些优化选择不改变上述关于多个定义和共享静态变量的规则。

| 由于关键词 inline 对于函数的含义已经变为“容许多次定义”而不是“优先内联”，因此这个含义也扩展到了变量。 | (C++17 起) |
| ------------------------------------------------------------ | ---------- |

#### 注解

如果具有外部连接的内联函数或变量 (C++17 起)在不同翻译单元中的定义不同，那么行为未定义。

inline 说明符不能用于块作用域内（函数内部）的函数或变量 (C++17 起)声明。

inline 说明符不能重声明在翻译单元中已定义为非内联的函数或变量 (C++17 起)。

隐式生成的成员函数和任何在它的首条声明中声明为预置的成员函数，与任何其他在类定义内定义的函数一样是内联的。

如果一个内联函数在不同翻译单元中被声明，那么它的[默认实参](https://zh.cppreference.com/w/cpp/language/default_arguments)的积累集合必须在每个翻译单元的末尾相同。

在 C 中，内联函数不必在每个翻译单元声明为 inline（最多一个可以是非 inline 或 extern inline），函数定义不必相同（但如果程序依赖于调用的是哪个函数则行为未指明），且函数局部的静态变量在同一函数的不同定义间不同。

| 关于内联静态成员的额外规则见[静态数据成员](https://zh.cppreference.com/w/cpp/language/static)。内联变量消除了将 C++ 代码打包为只有头文件的库的主要障碍。 | (C++17 起) |
| ------------------------------------------------------------ | ---------- |

# 表达式

## 初等表达式

初等表达式包括以下各项：

- [`this`](https://zh.cppreference.com/w/cpp/language/this)
- 字面量（例如 2 或 "Hello, world"）
- 标识表达式，包括
  - 经过适当声明的[无限定的标识符](https://zh.cppreference.com/w/cpp/language/identifiers#.E6.97.A0.E9.99.90.E5.AE.9A.E7.9A.84.E6.A0.87.E8.AF.86.E7.AC.A6)（例如 n 或 cout），
  - 经过适当声明的[有限定的标识符](https://zh.cppreference.com/w/cpp/language/identifiers#.E6.9C.89.E9.99.90.E5.AE.9A.E7.9A.84.E6.A0.87.E8.AF.86.E7.AC.A6)（例如 [std::string::npos](https://zh.cppreference.com/w/cpp/string/basic_string/npos)），以及
  - 在[声明符](https://zh.cppreference.com/w/cpp/language/declarations#.E5.A3.B0.E6.98.8E.E7.AC.A6)中将要声明的标识符

| [lambda 表达式](https://zh.cppreference.com/w/cpp/language/lambda) | (C++11 起) |
| ------------------------------------------------------------ | ---------- |
| [折叠表达式](https://zh.cppreference.com/w/cpp/language/fold) | (C++17 起) |
| [requires 表达式](https://zh.cppreference.com/w/cpp/language/constraints) | (C++20 起) |

括号中的任何表达式也被归类为初等表达式：这确保了括号具有比任何运算符更高的优先级。括号保持值、类型和值类别不变。

# 值 value

每个 C++ [表达式](https://zh.cppreference.com/w/cpp/language/expressions)（带有操作数的操作符、字面量、变量名等）可按照两种独立的特性加以辨别：*类型*和*值类别 (value category)*。每个表达式都具有某种非引用类型，且每个表达式只属于三种基本值类别中的一种：*纯右值 (prvalue)*、*亡值 (xvalue)*、*左值 (lvalue)*。

## 泛左值 (glvalue)

（“泛化 (generalized)”的左值）是一个表达式，其值可确定某个对象或函数的标识；

*泛左值*表达式包括左值、亡值。

性质：

- 泛左值可以通过左值到右值、数组到指针或函数到指针[隐式转换](https://zh.cppreference.com/w/cpp/language/implicit_conversion)转换成纯右值。
- 泛左值可以是[多态的](https://zh.cppreference.com/w/cpp/language/object#.E5.A4.9A.E6.80.81.E5.AF.B9.E8.B1.A1)：它标识的对象的[动态类型](https://zh.cppreference.com/w/cpp/language/types#.E5.8A.A8.E6.80.81.E7.B1.BB.E5.9E.8B)不必是该表达式的静态类型。
- 泛左值可以具有[不完整类型](https://zh.cppreference.com/w/cpp/language/types#.E4.B8.8D.E5.AE.8C.E6.95.B4.E7.B1.BB.E5.9E.8B)，只要表达式中容许。

## 纯右值 (prvalue)

（“纯 (pure)”的右值）是求值符合下列之一的表达式：

- 计算某个运算符的操作数的值（这种纯右值没有*结果对象*）
- 初始化某个对象（称这种纯右值有一个*结果对象*）。

下列表达式是*纯右值表达式*：

- **（除了[字符串字面量](https://zh.cppreference.com/w/cpp/language/string_literal)之外的）[字面量](https://zh.cppreference.com/w/cpp/language/expressions#.E5.AD.97.E9.9D.A2.E9.87.8F)，例如 42、true 或 nullptr**；
- **返回类型是非引用**的函数调用或重载运算符表达式，例如 str.substr(1, 2)、str1 + str2 或 it++；
- a++ 和 a--，内建的[后置自增与后置自减](https://zh.cppreference.com/w/cpp/language/operator_incdec#.E5.86.85.E5.BB.BA.E7.9A.84.E5.90.8E.E7.BD.AE.E8.BF.90.E7.AE.97.E7.AC.A6)表达式；
- a + b、a % b、a & b、a << b，以及其他所有内建的[算术](https://zh.cppreference.com/w/cpp/language/operator_arithmetic)表达式；
- a && b、a || b、!a，内建的[逻辑](https://zh.cppreference.com/w/cpp/language/operator_logical)表达式；
- a < b、a == b、a >= b 以及其他所有内建的[比较](https://zh.cppreference.com/w/cpp/language/operator_comparison)表达式；
- &a，内建的[取地址](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E5.8F.96.E5.9C.B0.E5.9D.80.E8.BF.90.E7.AE.97.E7.AC.A6)表达式；
- a.m，[对象成员](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E6.88.90.E5.91.98.E8.AE.BF.E9.97.AE.E8.BF.90.E7.AE.97.E7.AC.A6)表达式，其中 `m` 是**成员枚举项或非静态成员函数**[[2\]](https://zh.cppreference.com/w/cpp/language/value_category#cite_note-pmfc-2)；
- p->m，内建的[指针成员](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E6.88.90.E5.91.98.E8.AE.BF.E9.97.AE.E8.BF.90.E7.AE.97.E7.AC.A6)表达式，其中 `m` 是成员枚举项或非静态成员函数[[2\]](https://zh.cppreference.com/w/cpp/language/value_category#cite_note-pmfc-2)；
- a.*mp，[对象的成员指针](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E6.88.90.E5.91.98.E6.8C.87.E9.92.88.E8.AE.BF.E9.97.AE.E8.BF.90.E7.AE.97.E7.AC.A6)表达式，其中 `mp` 是成员函数指针[[2\]](https://zh.cppreference.com/w/cpp/language/value_category#cite_note-pmfc-2)}；
- p->*mp，内建的[指针的成员指针](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E6.88.90.E5.91.98.E6.8C.87.E9.92.88.E8.AE.BF.E9.97.AE.E8.BF.90.E7.AE.97.E7.AC.A6)表达式，其中 `mp` 是成员函数指针[[2\]](https://zh.cppreference.com/w/cpp/language/value_category#cite_note-pmfc-2)；
- a, b，内建的[逗号](https://zh.cppreference.com/w/cpp/language/operator_other#.E5.86.85.E5.BB.BA.E7.9A.84.E9.80.97.E5.8F.B7.E8.A1.A8.E8.BE.BE.E5.BC.8F)表达式，其中 b 是右值；
- a ? b : c，对某些 b 和 c 的[三元条件](https://zh.cppreference.com/w/cpp/language/operator_other#.E6.9D.A1.E4.BB.B6.E8.BF.90.E7.AE.97.E7.AC.A6)表达式（细节见[定义](https://zh.cppreference.com/w/cpp/language/operator_other#.E6.9D.A1.E4.BB.B6.E8.BF.90.E7.AE.97.E7.AC.A6)）；
- 转换到非引用类型的转型表达式，例如 static_cast<double>(x)、[std::string](http://zh.cppreference.com/w/cpp/string/basic_string){} 或 (int)42；
- [`this`](https://zh.cppreference.com/w/cpp/language/this) 指针；???
- [枚举项](https://zh.cppreference.com/w/cpp/language/enum);
- 具有标量类型的非类型[模板形参](https://zh.cppreference.com/w/cpp/language/template_parameters)；

| [lambda 表达式](https://zh.cppreference.com/w/cpp/language/lambda)，例如 [](int x){ return x * x; }； | (C++11 起) |
| ------------------------------------------------------------ | ---------- |

| [requires 表达式](https://zh.cppreference.com/w/cpp/language/constraints)，例如 requires (T i) { typename T::type; }；[概念](https://zh.cppreference.com/w/cpp/language/constraints)的特化，例如 std::equality_comparable<int>。 | (C++20 起) |
| ------------------------------------------------------------ | ---------- |

性质：

- 与右值相同（见下文）。
- 纯右值不具有[多态](https://zh.cppreference.com/w/cpp/language/object#.E5.A4.9A.E6.80.81.E5.AF.B9.E8.B1.A1)：它所标识的对象的[动态类型](https://zh.cppreference.com/w/cpp/language/types#.E5.8A.A8.E6.80.81.E7.B1.BB.E5.9E.8B)始终是该表达式的类型。
- 非类非数组的纯右值不能有 [cv 限定](https://zh.cppreference.com/w/cpp/language/cv)，除非它被[实质化](https://zh.cppreference.com/w/cpp/language/implicit_conversion#.E4.B8.B4.E6.97.B6.E9.87.8F.E5.AE.9E.E8.B4.A8.E5.8C.96)以[绑定](https://zh.cppreference.com/w/cpp/language/reference_initialization)到 cv 限定类型的引用 (C++17 起)。（注意：函数调用或转型表达式可能生成非类的 cv 限定类型的纯右值，但它的 cv 限定符通常被立即剥除。）
- 纯右值不能具有[不完整类型](https://zh.cppreference.com/w/cpp/language/type#.E4.B8.8D.E5.AE.8C.E6.95.B4.E7.B1.BB.E5.9E.8B)（除了类型 void（见下文），或在 [`decltype`](https://zh.cppreference.com/w/cpp/language/decltype) 说明符中使用之外）
- 纯右值不能具有[抽象类类型](https://zh.cppreference.com/w/cpp/language/abstract_class)或它的数组类型。

## 亡值 (xvalue)

（“将亡 (expiring)”的值）是代表它的资源能够被重新使用的对象或位域的泛左值；

下列表达式是*亡值表达式*：

- a.m，[对象成员](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E6.88.90.E5.91.98.E8.AE.BF.E9.97.AE.E8.BF.90.E7.AE.97.E7.AC.A6)表达式，其中 `a` 是右值且 `m` 是对象类型的非静态数据成员；
- a.*mp，[对象的成员指针](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E6.88.90.E5.91.98.E6.8C.87.E9.92.88.E8.AE.BF.E9.97.AE.E8.BF.90.E7.AE.97.E7.AC.A6)表达式，其中 a 是右值且 `mp` 是数据成员指针；
- a ? b : c，对某些 b 和 c 的[三元条件](https://zh.cppreference.com/w/cpp/language/operator_other#.E6.9D.A1.E4.BB.B6.E8.BF.90.E7.AE.97.E7.AC.A6)表达式（细节见[定义](https://zh.cppreference.com/w/cpp/language/operator_other#.E6.9D.A1.E4.BB.B6.E8.BF.90.E7.AE.97.E7.AC.A6)）；

| 返回类型是对象的右值引用的函数调用或重载运算符表达式，例如 std::move(x)；a[n]，内建的[下标](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E4.B8.8B.E6.A0.87.E8.BF.90.E7.AE.97.E7.AC.A6)表达式，它的操作数之一是数组右值；转换到对象的右值引用类型的转型表达式，例如 static_cast<char&&>(x)； | (C++11 起) |
| ------------------------------------------------------------ | ---------- |
| 在[临时量实质化](https://zh.cppreference.com/w/cpp/language/implicit_conversion#.E4.B8.B4.E6.97.B6.E9.87.8F.E5.AE.9E.E8.B4.A8.E5.8C.96)后，任何指代该临时对象的表达式。 | (C++17 起) |

性质：

- 与右值相同（见下文）。
- 与泛左值相同（见下文）。

特别是，与所有的右值类似，亡值可以绑定到右值引用上，而且与所有的泛左值类似，亡值可以是[多态的](https://zh.cppreference.com/w/cpp/language/object#.E5.A4.9A.E6.80.81.E5.AF.B9.E8.B1.A1)，而且非类的亡值可以有 [cv 限定](https://zh.cppreference.com/w/cpp/language/cv)。

## 左值 (lvalue)

（如此称呼的历史原因是，左值可以在赋值表达式的左边出现）是非亡值的泛左值；

下列表达式是*左值表达式*：

- 变量、函数、[模板形参对象](https://zh.cppreference.com/w/cpp/language/template_parameters#.E9.9D.9E.E7.B1.BB.E5.9E.8B.E6.A8.A1.E6.9D.BF.E5.BD.A2.E5.8F.82) (C++20 起)或数据成员的**名字**，不论类型，例如 [std::cin](http://zh.cppreference.com/w/cpp/io/cin) 或 [std::endl](http://zh.cppreference.com/w/cpp/io/manip/endl)。即使变量的类型是右值引用，由它的名字构成的表达式仍是左值表达式；
- **返回类型是左值引用**的函数调用或重载运算符表达式，例如 [std::getline](http://zh.cppreference.com/w/cpp/string/basic_string/getline)([std::cin](http://zh.cppreference.com/w/cpp/io/cin), str)、[std::cout](http://zh.cppreference.com/w/cpp/io/cout) << 1、str1 = str2 或 ++it；
- a = b，a += b，a %= b，以及所有其他内建的[**赋值**及复合赋值](https://zh.cppreference.com/w/cpp/language/operator_assignment)表达式；
- **++a 和 --a**，内建的[前置自增与前置自减](https://zh.cppreference.com/w/cpp/language/operator_incdec#.E5.86.85.E5.BB.BA.E7.9A.84.E5.89.8D.E7.BD.AE.E8.BF.90.E7.AE.97.E7.AC.A6)表达式；
- *p，内建的[间接寻址](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E9.97.B4.E6.8E.A5.E5.AF.BB.E5.9D.80.E8.BF.90.E7.AE.97.E7.AC.A6)表达式；
- a[n] 和 n[a]，内建的[下标](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E4.B8.8B.E6.A0.87.E8.BF.90.E7.AE.97.E7.AC.A6)表达式，当 `a[n]` 中的一个操作数是数组左值时 (C++11 起)；
- a.m，[对象成员](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E6.88.90.E5.91.98.E8.AE.BF.E9.97.AE.E8.BF.90.E7.AE.97.E7.AC.A6)表达式，除了 `m` 是成员枚举项或非静态成员函数，或者 a 是右值而 `m` 是对象类型的非静态数据成员的情况；
- p->m，内建的[指针成员](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E6.88.90.E5.91.98.E8.AE.BF.E9.97.AE.E8.BF.90.E7.AE.97.E7.AC.A6)表达式，除了 `m` 是成员枚举项或非静态成员函数的情况；
- a.*mp，[对象的成员指针](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E6.88.90.E5.91.98.E6.8C.87.E9.92.88.E8.AE.BF.E9.97.AE.E8.BF.90.E7.AE.97.E7.AC.A6)表达式，其中 a 是左值且 `mp` 是数据成员指针；
- p->*mp，内建的[指针的成员指针](https://zh.cppreference.com/w/cpp/language/operator_member_access#.E5.86.85.E5.BB.BA.E7.9A.84.E6.88.90.E5.91.98.E6.8C.87.E9.92.88.E8.AE.BF.E9.97.AE.E8.BF.90.E7.AE.97.E7.AC.A6)表达式，其中 `mp` 是数据成员指针；
- a, b，内建的**[逗号](https://zh.cppreference.com/w/cpp/language/operator_other#.E5.86.85.E5.BB.BA.E7.9A.84.E9.80.97.E5.8F.B7.E8.BF.90.E7.AE.97.E7.AC.A6)表达式**，其中 b 是左值；
- a ? b : c，对某些 b 和 c 的[三元条件](https://zh.cppreference.com/w/cpp/language/operator_other#.E6.9D.A1.E4.BB.B6.E8.BF.90.E7.AE.97.E7.AC.A6)表达式（例如，当它们都是同类型左值时，但细节见[定义](https://zh.cppreference.com/w/cpp/language/operator_other#.E6.9D.A1.E4.BB.B6.E8.BF.90.E7.AE.97.E7.AC.A6)）；
- [**字符串字面量**](https://zh.cppreference.com/w/cpp/language/string_literal)，例如 "Hello, world!"；
- 转换到左值引用类型的转型表达式，例如 static_cast<int&>(x)；
- 具有左值引用类型的非类型[模板形参](https://zh.cppreference.com/w/cpp/language/template_parameters)；

| 返回类型是到函数的**右值引用**的函数调用表达式或重载的运算符表达式；转换到函数的右值引用类型的转型表达式，如 static_cast<void (&&)(int)>(x)。 | (C++11 起) |
| ------------------------------------------------------------ | ---------- |

性质：

- 与泛左值相同（见下文）。
- 可以通过内建的取址运算符取左值的地址：&++i[[1\]](https://zh.cppreference.com/w/cpp/language/value_category#cite_note-1) 及 &[std::endl](http://zh.cppreference.com/w/cpp/io/manip/endl) 是合法表达式。
- 可修改的左值可用作内建赋值和内建复合赋值运算符的左操作数。
- 左值可以用来[初始化左值引用](https://zh.cppreference.com/w/cpp/language/reference_initialization)；这会将一个新名字关联给该表达式所标识的对象。

## 右值 (rvalue)

（如此称呼的历史原因是，右值可以在赋值表达式的右边出现）是纯右值或者亡值。

*右值表达式*包括纯右值、亡值。

性质：

- 右值不能由内建的取址运算符取地址：&int()、&i++[[3\]](https://zh.cppreference.com/w/cpp/language/value_category#cite_note-3)、&42 及 &std::move(x) 是非法的。
- 右值不能用作内建赋值运算符及内建复合赋值运算符的左操作数。
- **右值可以用来[初始化 const 左值引用](https://zh.cppreference.com/w/cpp/language/reference_initialization)，这种情况下该右值所标识的对象的生存期被[延长](https://zh.cppreference.com/w/cpp/language/reference_initialization#.E4.B8.B4.E6.97.B6.E5.AF.B9.E8.B1.A1.E7.9A.84.E7.94.9F.E5.AD.98.E6.9C.9F)到该引用的作用域结尾。**

| 右值可以用来[初始化右值引用](https://zh.cppreference.com/w/cpp/language/reference_initialization)，这种情况下该右值所标识的对象的生存期被[延长](https://zh.cppreference.com/w/cpp/language/reference_initialization#.E4.B8.B4.E6.97.B6.E5.AF.B9.E8.B1.A1.E7.9A.84.E7.94.9F.E5.AD.98.E6.9C.9F)到该引用的作用域结尾。当被用作函数实参且该函数有两种[重载](https://zh.cppreference.com/w/cpp/language/overload_resolution)可用，其中之一接受右值引用的形参而另一个接受 const 的左值引用的形参时，右值将被绑定到右值引用的重载之上（从而，当复制与移动构造函数均可用时，以右值实参将调用它的[移动构造函数](https://zh.cppreference.com/w/cpp/language/move_constructor)，复制和移动赋值运算符与此类似）。 | (C++11 起) |
| ------------------------------------------------------------ | ---------- |

## c++11

随着移动语义引入到 C++11 之中，值类别被重新进行了定义，以区别表达式的两种独立的性质[[5\]](https://zh.cppreference.com/w/cpp/language/value_category#cite_note-5)：

- *拥有身份 (identity)*：可以确定表达式是否与另一表达式指代同一实体，例如通过比较它们所标识的对象或函数的（直接或间接获得的）地址；
- *可被移动*：[移动构造函数](https://zh.cppreference.com/w/cpp/language/move_constructor)、[移动赋值运算符](https://zh.cppreference.com/w/cpp/language/move_assignment)或实现了移动语义的其他函数重载能够绑定于这个表达式。

C++11 中：

- 拥有身份且不可被移动的表达式被称作*左值 (lvalue)*表达式；
- 拥有身份且可被移动的表达式被称作*亡值 (xvalue)*表达式；
- 不拥有身份且可被移动的表达式被称作*纯右值 (prvalue)*表达式；
- 不拥有身份且不可被移动的表达式无法使用[[6\]](https://zh.cppreference.com/w/cpp/language/value_category#cite_note-6)。

拥有身份的表达式被称作“泛左值 (glvalue) 表达式”。左值和亡值都是泛左值表达式。

可被移动的表达式被称作“右值 (rvalue) 表达式”。纯右值和亡值都是右值表达式。

## 求值顺序

求值任何表达式的任何部分，包括求值函数参数的顺序都*未指明*（除了下列的一些例外）。编译器能以任何顺序求值任何操作数和其他子表达式，并且可以在再次求值同一表达式时选择另一顺序。

C++ 中无从左到右或从右到左求值的概念。这不会与运算符的从左到右及从右到左结合性混淆：表达式 a() + b() + c() 由于 operator+ 的从左到右结合性被分析成 (a() + b()) + c()，但在运行时可以首先、最后或者在 a() 和 b() 之间对 c() 求值：

### 规则

\1) [完整表达式](https://zh.cppreference.com/w/cpp/language/expressions#.E5.AE.8C.E6.95.B4.E8.A1.A8.E8.BE.BE.E5.BC.8F)的每次值计算和副作用都按顺序早于下一个完整表达式的每个值计算和副作用。

\2) 任何[运算符](https://zh.cppreference.com/w/cpp/language/expressions#.E8.BF.90.E7.AE.97.E7.AC.A6)的各操作数的值计算（但非副作用）都按顺序早于该运算符结果的值计算（但非副作用）。

\3) 调用函数时（无论函数是否内联，且无论是否使用显式函数调用语法），与任何实参表达式或与指代被调用函数的后缀表达式关联的每个值计算和副作用，都按顺序早于被调用函数体内的每个表达式或语句的执行。

\4) 内建[后自增与后自减](https://zh.cppreference.com/w/cpp/language/operator_incdec#.E5.86.85.E5.BB.BA.E7.9A.84.E5.90.8E.E7.BD.AE.E8.BF.90.E7.AE.97.E7.AC.A6)运算符的**值计算按顺序早于它的副作用**。

\5) 内建[前自增与前自减](https://zh.cppreference.com/w/cpp/language/operator_incdec#.E5.86.85.E5.BB.BA.E7.9A.84.E5.89.8D.E7.BD.AE.E8.BF.90.E7.AE.97.E7.AC.A6)运算符的**副作用按顺序早于它的值计算**（作为由复合赋值的定义所致的隐含规则）。

\6) 内建[逻辑](https://zh.cppreference.com/w/cpp/language/operator_logical)与（AND）运算符 && 和内建逻辑或（OR）运算符 || 的第一（左）操作数的每个值计算和副作用，**按顺序早于第二（右）操作数**的每个值计算和副作用。

\7) 与[条件运算符](https://zh.cppreference.com/w/cpp/language/operator_other#.E6.9D.A1.E4.BB.B6.E8.BF.90.E7.AE.97.E7.AC.A6) **?:** 中的第一个表达式关联的每个值计算和副作用，都按顺序早于与第二或第三表达式关联的每个值计算和副作用。

\8) 内建[赋值](https://zh.cppreference.com/w/cpp/language/operator_assignment#.E5.86.85.E5.BB.BA.E7.9A.84.E7.9B.B4.E6.8E.A5.E8.B5.8B.E5.80.BC)运算符和所有内建[复合](https://zh.cppreference.com/w/cpp/language/operator_assignment#.E5.86.85.E5.BB.BA.E7.9A.84.E5.A4.8D.E5.90.88.E8.B5.8B.E5.80.BC)赋值运算符的副作用（修改左参数），都按顺序晚于左右参数的值计算（但非副作用），且按顺序早于赋值表达式的值计算（即早于返回指代被修改对象的引用之时）。

\9) 内建[逗号运算符](https://zh.cppreference.com/w/cpp/language/operator_other#.E5.86.85.E5.BB.BA.E7.9A.84.E9.80.97.E5.8F.B7.E8.BF.90.E7.AE.97.E7.AC.A6) , 的第一个（左）参数的每个值计算和副作用都按顺序早于第二个（右）参数的每个值计算和副作用。

\10) [列表初始化](https://zh.cppreference.com/w/cpp/language/list_initialization)中，在大括号中用逗号分隔的任何给定的初始化器子句的每个值计算和副作用都*按顺序早于*逗号后的任何给定的初始化器子句的每个值计算和副作用

\11) 如果某个函数调用既不按顺序早于又不按顺序晚于另一函数调用，那么它们是顺序不确定的（程序必须表现为[如同](https://zh.cppreference.com/w/cpp/language/as_if)组成不同函数调用的 CPU 指令决不会交错，即使函数被内联也是如此）。

| 规则 11 有一个例外：在 [`std::execution::par_unseq`](https://zh.cppreference.com/w/cpp/algorithm/execution_policy_tag_t) 执行策略下执行的标准库算法所作的函数调用是*无顺序的*，并且可以任意交错。 | (C++17 起) |
| ------------------------------------------------------------ | ---------- |

\12) 对分配函数（[`operator new`](https://zh.cppreference.com/w/cpp/memory/new/operator_new)）的调用相对于 [new 表达式](https://zh.cppreference.com/w/cpp/language/new)中构造函数参数的求值来说，是顺序不确定的 (C++17 前)按顺序早于它 (C++17 起)。

\13) 从函数返回时，作为求值函数调用结果的**临时量的复制初始化按顺序早于在 [return 语句](https://zh.cppreference.com/w/cpp/language/return)的操作数末尾处对所有临时量的销毁**，而这些销毁进一步*按顺序早于*对环绕 return 语句的块的所有局部变量的销毁。

| 14) 函数调用表达式中，指名函数的表达式按顺序早于每个参数表达式和每个默认实参。<br />15) 函数调用表达式中，每个形参的初始化的值计算和副作用相对于任何其他形参的初始化的值计算和副作用是顺序不确定的。<br />16) 用运算符写法进行调用时，每个重载的运算符都会遵循它所重载的内建运算符的定序规则。<br />17) 下标表达式 E1[E2] 中，E1 的每个值计算和副作用都按顺序早于 E2 的每个值计算和副作用。<br />18) 成员指针表达式 E1.*E2 或 E1->*E2 中，E1 的每个值计算和副作用都按顺序早于 E2 的每个值计算和副作用（除非 E1 的动态类型不含 E2 所指的成员）。<br />19) 移位运算符表达式 E1 << E2 和 E1 >> E2 中，E1 的每个值计算和副作用都按顺序早于 E2 的每个值计算和副作用。<br />20) 每个简单赋值表达式 E1 = E2 和每个复合赋值表达式 E1 @= E2 中，E2 的每个值计算和副作用都按顺序早于 E1 的每个值计算和副作用。<br />21) 带括号的初始化器中的逗号分隔的表达式列表中的每个表达式，如同函数调用一般求值（顺序不确定）。 | (C++17 起) |
| ------------------------------------------------------------ | ---------- |
