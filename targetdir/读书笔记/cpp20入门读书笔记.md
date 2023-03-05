---
categories:
- 读书笔记
date: 2023-01-04 12:25:28
password: null
sticky: 100
tags:
- std
- cout
- move
- optional
- rvalue
title: cpp20入门读书笔记
---

> 

<!--more-->

> 目前编译器对 c++20 只部分支持, 请谨慎使用

# 1. Basic Ideas

# 2. Introducing Fundamental Types of Data

```c++
int braced_init {15};
//The braced initializer form, however, is slightly safer when it comes to so-called narrowing conversions窄化转换 . A narrowing conversion changes a value to a type with a more limited range of values范围变小. Any such conversion thus has the potential to lose information.
//大括号初始化如果窄化转换,标准编译器会提出 warning, 其他的则不一定
int function_notation(15);
int assignment_notation = 15;
```

Type signed char is always one byte

The signed modifier is mostly optional; if omitted, your type will **be signed by default.** The only **exception to this rule is char**. While the unmodified type char does exist, it is compiler-dependent whether it is signed or unsigned.

Only use variables of the unmodified char type to store letter characters. To store numbers, you should use either signed char or unsigned char.
std::byte type to store binary data

```cpp
int counter {}; // counter starts at zero
//Zero initialization works for any fundamental type. For all fundamental numeric types, for instance, an empty braced initializer is always assumed to contain the number zero.
```

Ever since C++14,  you can use the single quote character, ', to make numeric literals more readable. Here’s an example:
 `22'333 -1'234LL 12'345ULL`

there are situations where you do need to add the correct literal suffixes, such as when you initialize a variable with type **auto**

Binary literals were introduced by the C++14 standard. You write a binary integer literal as a sequence of binary digits (0 or 1) prefixed by either **0b or 0B**, eg: `0b1010101`

`import <numbers>;`
`std::numbers::e`
`std::numbers::e_v<float>` 特定长度
`#include <cmath>`

**implicit conversions** . The way this works is that the variable of a type with the more limited range is converted to the type of the other. 
order:**signed 优先度低于 unsigned**

```cpp
long double
double
float
unsigned long long 
long long
unsigned long
long
unsigned int
int
unsigned int x {20u};
int y {30};
x-y // type is unsigned int
```

`std::format` available in cpp20

```cpp
std::cout << std::format("Pond diameter required for {} fish is {:.2} feet.\n", fish_count, pond_diameter);

//[[fill]align][sign][#][0][width][.precision][type]
int main()
{
  // Default alignment: right for numbers, left otherwise 
  std::cout << std::format("{:7}|{:7}|{:7}|{:7}|{:7}\n", 1, -.2, "str", 'c', true); 
  //Left and right alignment + custom fill character
  std::cout << std::format("{:*<7}|{:*<7}|{:*>7}|{:*>7}|{:*>7}\n", 1,-.2,"str",'c',true); 
  //Centered alignment + 0 formatting option for numbers 
  std::cout << std::format("{:^07}|{:^07}|{:^7}|{:^7}|{:^7}\n", 1, -.2, "str", 'c', true);
}
/*
1| -0.2|str |c |true
1******|-0.2***|****str|******c|***true 
0000001|-0000.2| str | c | true
*/
```

`<limits>`

```cpp
std::cout << "Maximum value of type double is " << std::numeric_limits<double>::max();
```

Type **wchar_t** is a fundamental type intended for character sets where a single character does not fit into one byte. Hence its name: wchar_t derives from wide character , because the character is “wider” than the usual one-byte character. 
By contrast, type char is referred to as “narrow” because of the limited range of character codes that are available.
You define wide-character literals in a similar way to literals of type char, but you prefix them with L. Here’s an example:` wchar_t z {L'Z'};`
use **char8_t, char16_t, or char32_t** instead. Values of these types are intended to store characters encoded as UTF-8, UTF-16, or UTF-32, their prefix are: u8, u16/u, U

