# Ruby

## Basics

* Everything in Ruby is an object

```rb
puts 1.class # Fixnum
puts 3.14.class # Float
puts "hello".class # String
```

Comments:

```rb
# Single line comment

=begin
    Multiline comment
=end
```

Including other Ruby files:

```rb
# file2.rb

puts "Hello"
```

```rb
load "file2.rb"
# Hello
```

### Operators

Basic arithmetic operators: `+ - * / %`

Other supported operators: `+= -= *= /= %=`

## Variables

* Normal variables start with an underscore or lowercase letter
* By convention Ruby uses snake casing
* Constant variables start with an uppercase letter
* You can change a constant's value, however a warning will be thrown

```rb
num_one = 1
PI = 3.14
```

## Conditionals

Syntax:

```rb
if(condition)
    # Code
elsif(condition) && (condition)
    # Code
else
    # Code
end
```

Conditional operators: `== != < > <= >= <=>`
Logical operators: `&& || ! and or not`

> Note: <=> does a compareTo type of comparison: -1 if the first argument is less, 0
if equal, 1 if the second argument is greater.

Unless:

```rb
# unless = if not
unless condition
    # Code
else
    # Code
end
    # Code
```

Switch syntax:

```rb
case value
    when "str1", "str2":
        puts "string"
        exit
    when 1,2,3:
        puts "number"
        exit
end
```

Inline conditions:

```rb
num = 4
puts "Even number" if num % 2 == 0
```

Ternary Operator:

```rb
puts (condidtion)? "true" : "false"
```

## Collections

## Loops

Loop:

```rb
x = 1
loop do
    x += 1
    # next is like continue
    next unless (x % 2) == 0
    puts x
    break if x >= 10
end
```

While loop:

```rb
y = 1

while y <= 10
    y += 1
    next unless (y % 2) == 0
    puts y
end
```

Until loop:

```rb
a = 1

until a >= 10
    a += 1
    next unless (a % 2 == 0)
    puts a
end
```

For loop:

```rb
numbers = [1, 2, 3, 4, 5]

for number in numbers
    puts "#{number}, "
end

# Other for loop
numbers.each do |num|
    puts num
end

# Range for loop.
(1..5).each do |i|
    puts i
end
```

## I/O

### Standard Input & Output

```rb
print "Hello world!"

print "Enter your name: "
name = gets.to_s.chomp # Chomp removes newline/trailing characters.
print "Enter a number: "
num = gets.to_i
print "Your name is " + name + " and the number you entered is " + num.to_s

puts "Puts will print with a new line"
```

### String Formatting

Using variables in strings:

```rb
name = "Jerry"
puts "Hello #{name}"
```

### File Input & Output

```rb
handler = File.new("example.txt", "w")
handler.puts("Some data.")
handler.close

file_data = File.read("example.txt")
puts "File data: " + file_data
```

## Functions

Syntax:

```rb
def example()
    # code
end
```

Example function with a return:

```rb
def add_nums(num1, num2)
    return num1 + num2

puts add_nums(1, 2) # 3
```

## Exceptions

Exceptions in Ruby are handled by the `begin/rescue` block:

```rb
print "Enter a number: "
num = gets.to_i

begin
    answer = 5/num
rescue
    puts "Illegal division."
    exit
end

puts "5/#{num} = #{answer}"
```

Throwing an exception with `raise`:

```rb
age = 10
def check_age(age)
    raise ArgumentError, "Enter positive number" unless age > 0
end

begin
    check_age(-1)
rescue ArgumentError
    puts "Invalid age"
end
```

## Classes

## Language Specifics

## Libraries & Frameworks
