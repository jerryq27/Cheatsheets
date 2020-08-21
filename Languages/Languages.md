# Languages

Programming languages share similar concepts when it comes to their design.

## Basics

Common terms:

* **DRY Code** - Don't repeat yourself


### Operators

#### Arithmetic

* `+` - add
* `-` - subtract
* `*` - multiply
* `/` - divide
* `%` - modulus (remainder of a division)

#### Increment & Decrement

* `++` - add 1
* `--` - subtract 1

#### Arithmetic Assignment

* `+=` - add and assign
* `-=` - subtract and assign
* `*=` - multiply and assign
* `/=` - divide and assign
* `%/` - modulo and assign

## Variables

Variables can use either static typing, or dynamic typing:

### Static Type

Static typing is where the data type of a value **is** specified on
declaration.

`int num = 5;`

### Dynamic Type

Dynamic typing is where the data type of a value **isn't** specified on
declaration, but determined by the value at run time.

`num = 5`

## Conditionals
## Collections
## Loops
## I/O
## Functions

### Parameters & Arguments

_Parameters_ are specified in the function definition, while _Arguments_
are specified in the function call:

```
// Parameters: arg1, arg2
function(arg1, arg2) {
    ...
}

// Arguments: 1, 2
function(1, 2);
```

### First Class Citizen

Functions can be assigned to a variable and treated as such.

```
add = function(a + b) {
    return a + b;
}

sum = add(5, 5);
```

### Lambdas

Lambdas (also known as anonymous functions) are simple functions that
don't require reusability like defined functions.

```
// Val is 25
val = (lambda arg: arg * arg)(5);
```

## Exceptions
## Classes & Objects
## Language Specifics
## Libraries & Frameworks