## auto

**Caution** You need to be careful when using braced initializers with the auto keyword. For example, suppose you write this (notice the equals sign!):

```cpp
auto m = {10}; 
// m has type std::initializer_list<int>
```

To summarize, if your compiler properly supports **C++17**, you can use braced initialization to initialize any variable with a single value, provided you do not combine it with an assignment.
 If your compiler is not fully up-to-date yet, however, you should simply never use braced initializers with auto. Instead, either explicitly state the type or use assignment or functional notation.

# 3. Working with Fundamental Data Types

Remember that the lifetime and scope of a variable are different things. 
Lifetime is the period of execution time over which a variable survives. 
Scope is the region of program code over which the variable name can be used. It’s important not to get these two ideas confused.

 Variables defined outside of all blocks and classes are also called **globals and have global scope** (which is also called global namespace scope). This means they’re accessible in all the functions **in the source file** following the point at which they’re defined. If you define them at the beginning of a source file, they’ll be accessible throughout the file. In Chapter 11, we’ll show how to declare variables that can be used in multiple files.Global variables have static storage duration by default. use `::`to access

The **using** keyword has many uses:

- It allows you to refer to (specific or all) **enumerators** of scoped enumerations without specifying the enumeration’s name as scope.

- It allows you to refer to (specific or all) types and functions of a **namespace without specifying** the namespace’s name as scope.

- It allows you to define **aliases for other types**. In legacy code, you might still encounter typedef being used for the same purpose.

# 4. Making Decisions

# 5. Arrays and Loops

- for range loop
  
  ```cpp
  #include <iostream>
  #include <vector>
  
  int main()
  {
      std::vector<int> v = {0, 1, 2, 3, 4, 5};
  
      for (const int& i : v) // access by const reference
          std::cout << i << ' ';
      std::cout << '\n';
  
      for (auto i : v) // access by value, the type of i is int
          std::cout << i << ' ';
      std::cout << '\n';
  
      for (auto&& i : v) // access by forwarding reference, the type of i is int&
          std::cout << i << ' ';
      std::cout << '\n';
  
      const auto& cv = v;
  
      for (auto&& i : cv) // access by f-d reference, the type of i is const int&
          std::cout << i << ' ';
      std::cout << '\n';
  
      for (int n : {0, 1, 2, 3, 4, 5}) // the initializer may be a braced-init-list
          std::cout << n << ' ';
      std::cout << '\n';
  
      int a[] = {0, 1, 2, 3, 4, 5};
      for (int n : a) // the initializer may be an array
          std::cout << n << ' ';
      std::cout << '\n';
  
      for ([[maybe_unused]] int n : a)  
          std::cout << 1 << ' '; // the loop variable need not be used
      std::cout << '\n';
  
      for (auto n = v.size(); auto i : v) // the init-statement (C++20)
          std::cout << --n + i << ' ';
      std::cout << '\n';
  
      for (typedef decltype(v)::value_type elem_t; elem_t i : v)
      // typedef declaration as init-statement (C++20)
          std::cout << i << ' ';
      std::cout << '\n';
  
      for (using elem_t = decltype(v)::value_type; elem_t i : v)
      // alias declaration as init-statement (C++23)
          std::cout << i << ' ';
      std::cout << '\n';
  }
  ```

# 6. Pointers and References

> Low-level dynamic memory manipulation is synonymous for a wide range of serious hazards such as dangling pointers, multiple deallocations, deallocation mismatches, memory leaks, and so on. Our golden rule is therefore this: never use the low-level new/new[] and delete/delete[] operators directly. Containers (and std::vector<> in particular) and smart pointers are nearly always the better choice!

`float const * const pvalue {&value};`
read from right to left, * means "pointer to"

## new delete

It is perfectly **safe to apply delete on a pointer variable that holds the value nullptr**. The statement then has no effect at all. Using if tests such as the following is therefore not necessary

