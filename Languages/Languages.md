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

#### Bitwise Operators

* `&` - logical **AND**, returns true (1) if both bits are 1.
  * (0011 & 0101) = 0001
* `|` - logical **OR**, returns true (1) if either bit is 1.
  * (0011 | 0101) = 0111
* `^` - logical **XOR**, returns true (1) if the bits are different.
  * (0011 ^ 0101) = 0110
* `~` - logical **NOT**, flips the bits of one number.
  * ~(0011) = 1100
* `>>` - right shift, shifts bits to the right based on second argument. This is equivalent to dividing by 2.
Bits shifted outside of range are discarded.
  * (1100 >> 1) = 0110
* `<<` - left shift, shifts bits to the left based on second argument. This is equivalent to multiplying by 2.
Bits shifted outside of range are discarded.
  * (0011 << 2) = 1100

> Note: The shift bitwise operators `<<` and `>>` should **not** be used for
negative numbers.

## Variables

Variables can use either statically typed, or dynamically typed.
Behaviors between types can be strongly typed or weakly typed.

### Statically Typed

Static typing is where value types are checked in compile time. The data type of a
value **is** specified on declaration.

```c
int num = 5;
string name = "Jerry";
```

### Dynamically Typed

Dynamic typing is where values types are checked in run time. The data type of a
value **isn't** specified on declaration.

```py
num = 5 # int
name = "Jerry" # string
```

### Strongly Typed

Strongly typed languages enforce that only same types can operate with eachother.

```c
string num1 = "1";
int num2 = 2;
printf(num1 + num2); // Error: mismatched types
```

### Weakly Typed

Weakly typed languages allow for different types to operate with eachother.

```js
let num1 = 2;
let num2 = "1";

console.log(num1 + num2); // 21
```

## Conditionals
## Collections

## Loops

### While Loop

Code within a while loop keeps executing until the condition is false.

Syntax:

```c
while(condition) {
    // code
}
```

### Do While Loop

Code in a do while guarantees at lease one execution before checking the condition.

Syntax:

```c
do {
    // code
} while(condition);
```

### For Loop

For loops are useful when the number of desired iterations is known, or going
through iterables.

Syntax:

```c
for(initialization; condition; modification) {
    // code
}
```

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

## Testing

Two common types of testing are:

1. Unit Tests - a way of testing small pieces of code in isolation.
1. Integration Tests - a way of testing across multiple complex systems.

Unit Tests typically follow the 3 step process:

1. Arrange - setup the test
1. Act - run code being tested
1. Assert - assert that the results meet expectations
