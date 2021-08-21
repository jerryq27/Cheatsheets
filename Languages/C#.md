# C\#

C# is an Object Oriented language developed by Microsoft.

[Checkpoint](https://youtu.be/lisiwUZJXqQ?t=1213)

## Basics

Comments:

```c#
namespace Example
{
    class Main
    {
        /*
         * Multiline Comment
         */
        static void Main(string[] args)
        {
            // Single-line Comment
        }
    }
}

```

### Operators

Basic arithmetic operators: `+ - * / %`

Other supported operators: `++ -- += -= *= /= %=`

Mathematical Functions:

```c#
namespace Example
{
    class Main
    {
        static void Main(string[] args)
        {
            Math.Abs();
            Math.Ceiling();
            Math.Floor();
            Math.Max();
            Math.Min();
            Math.Pow();
            Math.Round();
            Math.Sqrt();

            // Generates a random number from 1-10.
            Random rand = new Random();
            Console.WriteLine(rand.Next(1, 11));
        }
    }
}
```

## Variables

Data Types:

```c#
namespace Example
{
    class Main
    {
        static void Main(string[] args)
        {
            bool isValid = false;
            char grade = 'A';

            int number = int.MaxValue;
            long biggerNum = long.MaxValue;
            decimal evenBiggerNum = decimal.MaxValue;
            float floatNum = float.MaxValue;
            double biggerFloatNum = double.MaxValue;

            // Var data types are determined in compile time.
            var something = "This will be a string."
            something = 3; // Error! Once determined, it cannot be changed.
            Console.WriteLine("'something' is a {0}", something.GetTypeCode());

            // Casting is done with no issues when going from less data to more data.
            int intExample = int.MaxValue;
            long longExample = (long)intExample; // 2147483647

            // Issues arise when casting from more data to less.
            longExample = long.MaxValue;
            intExample = (int)longExample; // -1
        }
    }
}
```

## Conditionals

Syntax:

```c#
static void Main(string[] args) 
{
    if(condition) {
        // code
    }
    else if(condition) {
        // code
    }
    else {
        // code
    }
}
```

Conditional operators: `== != < > <= >= && || ! ^`

Switch syntax:

```c#
static void Main(string[] args) 
{
    switch(variable) {
        case 0:
            // code
            break;
        case 1:
            // code
            break;
        case 2:
            // goto Section;
            break;
        default:
            // default code
            break;
    }
}

// Section:
//     Console.WriteLine("goto example.");
```

## Collections

## Loops

While loop syntax:

```c#
while(condition) {
    // code
}
```

Do-While loop syntax:

```c#
do {
    // code
} while(condition);
```

For loop syntax:

```c#
for(int i = 0; i < 10; i++) {
    // code
}
```

Looping through an array:

```c#
// Normal array.
string str = "hello";
foreach(char c in str) {
    Console.WriteLine(C);
}

// Key-value pair array.
foreach($kvArray as $key => $val) {
    echo $key . ': ' . $val;
}
```

## I/O

Basic I/O:

```C#
namespace Example
{
    class Main
    {
        static void Main(string[] args)
        {
            Console.Write("Hello world!\n"); // No new line.
            Console.WriteLine("Hello World!"); // New line included.

            Console.Write("What is your name: ");
            string name = Console.ReadLine();
            Console.WriteLine("Hi " + name);
        }
    }
}
```

## Functions

## Exceptions

## Classes & Objects

## Language Specifics

## Libraries & Frameworks