Note that the **delete operator frees the memory but does not change the pointer**. After the previous statement has executed, pvalue still contains the address of the memory that was allocated, but the memory is now free and may be allocated immediately to something else.
A pointer that contains such a spurious address is sometimes called a **dangling pointer.**
always resetting a pointer when you release the memory to which it points, like this:

```cpp
delete pvalue; // Release memory pointed to by pvalue 
pvalue = nullptr; // Reset the pointer
```

如果二次 delete 会报错捏

## smart pointer

Smart pointers are normally used only to store the address of memory allocated in the free store.

By far the most notable feature of a smart pointer is that you **don’t have to worry about using the delete or delete[] operator to free the memory**. It will be released automatically when it is no longer needed. This means that multiple deallocations, allocation/deallocation mismatches, and memory leaks will no longer be possible. If you consistently use smart pointers, dangling pointers will be a thing of the past as well.

Smart pointer types are defined by templates inside the` <memory> `module of the Standard Library

- `unique_ptr<T>`
  
  ```cpp
  auto pdata { std::make_unique<double>(999.0) };
  cout << pdata << endl;//指针地址
  cout << *pdata << endl;//指向的值 999.0
  
  auto pdata{std::make_unique<Foo>(Foo{1})};
  cout << pdata << endl;  // 指针地址
  cout << pdata.get() << endl;// 指针地址, 注意是.get()
  pdata.reset(new Foo{2});
  Foo* p_foo {pdata.release()};
  
  auto pvalues{ std::make_unique<double[]>(n) };
  ```
  
  In other words, there can never be two or more unique_ptr\<T\> objects pointing to the same memory address at the same time. A unique_ptr<> object is said to own what it points to exclusively. 

- `shared_ptr<T>`
  
  ```cpp
  auto pdata{ std::make_shared<double>(999.0) }
  std::shared_ptr<double> pdata2 {pdata};
  ```
  
  there can be any number of shared_ptr<T> objects that contain—or, share—the same address. 
  The **reference count** for a shared_ptr<> containing a given free store address is incremented each time a new shared_ptr<> object is created containing that address, and it’s decremented when a shared_ptr<> containing the address is destroyed or assigned to point to a different address. 
  All shared_ptr<> objects that **point to the same address** have access to the count of how many there are.

- `weak_ptr<T>`
  
  A weak_ptr\<T\> is linked to a shared_ptr\<T\> and contains the same address. Creating a weak_ptr<> does not increment the reference count associated with the linked shared_ptr<> object, though, so a weak_ptr\<\> does not prevent the object pointed to from being destroyed.
  
  One use for having weak_ptr<> objects is to avoid so- called reference cycles with shared_ptr<> objects. Conceptually, a reference cycle is where a shared_ptr<> inside an object x points to some other object y that contains a shared_ptr<>, which points back to x. 

## reference in loop

```cpp
double sum {};
unsigned count {};
double temperatures[] {45.5, 50.0, 48.2, 57.0, 63.8}; 
for (auto t : temperatures)//t is double
{
  sum += t;
  ++count; 
}

for (auto &t : temperatures) {//t is double&
        sum += t;
        ++count;
    }
```

# 7. Working with Strings

- Internally, the terminating null character is still present in the array managed by a std::string object, but only for compatibility with legacy and/or C functions. As a user of std::string, you normally do not need to know that it even exists. All string functionality transparently deals with this legacy character for you.
- You can use the **+** operator to concatenate a string object with a string literal, a character, or another string object.
- `std::to_string() std::stoi() std::stod()`

# 8. Defining Functions

- Input parameters should be reference-to-const, except for smaller values such as those of fundamental types. Returning values is generally preferred over output parameters.
- Returning a reference from a function allows the function to be used on the left of an assignment operator. Specifying the return type as a reference-to-const prevents this.

# 9. Vocabulary Types

