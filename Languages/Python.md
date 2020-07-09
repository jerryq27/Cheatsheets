# Python

Python is a interpreted, high level, general-purpose, easy to use programming language developed by Guido van Rossum.

TODO:
* [Modules/Packages](#Modules%20&%20Packages)

## Table of Contents

1. [Basics](#Basics)
    1. [Keywords](#Keywords)
    1. [Operators](#Operators)
1. [Variables](#Variables)
    1. [Strings](#Strings)
    1. [Numbers](#Numbers)
1. [Conditionals](#Conditionals)
1. [Collections](#Collections)
    1. [Lists](#Lists)
    1. [Tuples](#Tuples)
    1. [Dictionaries](#Dictionaries)
    1. [Sets](#Sets)
    1. [Generators](#Generators)
    1. [Map, Filter, Reduce & Zip](#Map,%20Filter,%20Reduce%20&%20Zip)
        1. [Map](#Map)
        1. [Filter](#Filter)
        1. [Reduce](#Reduce)
        1. [Zip](#Zip) 
1. [Loops](#Loops)
1. [I/O](#I/O)
    1. [Standard Input & Output](#Standard%20Input%20&%20Output)
    1. [String Formatting](#String%20Formatting)
    1. [File Input & Output](#File%20Input%20&%20Output)
1. [Functions](#Functions)
    1. [Type Hinting](#Type%20Hinting)
    1. [Nested Functions](#Nested%20Functions)
    1. [*args & **kwargs](#*args%20&%20**kwargs)
    1. [Anonymous Functions](#Anonymous%20Functions)
1. [Exceptions](#Exceptions)
1. [Classes & Objects](#Classes%20&%20Objects)
    1. [Inheritance](#Inheritance)
    1. [Modules & Packages](#Modules%20&%20Packages)
        1. [import](#import)
1. [Language Specifics](#Language%20Specifics)
    1. [Underscores](#Underscores)
    1. [Special Operators](#Special%20Operators)
    1. [Code Introspection](#Code%20Introspection)
    1. [Slicing](#Slicing)
    1. [List Comprehension](#List%20Comprehension)
1. [Libraries & Frameworks](#Libraries%20&%20Frameworks)

## Basics

* Python uses spaces/tabs for code blocks
* Newlines are allowed between pairs: `()[]{}''' ''' """ """` or with `\`
* Semicolons are optional
* Scripts use the `#!/usr/bin/env python` header to set the interpreter

* There's no main method, although this boilerplate is used to make sure some code runs first:

```python
if __name__ == '__main__':
    # Code
```

### Keywords
[`and`]()
[`as`]()
[`assert`]()
[`break`]()
[`class`]()
[`continue`]()
[`def`]()
[`del`]()
[`except`]()
[`finally`]()
[`for/while`]()
[`from`]()
[`global`]()
[`if/elif/else`]()
[`import`]()
[`in`]()
[`is`]()
[`lambda`]()
[`None`]()
[`nonlocal`]()
[`not`]()
[`or`]()
[`pass`]()
[`raise`]()
[`return`]()
[`True/False`]()
[`try`]()
[`with`]()
[`yield`]()

### Operators

Basic arithmetic operators: `+ - * / %`

Bitwise operators:

* `&` - AND
* `|` - OR
* `^` - XOR
* `~` - NOT
* `<<` - Left shift
* `>>` - Right shift

[Special Operators](#Special%20Operators)

## Variables

Variables are loosely typed (no need to include a data type)
`some_var = 12`

Using the `type()` function returns a variable's data type.

### Strings

* Strings can be defined with both single and double quotes
* Multiline strings are defined inside of triple quotes.

```python
first_string = "Hello world!"
second_string = 'Hello world!'

first_long_string = """
    Long string
"""
second_long_string = '''
    Long String
'''
```

There are other types of string literals:

* fstrings `f''` - used to allow string interpolation
* rstrings `r''` - used to make raw strings for regular expressions
* ustring `u''` - Unicode string, Python3 strings are u strings by default

### Numbers

The following numeric literals are supported:

* `0b` - used for binary
* `0x` - used for hexadecimal
* `0o` - used for octal
* `e` - used for exponential notation
* `j` - ???

Numeric literals can also use `_` for readability.

```python
print(f'''
    binary={0b10011010}
    hex={0xCAFEBABE}
    octal={0o310}
    exponential={1.5e2}
    underscores={1_000_000}
''')
```

## Conditionals

Syntax: 

```python
if condition:
    # code
elif condition:
    # code
else:
    # code
```

Conditional operators: `== != < > <= >= and or is not`

* Use of these operators is similar to most languages.
* Having `not` before a boolean expression inverts it.
* The difference between `==` and `is` is that `==` compares the value and `is` compares the instance.

## Collections

Python has 5 commonly used collection types

* [Lists](#Lists) - list of values
* [Tuples](#Tuples) - data values that should be grouped together
* [Dictionaries](#Dictionaries) - key-value pairs
* [Sets](#Sets) - list of unique values
* [Generators](#Generators) - lists created on the fly

Membership operators: `in not`

### Lists

Lists are ordered and changeable.
Lists are defined using `[]` or `list()` and can contain values of different types.
Using `[]` allows for multiple values to be defined, while `list()` only takes one argument, an iterable data type.

```python
# List
list1 = [1, '2', 3.14, True]
list2 = list('Hello')  # ['H', 'e', 'l', 'l', 'o']
```

Basic operations

```python
anime = ['Hunter X Hunter', 'Demon Slayer', 'My Hero Academia']

# Accessing values
first_anime = anime[0]

# Changing values
anime[0] = 'Death Note'

# Appending values
anime.append('One Piece')

# Adding values at specified index (index, value)
anime.insert(0, 'Demon Slayer')

# Remove first instance of a value
anime.remove('Demon Slayer')

# Remove at specified index or last item
anime.pop()
anime.pop(0)

# Delete at specified index or list itself
del anime[0]
del anime

# Empty list without deleting the reference
anime.clear()

# Hard copy a list
anime2 = anime.copy()
anime3 = list(anime)

# Joining lists
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

nums = nums1 + nums2
nums = nums1.extend(nums2)

# Checking for value's existence
if 'My Hero Academia' in anime:
    print('My Hero Academia is in the list.')

# Loop through a list
for show in anime:
    print(show)
```

### Tuples

Tuples are ordered and unchangeable.
Tuples are defined using `()` or `tuple()` and can contain values of different types.
Using `()` and `tuple()` are similar, but `tuple()` requires the values passed in to be surrounded by `()` as well `tuple((1,2))`.

```python
# Tuple
tuple1 = ('blue', 'green', 'purple')
tuple2 = tuple(('blue', 'green', 'purple'))
```

Basic operations

```python
classes = ('Intro to CS', 'Data Structures', 'Operating Systems')

# Accessing values
freshmen_class = classes[0]

# Once a tuple is created, values, cannot be changed, added, or deleted without changing to a list first.

# Changing value example
mutable_classes = list(classes)
mutable_classes[0] = 'CS 101'
classes = tuple(mutable_classes)

# Delete the tuple itself
del classes

# Checking for value's existence
if 'Data Structures' in classes:
    print('Data Structures is in the tuple.')

# Looping through a tuple
for c in classes:
    print(c)
```

Tuples have a concept known as packing and unpacking.

```python
```

### Dictionaries

Dictionaries are unordered, changeable, and indexed.
Dictionaries are defined using `{}` or `dict()` and can contain key-value pairs of different types.
Both `{}` and `dict()` can be used to define multiple key-value pairs.

```python
# Dictionary
dict1 = {
    'name': 'Jerry',
    'birth_date': 1993,
    'male': True
}
# Parameter names are converted to string keys.
dict2 = dict(name='Jerry', birth_date=1993, male=True)
```

Basic operations

```python
hero = {
    'name': 'Luffy',
    'role': 'Captain',
    'members': 8,
    'pirate': True,
}

# Accessing values
name = hero['name']
name = hero.get('name')

# Changing values
hero['members'] = '8'

# Adding new key-value pairs
hero['treasure'] = 'Straw Hat'

# Remove value by key
hero.pop('members')

# Remove the last inserted item (< 3.7 removes random item)
hero.popitem()

# Delete at specified key or the dictionary itself
del hero['role']
del hero

# Empty dictionary without deleting the reference
hero.clear()

# Hard copy a dictionary
hero2 = hero.copy()
hero3 = dict(hero)

# Checking for key's existence
if 'role' in hero:
    print('The hero has a role.')

# Looping through a dictionary

# Keys
for k in hero:
    print(k)

for k in hero.keys():
    print(k)

# Values
for v in hero.values()
    print(v)

# Keys and Values
for k in hero:
    print('key={} value={}'.format(k, hero[k]))

for k, v in hero.items():
    print('key={} value={}'.format(k, v))

```

### Sets

Sets are unordered, changeable, and unindexed. Set values are also unique (no duplicates).
Sets are defined using `{}` or `set()` and can contain values of different types.
Using `{}` and `set()` are similar, but `set()` requires the values passed in to be surrounded by `()` as well `tuple((1,2))`.

```python
set1 = {'apple', 'banana', 'orange'}
set2 = set(('apple', 'banana', 'orange'))
```

Basic operations

```python
movies = {'Tarzan', 'Aladdin', 'Lion King'}

# Since sets are unordered and unindexed, values cannot be accessed by a specified index.

# Values in set cannot be changed, but values can be added and deleted

# Adding one value
movies.add('Treasure Planet')

# Adding multiple values
movies.update(['Mulan', 'Tangled', 'A Goofy Movie'])

# Removing a value, error thrown if value doesn't exist
movies.remove('Tarzan')

# Removing a value, error not thrown if value doesn't exist
movies.discard('Tarzan')

# Removing the last value (Since sets are unordered, we don't know the value that will be removed)
removed_movie = movies.pop()
print(removed_movie)

# Delete the set itself
del movies

# Empty set without deleting the reference
movies.clear()

# Hard copy a set
movies2 = movies.copy()
movies3 = set(movies)

# Joining sets
nums = {1, 2, 3}
lets = {'a', 'b', 'c'}

data = nums.union(lets)  # New set
nums.update(lets)  # Add values from one set to another

# Checking for value's existence
if 'Lion King' in movies:
    print('Lion King is in the set.')

# Looping through a set
for m in movies:
    print(m)
```

### Generators

Generators are an iterable, but while most iterables can be looped 
through multiple times, generators can only be looped through once. 
The values in most iterables are stored in memory which can cause issues 
in large data sets. Generators help with that problem, since values are 
_generated_ on the fly. 

Using [list comprehension](#List%20Comprehension), lists are created
with `[]` and generators use `()`.

```python
lst = [x * x for x in range(1, 11)]  # List

gnr = (x * x for x in range(1, 11))  # Generator
```

The keyword `yield` is used in a function. It acts like `return`, but 
unlike `return` where code runs until it hits a `return`/end, code with
`yield` will not run until a value needs to be accessed. At that point 
the next value is _generated_. 

```python
# Returns a generator with the 1-10 squared values
def create_generator():
    for i in range(1, 11):
        yield i**2
```

### Map, Filter, Reduce & Zip

These methods allow you to apply functions to iterables without the need
for loops and conditionals. [Lambdas](#Anonymous%20Functions) are useful
to use for the function argument. These methods rerturn `map`, `filter`,
and `zip` objects which are basically generators and can be casted into a
list. `reduce`, however, returns an `int`.

#### Map

Map just passes each element in an iterable to a function and returns the
result of for each element. The number of `iters` must match the number
of arguments the function needs. If the iterables for multiple arguments
don't match, map keeps going until it can't find enough arguments for the
function and returns without raising an exception.

`map(function, *iters)`

Simple example using `round(number, number of places)`

```python
floats = [2.134567, 3.1453678, 7.2317943, 5.1423613]

rounded = map(round, floats, range(1, 5))
print(list(rounded))  # output: [2.1, 3.15, 7.232, 5.1424]

rounded = map(round, floats, range(1, 5_000_000))
print(list(rounded))  # output: [2.1, 3.15, 7.232, 5.1424]

rounded = map(round, floats, range(1, 3))
print(list(rounded))  # output: [2.1, 3.15]
```

#### Filter

Filter tries to filter out values in an iterable based on a conditional.
With filter you can only pass in one iterable to a function which
requires a boolean return. It passes each element to that function and
filters out the values that return `False`. If the function doesn't 
return a boolean, then just the iterable will be returned.

`filter(function, iter)`

```python
words = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

is_palindrome = lambda word: word == word[::-1]

print(list(filter(is_palindrome, words)))
```

#### Reduce

Reduce aims to reduce an iterable into a single value. The function used
is required to have two parameters, the first element of the iterable,
and the second element of the iterable. If the `opt_initial_val` value is
specified, it will be used as the first argument, and the first element
of the iterable will be the second argument.

> Must be imported from `functools`

`reduce(function, iterable, opt_initial_val)`

```python
from functools import reduce

_sum = lambda x, y: x + y
numbers = [13, 17, 22, 5, 11, 2, 1, 4]

print(reduce(_sum, numbers))
print(reduce(_sum, numbers, 25))
```

#### Zip

Zip combines iterables into tuples. If the number of iterables don't
match, it will pair the values until it can't find enough arguments for
the tuple then returns without raising an exception.

`zip(*args)`

```python
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
l3 = ['+', '-', '*', '/', '%']

print(list(zip(l1, l2)))  # output: [(1, 'a'), (2, 'b'), (3, 'c')]
print(list(zip(l1, l2, l3)))  # output: [(1, 'a', '+'), (2, 'b', '-'), (3, 'c', '*')]
```

## Loops

Python uses two types of loops:

* `while` loops - loop based on codition
* `for` loops - controlled loop over a sequence

Syntax:

```python
while condition:
    # code

for i in sequence:
    # code
```

Python allows the use of `else` clauses with loops. These clauses trigger if no `break` is 
encountered. The `continue` keyword has no effect on whether or not the clause triggers.

```python
for v in values:
    if v == search_val:
        print('Found it!')
        break
else:
    raise Error('Value not found.')
```

## I/O

### Standard Input & Output

```python
name = input('What is your name: ')
print('Your name is ' + name)
```

### String Formatting

There are a few ways to format a print statement

1. Using the `%` operator:

```python
num = 2
flt = 3.14
name = 'Jerry'
colors = ['blue', 'green', 'cyan']

# If it's more than one value, a tuple needs to be used.
# Objects can use the %s placeholder, it will use the __repr__ method.
print('num=%d flt=%f name=%s colors=%s' % (num, flt, name, colors))
```

2. Using the `.format()` function:

```python
num = 2
flt = 3.14
name = "Jerry"

print('num={} flt={} name={}'.format(num, flt, name))
print('num={2} flt={1} name={0}'.format(name, flt, num))
print('num={a} flt={b} name={c}'.format(a=num, b=flt, c=name))
```

3. Using string interpolation with f strings:

```python
num = 2
flt = 3.14
name = "Jerry"

# Using string interpolation, code can be specified within the {}
print(f'num={num} flt={flt} name={name}')
print(F'num={num} flt={flt} name={name}')
print(f'expression={num * flt}')
```

### File Input & Output

Python uses the built in `open()` function to work with files. This
function takes in the path to the file, and the mode in which to open the
file.

* `r` - open file for reading, default
* `w` - opens file for writing, it's created if it doesn't exist, it will replace the file if it does
* `x` - exclusive creationqq of a file for writing, fails if the file already exists
* `a` - opens file to append to it, it is created if it doesn't exist
* `t` - opens file in text mode
* `b` - opens file in binary mode
* `+` - opens file for reading and writing

> Text mode is used when reading in strings, binary mode is used for 
non-text files such as images and executables.

Once opened, a file must be closed once operations on it have finished.
It is also recommended to specify the encoding when opening files in text
mode for consistent behavior across systems.

```python
# Potentialy unsafe, if an exception occurs before the close statement
# The program ends without closing the file.
_file = open('example.txt', mode='r', encoding='utf8')
_file.close()

# Safe alternative
try:
    _file = open('example.txt', mode='r', encoding='utf8')
finally:
    _file.close()

# Recommended alternative
with open('example.txt', mode='r', encoding='utf8') as _file:
    # code
# File is closed internally when leaving the 'with' block
```

Common file operations:

1. `read()` - read the whole file or n bytes
1. `readline()` - read until a newline is encountered
1. `readlines()` - read the file into a list based on newlines
1. `tell()` - gets the current position of the cursor in the file
1. `seek()` - moves the position of the cursor in the file
1. `write()` - writes a string to the file
1. `writelines()` - writes a list of strings into a file by newlines

## Functions

Syntax:

```python
def function_name(param1, param2):
    # code
    return 1

val = function_name(arg1, arg2)  # Function call
```

Python also supports default parameter values for functions:

```python
def add(x=1, y=2):
    return "{} + {} = {}".format(x, y, x + y)

print(add())
print(add(5))
print(add(5, 5))
print(add(y=5))
```

Seeing a `*` in a function's parameter listing indicates  the end of
positional arguments. All arguments passed in after the `*` requires
the parameter's name to be explicitly specified.

```python
def star_params(a, b, *, c):
    print(f'{a} {b} {c}')
    
star_params(1, 2, c=3)  # No errors
star_params(1, 2, 3)  # Raises a TypeError
```

### Type Hinting

You can use type hints to specify what the type of the parameters and the 
return type of the function is:

```python
def get_string(name: str='Jerry', age: int) -> str:
    # Optionally you can specify types with a type comment:
    # type: (str, int) -> str
    return 'Hello, World!'
```

Interpretation-wise, type hints have no effect whatsoever. They are used
to help the programmer document their code. This also helps improve IDEs
and linters to give suggestions when they know specified types functions
are asking for.

### Nested Functions

With nested functions, the inner function has read only access to
variables within the scope of the outer function.

```python
def outer_function(message):
    def inner_function():
        print(message)
    inner_function()
    print(message)

outer_function('Hello, World!')
```

To modify outer function variables within the inner function, you must use
the `nonlocal` keyword. Without it, a new variable will be created instead
of modifying the existing one.

```python
def outer_function(message):
    def inner_function():
        nonlocal message
        message = 'Goodbye, World!'
        print(message)
    inner_function()
    print(message)

outer_function('Hello, World!')
```

### *args & **kwargs

Python functions support parameters that allow for any number of arguments to be passed in by 
prepending the parameter with `*`.

```python
def additional_args(arg1, arg1, *args):
    print(f'first arg: {arg1}\nsecond arg: {arg2}\nthe rest{list(args)}')

additional_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
```

or any number of keyword args with `**`.

```python
def additional_kwargs(arg1, arg2, **kwargs):
    print(f'first arg: {arg1}\nsecond arg: {arg2}\nkey word args{dict(kwargs)}')

additional_kwargs(1, 2, name='Jerry', color='blue', languages='English|Spanish|Japanese|Korean')

```

### Anonymous Functions

Anonymous functions (or lambda functions) are used for simple functions
that don't need reusabiliy like defined functions. These functions are
created using the `lambda` keyword.

`lambda <bound_var>: <body>`

Example:

```python
# Unnamed lambda
(lambda x: x ** 2)(5)  # 25

# Named lambda
sqr = lambda x: x ** 2
sqr(5)  # 25

# Multiple lines
odd_or_even = (lambda x:
(x % 2 and 'odd' or 'even'))
odd_or_even(3)
```

Lambdas can also use named arguments, `*args`, and `**kwargs`.

```py
named_args = lambda x, y, z=3: x + y + z
named_args(1, 2)

var_args = lambda *args: sum(args)
var_args(10, 20, 30, 40, 50)

_kwargs = lambda **kwargs: sum(kwargs.values())
_kwargs(one=1, two=2, three=3)
```

Lambdas are commonly used with higher order functions (take functions as
arguments to produce another function, in this case, the lambda)

```python
hof = lambda x, function: x + function(x)
hof(2, lambda x: x * x)
```

Anonymouse functions cannot contain any statements involving `return`
`pass`, `assert` or `raise`, otherwise a `SyntaxError` will be raised.

## Exceptions

Exceptions in Python are handled using the `try/except` block.

Syntax:

```python
try:
    # code
except Exception:
    # exception occured code
else:
    # no exception occured code
finally:
    # always run code
```

## Classes & Objects

Syntax:

```python
class ClassName:

    field1 = 'field' # public field

    def __init__(self):
        # These (except private) don't affect access
        # Just a convention to note their uses
        # It is up to the programmer to recognize these conventions.
        self.pub_field = 1  # public field
        self._pro_field = 2  # protected field
        self.__priv_field = 3  # private field

    def class_function(self):
        print('Class function call.')

obj = ClassName()
print(obj.field1)
obj.class_function()
```

Python classes have default magic/dunder (double underscore) functions
that can be overridden.

* `__init__` - class constructor.
* `__str__` - (pretty) string representation of an object for users.
* `__repr__` - (useful) string representation of an object for developers. 
* `__call__` - make object callable.

### Inheritance

Syntax:

```python
 class Child(Parent):

    def __init__(self, name):
        # Both acheive the same thing.
        Parent.__init__(self, name)
        super().__init__(name)

    # Class body

```

### Modules & Packages

Python **modules** are files with the `.py` extension that contain
variables, functions, and class definitions. The module name is the name
of the file itself. **Packages** are directories that include an
`__init__.py` file. Packages can contain many modules, and the package
name is the name of the directory itself.

#### import

Python uses the `import` keyword to import modules and packages. The
`import` keyword goes through a series of steps to import:

1. Searches for a built-in modules from the Python Standard Library
1. If not found, it searches for the specified file in one of the directories specified by `sys.path`. `sys.path` is initialized using:
    1. The current directory
    1. The `PYTHONPATH` environment variable
    1. The installation-dependent default

```python
# log.py
def info(message):
    print(f'info: {message}')

def warn(message):
    print(f'warn: {message}')

def error(message)
    print(f'error: {message}')

# -----------------
# main.py
import log

if __name__ == '__main__':\
    log.info('Starting program.')
    log.warn('Warn message')
    log.error('Program ending.')

#------------------
# main2.py
from log import info

if __name__ == '__main__':\
    info('Starting program.')
    info('Doing Python things.')
    info('Ending program.')
```

You can also alias the name the imported definition with the `as`
keyword:

```python
import log as l

l.info(...)
l.warn(...)
l.error(...)
```

> When the interpreter encounters an `import` statement with modules, it
runs all the code specified. however, with packages, it runs all the code
in the package's `__init__.py` file.

## Language Specifics

### Underscores

Underscores have various meanings and uses in Python:

* `_private` - private member, meant for internal use
    * Nothing prevents programmers from accessing private members
    * However, private members are ignored by Python with `from example import *`
* `class_` - used to avoid naming conflicts with Python keywords
* `__example` - used to protect variables from being overridden in subclasses
    * Using this triggers _name mangling_ with the Python interpreter
    * `dir()` will show how the variable gets altered: (`_SubClass__member`)
    * You will need to specify the altered name to access the correct value
    * Within the class however, you can specify the member with `self.__member`
* `__example__` - functions reserved for special use in Python.
    * These dunder functions are a convention used by the core Python team
    * Avoid this naming scheme in your code
* `_` - used to indicate a variable that is temporary, or insignificant.
    * Has no special meaning, just a convention
    * Interpreter session uses `_` to store the result of a previous calculation
    * Also useful for unpacking tuples

```python
# Loop
for _ in range(101):
    print('Hello, World!')

# Tuple return
def just_food():
    return ('water', 'chicken')

_, food = just_food()
print(food)

# Unpacking tuple:
info = ('water', 'chicken', 'cake', 'bread')
_, food, dessert, _ = info 
```


### Special Operators

The `*` operator can be used with strings

```python
month = 'M' * 2
day = 'D' * 2
year = 'Y' * 4

date_format = '{}/{}/{}'.format(month, day, year)
```

and can be used with lists as well

```python
print([1, 2, 3] * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3] 
```

You can use `**` operator for a power relationship:

```python
    squared = 5 ** 2  # 5^2
    cubed = 5 ** 3  # 5^3
```

The `//` operator is used for floor division:

```python
print(6 / 3.14)  # 1.910828025477707
print(6 // 3.14)  # 1.0
```

### Code Introspection

Python has some built in utilities to examine classes, functions and 
keywords.

* `help(function)` - used to find out what other functions do
* `dir(class/obj)` - returns a list of attributesa and functions in a 
class/object
* `hasattr(obj, attr)` - returns whether the object has the given 
attribute
* `id(obj)` - returns the unique id of the object (cpython uses the 
memory address)
* `type(arg)` - returns the type of the argument
* `repr(obj)` - returns the string represention of the object (default 
contains the memory address in hex == decimal from `id()`) 
* `callable(arg)` - returns whether the argument is callable
* `issubclass(subclass, superclass)` - returns whether a is subclass of b 
* `isinstance(obj, class)` - returns whether the object is an instance of 
the class
* `__doc__` -
* `__name__` -

### Slicing

Slicing can be used with iterables such as collections and strings, 
and provides alternative ways of accessing values.
The format is usually `[start(inclusive):stop(exclusive):step(every n value from start to stop)]`

* If start isn't specified, the first index is used
* if stop isn't specified, the last index is used

```python
str1 = 'Python'
print(str1[2:5])  # tho 
print(str1[:5])  # Pytho
print(str1[::2])  # Pto

list1 = [1, 2, 3, 4, 5]
print(list1[0:3])  # [1, 2, 3]
```

Using negative numbers counts from the end of the iterable.
```python
str1 = 'Python.md'
print(str1[:-3])  # Python
```

### List Comprehension

Creating lists in a single, readable line.

Syntax: `[<var> for <var> in <iterable> if <condition>]`

Simple example:

```python
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

postive_numbers = [x for x in numbers if x > 0]
print(positive_numbers)
```

## Libraries & Frameworks

[Django] - a high level web framework
[Numpy] - library for easier calculations with arrays
[Pandas] - built using numpy, for tabular data

[Django]: ../WebDevelopment/Django.md