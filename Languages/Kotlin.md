# Kotlin

Kotlin is a programming language developed by JetBrains and supported by Android.

## Basics

* Everything in Kotlin is an Object.
* Kotlin aims to be safe of NullPointerExceptions, by default variables can't be null.
* Semicolons are optional.
* Kotlin can easily be translated to Java.
* Kotlin can also use Java libraries
* String literals can be enclosed with `"Short String"` or `""" Long String """`
* String interpolation is supported with `"$var"` or `"${expression}"`
* `->` is used as a separator:
  * separates the parametes and body of a lambda expression

  ```kotlin
    val sum = { x: Int, y: Int -> x + y }
  ```

  * seprates the condition and body of a when expression branch

  ```kotlin
    (R, T) -> R
  ```

  * separates the paramters and return type declaration in a function type

  ```kotlin
    when (x) {
        0, 1 -> print("x == 0 or x == 1")
        else -> print("otherwise")
    }
  ```

## Variables

Variables are defined with the `val` or `var` keywords.

* `val` variables are immutable (final)
* `var` variables are mutable

```kotlin
var name = "String"
var name: String = "Jerry" // Type can also be specified.
```

## Conditionals

Kotlin supports the basic conditional operators: `> < >= <= == != && || !`

```kotlin
val age = 8

// Normal if/else
if(age < 5) {
    println("Go to preschool")
}
else if(age == 5) {
    println("Go to kindergarten")
}
else if((age > 5) && (age <= 17)) {
    val grade = age - 5
    println("Go to grade $grade")
}
else {
    println("Go to college")
}
```

However, the more Kotlin approach would be to use a `when` statement.

```kotlin
when(age) {
    0, 1, 2, 3, 4 -> println("Go to preschool")
    5 -> println("Go to kindergarten")
    in 6..17 -> {
        val grade = age - 5
        println("Go to grade $grade")
    }
    else -> println("Go to college")
}
```

## Collections

```kotlin
// Arrays can hold a list of various values
var arr = arrayOf(1, 1.23, "str")
// Unless the type is specified
var intArray: Array<Int> = arrayOf(1, 2, 3)
```

There are 3 common types of collections:

1. Lists
1. Sets
1. Maps

```kotlin
var list1: MutableList<Int> = mutableListOf(1, 2, 3, 4, 5)
val list2: List<Int> = listOf(1, 2, 3)
```

## Loops

## Functions

## Classes