- Use **std::optional<>** to represent any value that may or may not be present. Examples are optional inputs to a function or the result of a function that may fail. This makes your code self-documenting and therefore safer. 
  As of C++17, the Standard Library provides std::optional <>, designed to replace all implicit encodings of optional values that we showed earlier.
  
  ```cpp
  std::optional<int> 
    find_last(const std::string& s,              
              char c, 
              std::optional<int> startIndex); 
  
  std::optional<int> 
    read_int_setting(const std::string& file, 
                     const std::string& setting);
  ```
  
  We replaced it with a default value that is equal to `std::nullopt` . This special constant is defined by the Standard Library to initialize optional\<T\> values that do not (yet) have a T value assigned.
  To check:  
  you have the compiler convert the optional<> to a Boolean for you, you call the **has_value()** function, or you **compare the optional<> to nullopt** . 
  To get:
  you can either use the *** operator** or call the **value()** function. Assigning the optional<size_t> return value directly to a size_t, however, would not be possible. The compiler cannot convert values of type optional<size_t> to values of type size_t.

- Use **std::string_view** instead of const std::string& to avoid inadvertent copies of string literals or other character arrays.
  
  ```cpp
  void find_words(std::vector<std::string>& words,
                  const std::string& text,
                  const std::string& separators);
  
  int main() {
      std::string text; // The string to be searched
      std::cout << "Enter some text terminated by *:\n";
      std::getline(std::cin, text, '*');
      const std::string separators{" ,;:.\"!?'\n"};
      std::vector<std::string> words; // Words found
      find_words(
          words, text, " ,;:.\"!?'\n"); /* no more 'separators' constant! */
      //list_words(words);
  }
  // 这里, find_words 第三个参数传入的是字符串常量(const  char[])而不是引用
  //编译器会隐式临时复制, 然后传入这个复制的引用
  ```
  
  The compiler, however, will refuse any and all implicit conversions of std::string_view objects to values of type std::string (give it a try!).
  
  string_view does not provide a **c_str()** function to convert it to a const char* array.`std::string{my_view}.`

- Use **std::span\<const T\>** instead of, for instance, const  std::vector\<T\>& parameters to make the same function work as well for C-style arrays, std::array<> objects, etc.

- Similarly, use std::span\<T\> instead of std::vector\<T\>& parameters, unless you need the ability to add or remove elements.

- The reason is that there is one significant difference between a span and a view: a span <>, unlike a
  
  string_view , allows you to reassign or change the elements of the underlying array. 
  While a span<> allows you to reassign or otherwise alter elements, it does not allow you to add or remove any elements. That is, a span<> does not offer members such as push_back(), erase(), or clear(). Otherwise, a span<> could never be created for C-style arrays or std::array<> objects.

- Use std::span<(const) T,N> instead of (const) std::array<T,N>& parameters to make the same function work for C-style arrays (or other containers you know to contain at least N elements).

# 10. Function Templates

need examples

# 11. Modules and Namespaces

C++ is object oriented, in the sense that it supports the object oriented paradigm for software development.

However, differently from Java, C++ doesn't force you to group function definitions in classes: the standard C++ way for declaring a function is to just declare a function, without any class.

If instead you are talking about method declaration/definition then the standard way is to put just the declaration in an include file (normally named `.h` or `.hpp`) and the definition in a separate implementation file (normally named `.cpp` or `.cxx`). I agree this is indeed somewhat annoying and requires some duplication but it's how the language was designed (the main concept is that C++ compilation is done one unit at a time: you need the .cpp of the unit being compiled and just the .h of all the units being used by the compiled code; in other words the include file for a class must contain all the information needed to be able to generate code that uses the class). There are a LOT of details about this, with different implications about compile speed, execution speed, binary size and binary compatibility.

For quick experiments anything works... but for bigger projects the separation is something that is practically required (even if it may make sense to keep some implementation details in the public .h).

