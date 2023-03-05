---
categories:
- 读书笔记
date: 2023-01-16 21:06:10
sticky: 100
tags:
- chapter
- library
- ifndef
- identifier
- endif
title: cpp20实践读书笔记
---

> 

<!--more-->

# CHAPTER 1: A Crash Course in C++ and the Standard Library

## preprocessor

| PREPROCESSOR DIRECTIVE                       | FUNCTIONALITY                                                                                                                                                                           | COMMON USES                                                                                                                                                                                                                                                                                                                            |
|:-------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| #include [file]                              | The specified file is inserted into the code at the location of the directive.                                                                                                          | Almost always used to include header files so that code can make use of functionality defined elsewhere.                                                                                                                                                                                                                               |
| #define [id] [value]                         | Every occurrence of the specified identifier is replaced with the specified value.                                                                                                      | use less, most in c                                                                                                                                                                                                                                                                                                                    |
| #ifdef [id] #endif <br />#ifndef [id] #endif | Code within the ifdef (“if defined”) or ifndef (“if not defined”) blocks are conditionally included or omitted based on whether the specified identifier has been defined with #define. | Used most frequently to protect against circular includes. Each header file starts with an #ifndef checking the absence of an identifier, followed by a #define directive to define that identifier. The header file ends with an #endif. This prevents the file from being included multiple times; see the example after this table. |
| #pragma [xyz]                                | xyz is compiler dependent. Most compilers support a #pragma to display a warning or error if the directive is reached during preprocessing.                                             | See the example after this table.                                                                                                                                                                                                                                                                                                      |

```cpp
#ifndef MYHEADER_H
#define MYHEADER_H
// ... the contents of this header file 
#endif

#pragma once
```

## standard io

WARNING Keep in mind that endl inserts a new line into the stream and flushes everything currently in its buffers down the chute. 

Overusing endl, for example in a loop, is not recommended because it will have a performance
impact. On the other hand, inserting \n into the stream also inserts a new line but does not automatically flush the buffers.

# CHAPTER 2: Working with Strings and String Views

# CHAPTER 3: Coding with Style

# CHAPTER 4: Designing Professional C++ Programs

# CHAPTER 5: Designing with Objects

# CHAPTER 6: Designing for Reuse

# CHAPTER 7: Memory Management

# CHAPTER 8: Gaining Proficiency with Classes and Objects

# CHAPTER 9: Mastering Classes and Objects

# CHAPTER 10: Discovering Inheritance Techniques

# CHAPTER 11: Odds and Ends

# CHAPTER 12: Writing Generic Code with Templates

# CHAPTER 13: Demystifying C++ I/O

# CHAPTER 14: Handling Errors

# CHAPTER 15: Overloading C++ Operators

# CHAPTER 16: Overview of the C++ Standard Library

# CHAPTER 17: Understanding Iterators and the Ranges Library

# CHAPTER 18: Standard Library Containers

# CHAPTER 19: Function Pointers, Function Objects, and Lambda Expressions

# CHAPTER 20: Mastering Standard Library Algorithms

# CHAPTER 21: String Localization and Regular Expressions

# CHAPTER 22: Date and Time Utilities

# CHAPTER 23: Random Number Facilities

# CHAPTER 24: Additional Library Utilities

# CHAPTER 25: Customizing and Extending the Standard Library

# CHAPTER 26: Advanced Templates

# CHAPTER 27: Multithreaded Programming with C++

# CHAPTER 28: Maximizing Software Engineering Methods

# CHAPTER 29: Writing Efficient C++

# CHAPTER 30: Becoming Adept at Testing

# CHAPTER 31: Conquering Debugging

# CHAPTER 32: Incorporating Design Techniques and Frameworks

# CHAPTER 33: Applying Design Patterns

# CHAPTER 34: Developing Cross-Platform and Cross-Language Applications
