#!/bin/bash # Should always be the first line, this tells the system which shell to run when using `./`
#### NOTE ####
# Spacing is important!
# Single and double quotes are weird!
# Conditionals are inside '[]', '[[]]', and '(())'.
# ';' are like line breaks.
# Lists seem to use '{}'.
# 'break' and 'continue' are valid keywords.

#### BASICS ####
unset VAR # Removes a variable?
unset -f function_name # Removes a function.

## Variable manipulating operators. (Seems to only work with a statement, not by itself)
${VAR} # Substitues in the value of VAR, same as $VAR.
${VAR:-"VAL"} # If VAR is null or unset, VAL is substituted in, VAR does not change.
${VAR:="VAL"} # If VAL is null or unset, VAR is set to the value of VAL.
${VAR:?"message"} # If VAR is null or unset, a message is printed to STDERR.
${VAR:+"VAL"} # If VAR is set, VAL is substituted in for VAR, VAR does not change.

## Quotes.
'' # Single quotes are basically a raw string, all special characters lose meaning.
# Escaped a single quote within single quotes with \'.
"" # Most characters lose their meaning. '$', backquotes, and '\' escapes all have meaning.

#### CONDITIONALS ####

## Boolean operators.
[ ! true ] # Not
-o # Logical OR
-a # logical AND

## File operators.
# Other
-b # Checks if the file is a special 'block' file.
-c # Checks if the file is a special 'character' file.
-g # Checks if the file has its set group ID (SGID) bit set.
-k # Checks if the file has its 'sticky' bit set.
-p # Checks if file is a 'named pipe'.
-t # Checks if file descriptor is open and associated with a terminal.
-u # Checks if the set user ID (SUID) bit is set.

# Other syntax and rules.
[] # Calls a program 'test' and passes arguments to it. So commands interpreted by bash cannot be used here.
# Relational operators (Numbers only), '==' and '!=' (Both Strings/numbers).
# Can use the boolean operators, but cannot use '&&' and '||'.
[[ ]] # String-centered comparator syntax interpreted by bash. (File names, regex, etc.)
# You can use '==', '!=', '<', '>', '&&', '||'
(( )) # Arithmetic-centered syntax interpreted by bash. Mostly used for numeric conditionals and writing math.
# You can also use conditionals with math. '!='. '==', '<=', '>=', '<', and '>'. true retuns 1 and false is 0.
# If an expression is used as a conditional, non-zero values are true and zero is false.
# Use $(( )) to capture the result of an expression.

#### ARRAYS ####
# Array declaration syntax.
ARRAY1=( 1 2 3 4 5 )

ARRAY2[0]=1
ARRAY2[1]=2
ARRAY2[2]=3
ARRAY2[3]=4
ARRAY2[4]=5

# Printing an array brackets and */@ required.
echo ${ARRAY1[*]}

# Looping over an array syntax.
for i in ${ARRAY1[*]}; do echo $i; done

#### SHELL OUTPUT/INPUT REDIRECTS ####
$COMMAND > $FILE # Redirects the commands output to a file instead of the terminal.
> # Overwrites a file.
>> # Appends to a file.
$COMMAND < $FILE # Redirects the command input from a file instead of the terminal.
< # Reads everything as input.
# Command keeps accepting input until a specified delimiter is found.
$COMMAND <\< DELIMITER

## Discarding output.
# To discard the output of a command, redirect it to /dev/null.
$COMMAND > /dev/null # /dev/null is a special file that automatically disards all input.
# To discard output and error output of a command, redirect STDERR to STDOUT.
$COMMAND > /dev/null 2 >& 1 # 2 is STDERR and 1 is STDOUT.
$COMMAND > /dev/null 1 >& 2 # Displays a message to STDERR from STDOUT.
$1 >& $2 # Merges output from $1 with $2.
$1 <& $2 # Merges input from $1 with $2.
$1 | $2 # Redirects output of $1 to the input of $2.
## File descriptors
# 0 = STDIN
# 1 = STDOUT
# 2 = STDERR
