# Brainfuck

Brainfuck is a simple to use language with only 8 commands.

## Basics

* \+ - increases value under the pointer
* \- - decreases the value under the pointer
* \> - increases the pointer
* \< - decreases the pointer
* [ - starts a loop, code is repeated as long as the current pointer value is not 0.
* ] - ends a loop
* . - outputs ASCII code under the pointer
* , - reads char and stores ASCII under the pointer

An easy way to visualize how Brainfuck works is to think of it as an array of cells with the
pointer starting at cell 0.

[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
 ^ 

After running this code:

```
+++
>++
>++++
```

The array looks like this:

[ 3 ] [ 2 ] [ 4 ] [ ] [ ] [ ] [ ] [ ]
              ^


## Variables

## Conditionals

## Collections

## Loops

Brainfuck loops use the current value the pointer is pointing at as the counter.
The loop terminates once the counter is 0.

Brainfuck loop to generate a value of 50:

```
+++++ # cell-0 = 5 

[
> +++++ +++++ # cell-1 += 10
< - # cell-0--
]
```


## I/O

## Functions

## Exceptions

## Classes & Objects

## Language Specifics

## Libraries & Frameworks