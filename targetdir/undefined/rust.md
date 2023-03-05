---
categories:
- undefined
date: 2023-03-03 15:26:37
sticky: 100
tags:
- tuple
- tuples
- println
- let
- pair
title: rust
---

> 

<!--more-->

# 安装

```shell
curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
```

检查环境变量

```
export PATH="$HOME/.cargo/bin:$PATH"
```



## ?

```rust
// Tuples can be used as function arguments and as return values
fn reverse(pair: (i32, bool)) -> (bool, i32) {
    // `let` can be used to bind the members of a tuple to variables
    let (int_param, bool_param) = pair;

    (bool_param, int_param)
  //return ?
}

// The following struct is for the activity.
#[derive(Debug)]//?
struct Matrix(f32, f32, f32, f32);

fn main() {
    // A tuple with a bunch of different types
    let long_tuple = (1u8, 2u16, 3u32, 4u64,
                      -1i8, -2i16, -3i32, -4i64,
                      0.1f32, 0.2f64,
                      'a', true);

    // Values can be extracted from the tuple using tuple indexing
    println!("long tuple first value: {}", long_tuple.0);// .
    println!("long tuple second value: {}", long_tuple.1);

    // Tuples can be tuple members
    let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);

    // Tuples are printable
  //{:?}?
    println!("tuple of tuples: {:?}", tuple_of_tuples);
    
    // But long Tuples (more than 12 elements) cannot be printed

    let pair = (1, true);
    println!("pair is {:?}", pair);

    println!("the reversed pair is {:?}", reverse(pair));

    // To create one element tuples, the comma is required to tell them apart
    // from a literal surrounded by parentheses
    println!("one element tuple: {:?}", (5u32,));
    println!("just an integer: {:?}", (5u32));

    //tuples can be destructured to create bindings
    let tuple = (1, "hello", 4.5, true);

    let (a, b, c, d) = tuple;
    println!("{:?}, {:?}, {:?}, {:?}", a, b, c, d);

    let matrix = Matrix(1.1, 1.2, 2.1, 2.2);
    println!("{:?}", matrix);

}

let xs: [i32; 5] = [1, 2, 3, 4, 5];

    // All elements can be initialized to the same value
let ys: [i32; 500] = [0; 500];
```



Slices are similar to arrays, but their length is not known at compile time. Instead, a slice is a two-word object, **the first word is a pointer to the data, and the second word is the length of the slice.**





































