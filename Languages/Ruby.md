# Ruby

## Basics

* Everything in Ruby is an object

Comments:

```rb
# Single line comment

=begin
    Multiline comment
=end
```

## Variables

* Normal variables start with an underscore or lowercase letter
* Constant variables start with an uppercase letter
* You can change a constant's value, however an error will be thrown

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

Conditional operators: `== != < > <= >= <=> && || ! and or not`

> Note: <=> does a compareTo type of comparison: -1 if the first argument is less, 0
if equal, 1 if the second argument is greater.

Unless:

```rb
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
    next unless (y % 2 == 0)
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
    puts "#{num}"
end

# Range for loop.
(1..5).each do |i|
    puts "#{i}"
end
```

## I/O

Standard input/output

```rb
print "Hello world!"

print "Enter your name":
name = gets.to_s

puts "This print will have a new line"
```

## Functions

Syntax:

```rb
def add_nums(num1, num2)
    # code
```

## Classes

## Language Specifics

## Libraries & Frameworks