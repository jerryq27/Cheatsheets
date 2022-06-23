# Rust

Rust is a programming language developed by . It aims to produce fast and efficient code
with a compiler that encourages certain programming patterns that are different from other
languages.

## Basics

Variables in Rust are [dynamically typed](../Languages/Languages.md#dynamically-typed) (though, a type can be specified)
and [immutable](../Languages/Languages.md#basics) by default.
They are created using the `let` keyword:

```rs
let x = 5;
x = 1; // Compiler error.

let y: u32 = 10; // Specified type.
```

The reason for this behavior is that Rust tries to prevent situations that can lead to bugs. Some piece code
can operate on the assumption that certain values won't change. If other pieces of code end up changing some
of those values, than the first piece can stop behaving in the way it was supposed to. This kind of issue can
be difficult to debug, especially if those values only get altered by other pieces of code _sometimes_.

The Rust compiler makes sure that when values are stated as immutable, they won't change, and this relieves
the programmer from having to keep track of immutable values.

To make a variable mutable, the `mut` keyword is used:

```rs
let mut x = 5;
x = 1; // Ok
```

Variables can also be changed through a process known as [shadowing](../Languages/Languages.md#variables).
To shadow a variable, the keyword `let` **must** be used with the same variable name. The new variable
that shadowed the first is what the program sees when it's used. Shadowing ends along with it's scope.

```rs
fn main() {
    let x = 5;
    
    let x = x + 2; // X has been shadowed.
    
    {
        let x = x * 2; // X has been shadowed again.
        println!("Value at the inner scope is: {}", x); // 14
        // Inner shadowing has ended in this scope.
    }
    
    println!("Value of x at the outer scope is: {}", x); // 7
}
```

There are key advantages to using shadowing over mutable variables:

* Shadowing allows for the modification of an immutable variable, while making it immutable after the modification.
* Since shadowing effectively creates a new variable using `let`, the value's type can be changed while using the same name.
  * This technique helps avoid scenarios where multiple variables holding the same data with different types: `id` and `id_str`.

```rs
let total_letters = "aaaaaa";
let total_letters = total_letters.len();
```

### Constants

Constants, like Rust variables, are values bound to a name that cannot be changed. There are a few
differences between constants and varibales:

* Constants are declared using the `const` keyword instead of `let`.
* The `mut` keyword cannot be used with constants.
* The type of the constant value **must** be specified.
* Constants can be declared in any scope, including the global scope.
* Constants can only be set to a constant expression, _not_ a value to be determined on runtime.

```rs
const HOURS_IN_A_WEEK: u32 = 24 * 7;
```

### Operators

Rust uses the [basic arithmetic operators](../Languages/Languages.md#arithmetic).

## Command Line

[Rust Installation](https://doc.rust-lang.org/book/ch01-01-installation.html)

Common commands:

* `rustc --version` shows the current version of Rust.
* `rustup update` updates Rust.
* `rustup self uninstall` uninstalls Rust.

The installation of Rust includes a local copy of the documentation. To see those docs, run:

 `rustup doc`

The Rust compiler is the `rustc` program. To compile a program, run:

`rustc example.rs`

This command will create an executable binary file.

Rust also includes a build system and package manager called _Cargo_. Cargo can also be used to
manage projects, build the code, download the dependencies, etc.

Creating a project with Cargo generates the following structure:

```txt
project/
    src/main.rs
    Cargo.toml
```

The _Cargo.toml_ file is the configuration for a Cargo project.

```toml
[package]
name = "project_name"
version = "0.1.0"
edition = "2021"

[dependencies]
// Crates
```

The **\[package\]** section list statements for configuring a package, which Cargo needs to compile the program.
in this case it's:

* name - the name of the program
* version - the version of the program
* edition - the edition of Rust to use.

The **\[dependencies\]** list the dependenvies the program needs to fetch to compile. In Rust, these dependencies
are known as _crates_.

Common cargo commands:

* `cargo --version` shows the current version of cargo.
* `cargo new $PROJECT` creates a new Rust project.
  * `--vcs=git` creates a Git repository with the Rust project.
* `cargo build` - creates an executable in _target/debug/$EXECUTABLE_ and generates a _Cargo.lock_ file on the first run.
  * `--release` - creates and executable for release in _target/release/$EXECUTABLE_.
* `cargo run` - creates the executable and runs it.
* `cargo check` - checks if the code can compile without compiling an executable.

## Variables

Rust has two different data types, _scaler_ and _compount_ types.

Scaler type represents a single value, and there are four primary scaler types:

* integers
* floating points
* booleans
* characters

```rs
let num: u32 = 25;
let flt: f64 = 3.14;
let isBool: bool = true;
let letter: char = 'c';
```

Compound types group multiple values together into one type, and Rust has two primitive compound types:

* tuples
* arrays

See [collections](#collections).

### Numbers

Length|Signed|Unsigned
---|---|---
8-bit|`i8`|`u8`
16-bit|`i16`|`u16`
32-bit|`i32` (default)|`u32`
64-bit|`i64`|`u64`
128-bit|`i128`|`u128`
archeticture|`isize`|`usize`\

The _archeticture_ size means it depends on the computer's architecture.

> These values will experience [integer overflow](../Languages/Languages.md#integer-overflow) If 
a number is changed to value outside it's range.

The following number letters are also allowed by Rust:

Example|Value
---|---
`3_14`|Decimal
`0xff`|Hex
`0o77`|Octal
`0b1010`|Binary
`b'A'`|Byte (`u8` only)

Floating Points:

Length|Type
---|---
32-bit|`f32`
64-bit|`f64` (default)

> 64-bit floating points are the default due to their precision and little noticeable difference
in performance between `f32` and `f64` on modern CPUs.

## Conditionals

## Collections

Rust has two primitive collection types, tuples and arrays. In Rust these are known as _compound types_.

### Tuple

Rust tuples are a general way of grouping values of various types together into one compound type. Tuples
have a fixed size and cannot grow or shrink once declared.

```rs
let tup: (i32, f64, u8) = (500, 6.4, 1);

// Get values from tuple (destructuring).
let (a, b, c) = tup;

// Second way of accessing values.
println!(tup.0); // 500
println!(tup.1); // 6.4
println!(tup.2); // 1

// Special type of tuple known as a "unit type" which returns a "unit value"?
let unit_type = ();
```

### Arrays

Arrays are a collection of values with the same type, and uniquely to Rust, have a fixed size
once declared.

```rs
let arr = [1, 2, 3, 4, 5];

let size_declared_arr[i32; 3] = ['a', 'b', 'c'] // [type; size]

let values_declared_arr [10; 5]; // [value; size] [10, 10, 10, 10, 10]
```

> Arrays are stored in the [stack](../Languages/Languages.md#stack).

## Loops

## I/O

## Functions

Functions can be defined in any order, it doesn't matter to Rust. The program
will run in order of how the code appears in the main function. Function parameters
**must** declare a type.

Syntax:

```rs
fn main() {
    println!("Hello, world!");

    some_other_function();
}

fn some_other_function() {
    println!("From another function.");
}

fn function_with_param(x: i32, y: char) {
    println!("The parameter's value is {} and {}", x, y);
}
```

There is a distinction between _statements_ and _expressions_ in Rust.

* Statements - instructions that perform an action, but don't return a value.
* Expressions - instructions that evaluate into a resulting value.

```rs
// Statements
fn sample() {
    // Function definitions are statements.
}

let x = 5;


// Expressions
sample();
```

```rs
// Compiler error: (expected expression, found statement)
// let statements don't return values, so x can't bind to anything.
let x = (let y = 4);

// This is ok
let a = {
    let b = 10;
    10 + 1
};
```

Unlike languages like Ruby, assignments don't return values in Rust.

> Adding a **;** turns a expression into an statement.

Functions that return a value must declare the return type in the function signature:

```rs
// Valid functions, the 11 with no semicolon is an expression.
fn returnNum() -> i32 {
    11
}

let num = returnNum();
println!("num = {}", num); // 11

fn addOne(x: i32) -> i32 {
    x + 1 //; Would throw a compiler error if there was a semicolon here.
}
let x = addOne(20);
println!("x = {}", x); // 21
```

## Exceptions

## Classes & Objects

## Language Specifics

## Libraries & Frameworks
