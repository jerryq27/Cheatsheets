# Ruby

[Checkpoint](https://youtu.be/Dji9ALCgfpM?t=1780)

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

### Strings

String can be defined using both single and double quotes:

```rb
str1 = "String1"
str2 = 'String2'
```

String functions:

```rb
# Concatenation
first_name = "Luke"
last_name = "Skywalker"
full_name = first_name + " " + last_name
full_name = "#{first_name} #{last_name}"

# Comparing strings
puts "a == a? #{'a' == 'a'}"

# Comparing string objects
puts "'a' == 'a'? #{'a'.equal?('a')}" # false
puts full_name.equals?(full_name) # true

# String casting
1.to_s

# String length
puts full_name.size

# Check for substring
puts full_name.include?("Luke") # true
puts full_name.starts_with?("Skywalker") # false

# Index
puts full_name.index("Skywalker").to_s # 5

# Count occurences (Regex?)
puts "Vowels: #{full_name.count('aeiou').to_s}"
puts "Consonants: #{full_name.count('^aeiou').to_s}"

# Remove occurences
puts full_name.delete('e')

# Casing
puts full_name.upcase
puts full_name.downcase
puts full_name.swapcase

# Strip whitespace
puts full_name.lstrip
puts full_name.rstrip
puts full_name.strip

# Strip characters
full_name.chomp # trailing whitespace
full_name.chomp("er") # last two characters
full_name.chop # last character

# Padding strings?
puts full_name.rjust(20, '.')
puts full_name.ljust(20, '.')
puts full_name.center(20, '.')

# Split a string (Regex?)
name_array = full_name.split(//) # Split each character. 
name_array2 = full_name.split(/ /) # Split by space.
```

Multiline string:

```rb
# EOM can be anything, the symbol is used to determine the end of the string.
long_string = <<EOM
This is a long string
that allows the use of interpolation
2 + 2 = #{2 + 2}
EOM
x = 2
```

> Note: Special characters behave [differently](#String-Formatting) depending on the
quotes used.

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

String interpolation is only allowed within double quotes. Single quoted strings
are treated as raw strings:

```rb
name = "Jerry"
puts "Hello #{name}"

puts "2 + 2 = #{2 + 2}"
puts '2 + 2 = #{2 + 2}' # Raw string.
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
