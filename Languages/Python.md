# Python

Python is a interpreted, high level, general-purpose, easy to use programming language developed by Guido van Rossum.

## Basics

* Python uses spaces/tabs for code blocks
* Newlines are allowed between pairs: ()[]{}''' ''' """ """ or with `\`
* Semicolons are optional
* Scripts use the `#!/usr/bin/env python3` header to set the interpreter

* There's no main method, although this boilerplate is used to make sure some code runs first:

```python
if __name__ == '__main__':
    # Code
```

## Variables

Variables are loosely typed (no need to include a data type)
`some_var = 12`

Using the `type()` function returns a variable's data type.

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

Python has 4 commonly used collection types

* Lists - list of values
* Tupples - data values that should be grouped together
* Dictionaries - key-value pairs
* Sets - list of unique values

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

### Standard input and output

```python
name = input('What is your name: ')
print('Your name is ' + name)
```

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

### File input and output

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

## Exceptions

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
they can override.

* `__init__` - class constructor.
* `__repr__` - toString function. 

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


## Language Specifics

### Operators

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

### Generators and yield

Generators are an iterable, but while most iterables can be looped 
through multiple times, generators can only be looped through once. 
The values in most iterables are stored in memory which can cause issues 
in large data sets. Generators help with that problem, since values are 
_generated_ on the fly. 

Lists are created with `[]` and generators use `()`.

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

## Libraries & Frameworks

[Django] - a high level web framework
[Numpy] - library for easier calculations with arrays
[Pandas] - built using numpy, for tabular data

[Django]: ../WebDevelopment/Django.md