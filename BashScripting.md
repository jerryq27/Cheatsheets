# Bash Scripting

Bash Scripting is a way to write scripts used in a Linux environment.

## Basics

All scripts should begin with `#!/bin/bash`, this tells the system which program will execute the script.

Flipping the executable bit allows a script to be ran with `./`.

**'STRING'** - raw string, all special characters lose meaning.

> Escaped a single quote within single quotes with `\'`.

**"STRING"** - string, special characters like **$**, backquotes, and **\\** escapes all retain their meaning.

## Variables

Setting variables:

* `VAR=<VALUE>` - sets a value.
* `unset $VAR` - unsets a value.
* `read VAR` - reads user input into a variable.
* `$(EXPRESSION)` - captures output of command into a variable.

> You can also surround the expression with backticks.

Reading variables:

* `echo $VAR` - prints out the variable's contents.

### System Variables

* **$\[0-9\]** - Get command line arguments, **0** is the script name.
* **$#** - Get the number of arguments.
* **$*** - Gets all arguments as a single quoted value.
* **$@** - Gets all the arguments as a list of quoted values.
* **$$** - The process ID of the current shell in which the script is running.
* **$!** - The process ID of the last executed background task (i.e. with the **&** argument).

## Conditionals

Syntax:

> [ ] is technically calling a _test_ program and passes the arguments to it.

```bash
# if/else
if [ $1 == $2 ]
    then # if condition.
elif [ $1 != $2 ]
    then # else if condition.
else
    # else condition.
fi # Marks the end of a conditional

# Switch
x=7
case $x in
    1) echo 'Lonely 1..'
    ;;
    3) echo 'Magic 3!'
    ;;
    7) echo 'Lucky 7 :D'
    ;;
esac
```

> Strings can also be compared with the == and != operators.

Supports regular conditional operators.
Also supports these _relational operators_ for numbers:

* **-eq** - equals.
* **-ne** - not equals.
* **-gt** - greater than.
* **-lt** - less than.
* **-ge** - greater than or equal to.
* **-le** - less than or equal to.

### String Conditional Flags

* **-z** - Checks if the size of the string is zero.
* **-n** - Checks if the size of the string is not zero.

> [ $STRING ] returns false if the string is empty.

### File Conditional Flags

* `[ -d $FILE ]` - Checks if the argument is a directory.
* **-f** - Checks if the argument is a file.
* **-r** - Checks if the file is readable.
* **-w** - Checks if the file is writable.
* **-x** - Checks if the file is executable.
* **-s** - Checks if the file size is greater than zero.
* **-e** - Checks if the file exists.

## Loops

Sytax:

```bash
# While loop
i=1
while [ $i -le 10 ]
    do echo $i
    i=$(expr $i + 1)
done

# Until loop
i=1
until [ $i -gt 10 ]
    do echo $i
    i=$(expr $i + 1)
done

# For loop
for i in {1..10}
    do echo $i
done
```

## File I/O

Operators

* `$EXPRESSION > $FILE` - Overwrites the file with the command output.
* `$EXPRESSION >> $FILE` - Appends command output to the file.
* `$EXPRESSION < $FILE` - Provides file contents as input to the command.

## Functions

Syntax:

```bash
# No argument function.
hello() {
    echo 'Hello, world!'
}

hello

# Function with arguments.
greet() {
    echo "Hello $1!"
}
greet Jerry

# Function with a return.
sum() {
    s=$(expr 2 + 2)
    return $s
}
sum
SUM=$?

```

> Note, no parenthesis in a function call.

* `unset -f $FUNCTION_NAME` - unsets a function
