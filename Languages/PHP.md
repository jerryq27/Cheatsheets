# PHP

PHP is primarily used to handle server-side backend functionality, but it
can be used wherever JavaScript is used.

## Basics

PHP code is written in HTML denoted by the PHP tags:

```php
<?php
    /* Write PHP code here. */

    // Basic print statement.
    echo "<p>Hello world!</p>";

    // Fromatted print statement.
    printf('Values is %s number is %d pi is %.2f', $str, $num, $pi);
    // Echo can also print variables like this.
    echo 'Value is $str number is $num pi is $pi';
?>
```

### Operators

Basic arithmetic operators: `+ - * / %`

Other supported operators: `++ -- += -= *= /= %=`

## Variables

Variables in PHP are loosely typed and always start with a `$` sign. The next
character must be a letter, then you can use other characters.

```php
$number = 7;
// Single and double quotes supported for strings.
$name = 'Jerry';

// Multiline string, EOS can be anything, it's used to mark the end of the
// string.
$longString = <<<EOS
This is a really long
string that spans over
multiple lines.
EOS;

// Constants
define('PI', 3.14);
echo PI;
```

You can also refer to variables by reference using `&`:

```php
$num = 10;
$numRef = &$num;

$num++;

echo $numRef; // 11
```

String functions:

```php
// Get the length of a string.
strlen($str);

// Trimming white space.
ltrim($str);
rtrim($str);
trim($str);

// Change string case.
strtoupeer($str);
strtolower($str);

// Substrings.
$substr = substr($str, $fromindex, $numofchars)

// String compare. neg: str1 < str2, 0: equal, pos: str1 > str2.
echo strcmp($str1, $str2);
// String compare ignore-case
echo strcasecmp($str1, $str2);

// Search, returns the search and all characters after.
echo strstr($str, $search);
// Ignore-case search.
echo stristr($str, $search);

// Get index position of a search.
strpos($str, $search);

// Replace substring.
str_replace($search, $replaceStr, $str);

// Converting string to array.
$arr = explode($delimiter, $str, $OPT_ARRAY_SIZE);

// Converting array to string.
$str = implode($delimiter, $arr);
```

## Conditionals

Syntax:

```php
if($condition) {
    // code
}
elseif($condition) {
    // code
}
else {
    // code
}
```

Conditional operators: `== === !== < > <= >= && || !`

Switch syntax:

```php
switch($value) {
    case "string1":
        echo "1";
        break;
    case "string2":
        echo "2";
        break;
    default:
        // Executes if no other cases are met.
        echo "Not a string.";
}
```

Ternary Operator:

```php
($condition) ? $trueVal : $falseVal;
```

## Collections

Array syntax:

```php
$names = array('Jim', 'Sally', 'Fred');

echo $names[1]; // Sally

// Append to an array.
$names[4] = 'Steve';

// Combining arrays.
$arr1 = $arr1 + $arr2;

// Multidimensional arrays.
$twoDArray = array(
    array('str1', 1),
    array('str2', 2),
    array('str3', 3)
);
```

Key-value pair array syntax (by default an array key would be the index):

```php
$kvPairArray = array('Name'=>'Jerry', 'food'=>'cookies', 'num'=>7);

echo $kvPairArray['food']; // cookies
```

> Note: Arrays can be compared using the `== === != !==` comparison operators.

## Loops

While loop syntax:

```php
while($condition) {
    // code
}
```

For loop syntax:

```php
for($value = 1; $value < 10; $value++) {
    // code
}
```

Looping through an array:

```php
// Normal array.
foreach($array as $val) {
    echo $val;
}

// Key-value pair array.
foreach($kvArray as $key => $val) {
    echo $key . ': ' . $val;
}
```

## I/O

## Functions

Syntax:

```php
function addNums($num1, $num2) {
    return $num1 + $num2;
}

echo '3 + 4 = ' . addNums(3, 4);
```

### Builtin Functions

PHP has some built in functions that provide a lot of utility:

```php
<?
exit(); // Kills the PHP script.

// Sorting an array.
sort($arr); // Optional second parameter: SORT_NUMERIC, SORT_STRING(default?)
// Sorts array with keys (by value?).
asort($arr);
// Sorts array by keys.
ksort($arr);
// Reverse versions of each sort.
rsort();
rasort();
rksort();

// Sets the date format.
date_default_timezone_set('UTC');

echo date('h:i:s:u a, l F jS Y e'); // 04:09:10000000 pm, Saturday August 9th 2014 UTC
?>
```

## Exceptions

## Classes & Objects

## Language Specifics

## Libraries & Frameworks
