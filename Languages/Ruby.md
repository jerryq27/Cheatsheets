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

### Symbols

Symbols in Ruby are essentially strings that cannot be changed
Useful for hashes or strings that won't change or use string methods:

```rb
:example_symbol

puts :example_symbol # example_symbol
puts :example_symbol.to_s # example_symbol
puts :example_symbol.class # Symbol
puts :example_symbol.object_id # 833628
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

Array Syntax:

```rb
arr = Array.new # #mpty array
arr2 = Array.new(5) # Empty array with 5 spaces
arr3 = Array.new(5, "empty") # Array with 5 spaces with the default value of "empty"
arr4 = [1, "two", 3.14] # Array pre-defined with multiple data types
```

Array methods:

```rb
arr = ["Naruto", "Sasuke", "Sakura", "Kakashi"]

# Getting values from an array.
puts arr[2] # Sakura
puts arr[2, 2].join(", ") # Sakura, Kakashi
puts arr.values_at(0, 1, 3).join(", ") # Naruto, Sasuke, Kakashi

# Add value to beginning of the array
arr.unshift("Jaraiya")
# Removes the first item of the array
arr.shift()
# Adds values to the end of the array
arr.push("Sai", "Yamamoto")
# Removes one item at the end of the array
arr.pop()
# Adds these values to the end of the array.
arr.concat(["Hinata", "Kiba", "Shino"])

# Array length
puts arr.size().to_s

# Search array
puts arr.include?("Sai").to_s # true

# Occurences
puts arr.count("Shino") # 1

# Check if empty
puts arr.empty?.to_s

# Join to a string.
puts arr.join(", ")

# Print array
p arr
puts arr

# Loop through array
arr.each do |ninja|
    puts ninja
end
```

### Hashes

Hashes in Ruby are a key-value pair type of collection:

```rb
hash1 = {
    "PI" => 3.14,
    "Golden" => 1.618,
    "e" => 2.718
}
hash2 = Hash["Dog", "Spot", "Cat", "Mr. Grumpypants"]

puts hash1["PI"] # 3.14
puts hash2["Cat"] # Mr. Grumpypants
```

Hash methods:

```rb
ranks = Hash["Kakashi", "Jonin", "Shikamaru", "Chunin"]

# Adding values to hashes
ranks["Sasuke"] = "Genin"

# Deleting values from hashes
ranks.delete("Kakashi")

# Hash with default keys
default_key_hash = Hash.new("No key")
puts default_key_hash("user") # No Key

# Combining hashes
hash1.update(hash2) # Destructive, will overwrite any values with the same key in hash1
hash1.merge(hash2) # Not destructive, keep all keys and values, even duplicates

# Hash length
puts ranks.size().to_s

# Search hash
puts ranks.has_key?("Sai").to_s # false
puts ranks.has_value("Chunin").to_s # true

# Check if empty
puts ranks.empty?.to_s

# Loop through hash
ranks.each do |key, value|
    puts key.to_s + ": " + value.to_s
end
```

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

# printf with placeholders.
printf "String: %s Integers: %d Floats: %.3f", "abd", 2, 1.234567890
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

Example:

```rb
=begin
w = write
a = append
=end

file = File.new("example.txt", "w")
file.puts("Some data.")
file.close

data = File.read("example.txt")
puts "File data: " + data

# Looping through file data
# Does it need two loops?
File.open("100-words.txt") do |line|
    line.each do |item|
        word, definition =  item.chomp.split("|")
        puts "#{word} means #{definition}"
    end
end
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

## Classes & Objects

Syntax:

```rb
class Person
    def initialize
        # Constructor
    end
end

person1 = Person.new
```

Getters and setters can be defined in multiple ways:

```rb
class Animal

    # Setter examples
    def set_name(name)
        @name = name
    end

    def name=(new_name)
        if new_name.is_a?(Numeric)
            puts "Name can't be a number"
        else
            @name = new_name
        end
    end

    # Getter examples
    def get_name
        @name
    end

    def name
        @name
    end

end

dog = Animal.new

# Using each setter
dog.set_name("Spot")
dog.name = "Spot"

# Using each getter
puts dog.get_name
puts dog.name
```

Shortcut to generating getters and setters:

```rb
class Person
    # Generates getters
    attr_reader :name, :age, :favorite_food
    # Generates setters
    attr_writer :name, :age, :favorite_food
    # Generates both in one line
    attr_accessor :name, :age, :favorite_food

    def speak
        return "Hello"
    end
end

hobbit = Person.new
hobbit.name = "Frodo"
hobbit.age = 30
hobbit.favorite_food = "Elven bread"
puts hobbit.speak
```

### Inheritance

[Definition]()

Example:

```rb
class Hobbit < Person
    def speak
        return "Hello, I'm a hobbit!"
    end
end

hobbit2 = Hobbit.new
hobbit2.name = "Sam"
hobbit2.age = 30
hobbit2.favorite_food = "potatoes"
puts hobbit2.speak
```

### Polymorphism

[Definition](#)

Example:

```rb
class Ninja
    def rank(ninja)
        ninja.rank
    end
end

class Jonin < Ninja
    def rank
        puts "Jonin"
    end
end

class Chunin < Ninja
    def rank
        puts "Chunin"
    end
end

ninja = Ninja.new
ninja.rank(Jonin.new) # Jonin
ninja.rank(Chunin.new) # Chunin
```

### Modules

Interfaces?

Modules are made of methods and instance variables like classes but can't be instantiated
into an object:

```rb
# human.rb
module Human
    attr_accessor :name, :height, :weight

    def run
        puts self.name + " runs"
    end
end

# smart.rb
module Smart
    def act_smart
        return "E=MC^2"
    end
end

# main.rb

# Must be in the same directory
require_relative "human"
require_relative "smart"

class Scientist
    include Human
    # Using prepend will prevent overriding the module function.
    prepend Smart

    def act_smart
        return "To be or not to be"
    end
end

person = Scientist.new
person.name = "Einstein"
person.run
puts person.act_smart # E=MC^2


# Modules can also be defined here, but having their own file keeps things organized.
module Animal
    def make_sound
        puts "Woof!"
    end
end

class Dog
    include Animal
end

snoopy = Dog.new
snoopy.make_sound
```

### Built-In Modules

Ruby has some built-in modules. The Enumerable module lets a class
take advantage of collection properties.

Enumerable class example:

```rb
class Menu
    include Enumerable

    # Required by the Enumerable module
    def each
        yield "Pizza"
        yield "Spaghetti"
        yield "Salad"
        yield "Water"
        yield "Bread"
    end
end

menu_options = Menu.new

# Looping through the collection.
menu_options.each do |item|
    puts "Would you like #{item}?"
end
menu_options.reverse_each do |item|
    puts item
end

p menu_options.find {|item| item = "Pizza"}
p menu_options.select {|item| item.size <= 5 } # Get items that meet the criteria
p menu_options.reject {|item| item.size <= 5 } # Get items that don't meet the criteria
p menu_options.first # Prints the first item
p menu_options.take(2) # Prints the first two items
p menu_options.drop(2) # Prints everything but the first two items
p menu_options.min # Grabs "minimum" item
p menu_options.max # Grabs "maximum" item
p menu_options.sort # Grabs sorted version of the collection
```

## Language Specifics

## Libraries & Frameworks
