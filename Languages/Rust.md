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

## Conditionals

## Collections

## Loops

## I/O

## Functions

## Exceptions

## Classes & Objects

## Language Specifics

## Libraries & Frameworks