Note: Even if you know Java, C++ is a completely different language... and it's a language that cannot be learned by experimenting. The reason is that it's a rather complex language with a lot of asymmetries and apparently illogical choices, and most importantly, when you make a mistake there are no "runtime error angels" to save you like in Java... but there are instead "undefined behavior daemons".

The only reasonable way to learn C++ is by reading... no matter how smart you are there is no way you can guess what the committee decided (actually being smart is sometimes even a problem because the correct answer is illogical and a consequence of historical heritage.)

Just pick a [good book](https://stackoverflow.com/q/388242/320726) or two and read them cover to cover.

# 12. Defining Your Own Data Types

- const member functions can’t modify the member variables of a class object unless the member variables have been declared as mutable.

# 13. Operator Overloading

For a unary operator defined as a **class member function**, the operand is the class object. For a unary operator defined as a **global operator function**, the operand is the function parameter.

For a binary operator function declared **as a member of a class**, **the left operand is the class object, and the right operand is the function parameter.** For a binary operator defined by a **global operator function**, **the first parameter specifies the left operand, and the second parameter specifies the right operand**.

If you overload operators == and <=>, you get operators !=, <, >, <=, and >= all for free. In many cases you can even have the compiler generate the code for you.

# 14. Inheritance

A derived class constructor can, and often should, explicitly call constructors for its direct bases in the initialization list for the constructor. If you don’t call one explicitly, the base class’s default constructor is called. A copy constructor in a derived class, for one, should always call the copy constructor of all direct base classes.

# 15. Polymorphism

You should use the override qualifier with each member function of a derived class that overrides a virtual base class member. This causes the compiler to verify that the functions signatures in the base and derived classes are, and forever remain, the same.

```cpp
class Carton : public Box
{
public:
double volume() const override { // Function body as before...
}
// Details of the class as in Ex15_02... };
```

The **dynamic_cast<>** operator is generally used to cast from a pointer-to-a-polymorphic-base-class to a pointer- to-a-derived-class. If the pointer does not point to an object of the given derived class type, **dynamic_cast<> evaluates to nullptr**. This type check is performed dynamically, at runtime.

# 16. Runtime Errors and Exceptions

```cpp
try
{
  // Code that may throw exceptions must be in a try block...
  if (test > 5)
      throw "test is greater than 5"; // Throws an exception of type const char*
  // This code only executes if the exception is not thrown... }
  catch (const char* message)
  {
  // Code to handle the exception...
  // ...which executes if an exception of type 'char*' or 'const char*' is thrown 
        std::cout << message << std::endl; 
}
```

If an exception isn’t caught by any catch block, then the std::terminate() function is called, which immediately aborts the program execution.

The noexcept specification for a function indicates that the function does not throw exceptions. If a noexcept function does throw an exception it does not catch, std::terminate() is called.

Even if a destructor does not have an explicit noexcept specifier, the compiler will almost always generate one for you. This implies that you must never allow an exception to leave a destructor; otherwise, std::terminate() will be triggered.

The Standard Library defines a range of standard exception types in the <stdexcept> module that are derived from the std::exception class that is defined in the <exception> module.

# 17. Class Templates

Always use the copy-and-swap idiom to implement the copy assignment operator in terms of the copy constructor and a (noexcept) swap() function.
 Use the const-and-back-again idiom to implement non- const overloads in terms of const overloads of the same member function to avoid having to repeat yourself. This is an example of the DRY principle (Don’t Repeat Yourself), which advocates avoiding code duplication at all costs.

# 18. Move Semantics

std::move() can be used to convert an lvalue (such as a named variable) into an rvalue. Take care, though. Once moved, an object should normally not be used anymore.

**std::move() Does Not Move**

Make no mistake, std::move() does not move anything. All this function does is turn a given lvalue into an rvalue reference. 

If there’s no move assignment operator for Array<> to accept the rvalue, the copy assignment operator will be used instead. So, always remember, adding std::move() is of no consequence if the function or constructor that you are passing a value to has no overload with an rvalue reference parameter!

```cpp
Array<std::string> more_strings{ 2'000 }; Array<std::string>&& rvalue_ref{ std::move(more_strings) }; 
strings = rvalue_ref;
```

Notwithstanding that the rvalue_ref variable clearly has an rvalue reference type, the output of the program will show that the corresponding object is copied:
`Array of 1000 elements moved (assignment) Array of 2000 elements copied`

Every variable name expression is an lvalue, even if the type of that variable is an rvalue reference type. To move the contents of a named variable, you must therefore always add std::move():

```cpp
strings = std::move(rvalue_ref);
```

 One way to work around this duplication is to redefine the const T& overload in terms of the T&& one like so:

```cpp
template <typename T>
 void Array<T>::push_back(const T& element)
 { push_back(T{ element }); // Create a temporary, transient copy and push that }

//better way in one function
template <typename T>
void Array<T>::push_back(T element) // Pass by value (copied lvalue, or moved rvalue!) 
{
...
newArray[m_size] = std::move(element); // Move the new element...
...
}
```

how a modern C++ compiler is supposed to **handle return-by-value** (slightly simplified, as always):

- In a return statement of the form return name;, a compiler is obliged to treat name as if it were an rvalue expression, provided name is either the name of a locally defined automatic variable or that of a function parameter.

- In a return statement of the form return name;, a compiler is allowed to apply the so-called named return value optimization (NRVO), provided name is the name of a locally defined automatic variable (so not if it is that of a function parameter).

The first bullet implies that using std::move(result) in our example would be, at the very least, redundant. Even

**without the std::move(), the compiler already treats result as if it is an rvalue**. The second bullet moreover implies that return std::move(result) would prohibit the NRVO optimization. NRVO applies solely to statements of the form return result;

if the variable value in return value; has static or thread-local storage duration (see Chapter 11), you need to add std::move() if moving is what you want. This case is rare, though.
 When returning an object’s member variable, as in return m_member_variable;, std::move() is again required if you do not want the member variable to be copied.
 If the return statement contains any other lvalue expression besides the name of a single variable, then NRVO does not apply, nor will the compiler treat this lvalue as if it were an rvalue when looking for a constructor.

```cpp
Array<T>& Array<T>::operator=(Array&& rhs) noexcept {
    std::cout << "Array of " << rhs.m_size << " elements moved (assignment)"
              << std::endl;
    if (&rhs != this) // prevent trouble with self-assignments
    {
        delete[] m_elements;         // delete[] all existing elements
        m_elements = rhs.m_elements; // copy the elements pointer and the size
        m_size = rhs.m_size;
        rhs.m_elements = nullptr; // make sure rhs does not delete[] m_elements
    }
    return *this; // return lhs
}

//move and swap
template <typename T>
Array<T>& Array<T>::operator=(Array&& rhs) noexcept {
    Array<T> moved(std::move(rhs)); // move... (noexcept)
    swap(moved);                    // ... and swap (noexcept)
    return *this;                   // return lhs
}
```

# 19. First-Class Functions

lambda

```cpp
auto less{[](int x, int y) { return x < y; }};
std::cout << "Minimum element: " << *findOptimum(numbers, less) << std::endl;
```

in []

- capture by value : =, or just para name

- capture by ref : &

- specific :
  
  ```cpp
  auto counter{ [&count](int x, int y) 
      { ++count; return x < y; } 
  };
  ```
  
  Here, count is the only variable in the enclosing scope that can be accessed from within the body of the lambda.
  
  The capture default, if used, should always come first. Capture clauses such as [&counter, =] or [number_to_search_for, &] are therefore not allowed.
  
  If you use the = capture default, you are no longer allowed to capture any specific variables by value; similarly, if you use &, you can no longer capture specific variables by reference. Capture clauses such as [&,  &counter] or [=, &counter, number_to_search_for] are therefore not allowed.

# 20. Containers and Algorithms

# 21. Constrained Templates and Concepts
