# PHP

PHP is primarily used to handle server-side backend functionality, but it
can be used wherever JavaScript is used.

## Basics

PHP code is written in HTML denoted by the PHP tags:

```php
<?php
    /* Write PHP code here. */
?>
```

Importing PHP code from other files:

```php
<?php
include 'OtherFile.php';

// code
?>
```

### Operators

Basic arithmetic operators: `+ - * / %`

Other supported operators: `++ -- += -= *= /= %=`

Mathematical Functions:

```php
<?php
    abs($num);
    ceil($num);
    floor($num);
    round($num);
    max($num1, $num2);
    min($num1, $num2);
    pow($num1, $num2);
    sqrt($num);
    exp($num);
    log($num);
    log10($num);
    pi(); 
    hypot($num1, $num2);
    deg2rad($num);
    rad2deg($num);
    rand($num1, $num2); // Original Random function
    mt_rand($num1, $num2); // Faster Random function?
    is_numeric($num);
    is_finite($num);
    is_infinite($num);
    sin($num);
?>
```

## Variables

Variables in PHP are [dynamically typed](../Languages/Languages.md#dynamically-typed) and always start with a `$` sign. The next
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
// Title Casing.
ucfirst($str);

// Substrings.
$substr = substr($str, $fromindex, $numofchars)
// Get index position of a sub string.
strpos($str, $substr);
// Replace substring.
str_replace($substr, $replaceStr, $str);

// String compare. neg: str1 < str2, 0: equal, pos: str1 > str2.
echo strcmp($str1, $str2);
// String compare ignore-case
echo strcasecmp($str1, $str2);

// Search, returns the search and all characters after.
echo strstr($str, $search);
// Ignore-case search.
echo stristr($str, $search);

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
$letters = ['a', 'b', 'c', 'd'];

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

Array functions:

```php
<?php
    // Get the size of the array.
    count($arr);
    // Create array based on a number range.
    range($num1, $num2); 
    // Sorting an array.
    sort($arr); // Optional second parameter: SORT_NUMERIC, SORT_STRING(default?)
    // Sorts array with keys (by value?).
    asort($arr);
    // Sorts array by keys.
    ksort($arr);
    // Reverse versions of each sort.
    rsort();
    rasort(); // arsort();?
    rksort(); // krsort();?

    // Check for existence.
    in_array($val, $array);

    // Apply function to every item.
    $results = array_map('function_name', $arr);
    // Other list functions
    array_reduce($arr, 'function_name', $startVal);
    array_filter($arr, 'function_name');
?>
```

> Note: Arrays can be compared using the `== === != !==` comparison operators.

## Loops

While loop syntax:

```php
while($condition) {
    // code
}
```

Do-While loop syntax:

```php
do {
    // code
} while($condition);
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

Basic output:

```php
<?php
    // Basic print statement.
    echo "<p>Hello world!</p>";

    // Formatted print statement.
    printf('Values is %s number is %d pi is %.2f', $str, $num, $pi);
    // With double quotes, echo can also print variables like this.
    echo "Value is $str number is $num pi is $pi";

    // Number formatting. 
    echo number_format(1234.56789, 2); // 1234.57
?>
```

Reading input from a POST form:

```php
<?php
    // email is the HTML form input element with the name 'email'.
    if(isset($_POST["email"])) {
        // INPUT_POST = $_POST constant?
        if(filter_input(INPUT_POST, "email", FILTER_VALIDATE_EMAIL)) {
            echo "Valid email."
        }
        else {
            echo "Invalid email."
        }
    }
?>
```

Working with HTML input:

```php
<?php
    $html = '<a href="#">Dead link</a>';
    echo htmlspecialchars($html); // <a href="#">Dead link</a>
    echo strip_tags($html); // Dead link
    echo strip_tags($html, '<a>'); // <a href="#">Dead link</a>
?>
```

### Database I/O

Connecting to a database:

```php
<?php
define('USER', 'testuser');
define('PASSWORD', 'password1');

$dbstr = 'mysql:host=localhost;dbname=testdb';
try {
    $db = new PDO($dbstr, USER, PASSWORD);
}
catch(PDOException $e) {
    echo 'Error' . $e->getMessage();
    exit();
}


// INside HTML file
require('db_connect.php');
$query = 'SELECT * FROM test ORDER BY id';

$command = $db->prepare($query);
$command->execute();
$data = $command->fetchAll();
$command->closeCursor();

foreach($data as $item) {
    echo "<tr>$item</tr></br>";
    echo $item['id'];
}
?>
```

### Cookies

Cookies allow you to store values in the user's browser.

```php
<?php

    setCookie('my_cookie', 'value_name', 5, '/');

    if(!isset($_COOKIE['my_cookie'])) {
        echo 'Cookie not set <br>';
    }
    else {
        echo 'Cookie value: ' . $_COOKIE['my_cookie'] . '<br>';
    }
?>
```

> Note: Cookies aren't always going to be enabled, so it's a good idea to check before
using them.

## Functions

Syntax:

```php
<?php 
    function addNums($num1, $num2) {
        return $num1 + $num2;
    }

    echo '3 + 4 = ' . addNums(3, 4);

    // Default arguments.
    function addNumsDef($num1=3, $num2=4) {
        return $num1 + $num2;
    }
    echo addNumsDef(); // 7
?>
```

Passing a variable number of arguments:

```php
<?php
    function getSum(...$nums) {
        $sum = 0;
        foreach($nums as $num) {
            $sum += $num;
        }
        return $sum;
    }

    echo "Sum = " . getSum(1,2,3,4,5); // 15
?>
```

Returning a variable number of values:

```php
<?php
    function returnMultiple($x, $y) {
        return array(
            $x + $y,
            $x - $y
        );
    }

    list($sum, $diff) = returnMultiple(1, 2);
    echo "Sum=$sum\nDiff=$dif";
?>
```

By default, arguments are passed into functions by value. Arguments
can also be passed by reference:

```php
function changeValbyRef(&$valueToChange) {
    $valueToChange = 10;
}

$val = 5;
changeValByRef($val);
echo $val; // 10
```

### Builtin Functions

PHP has some built in functions that provide a lot of utility:

```php
<?
exit(); // Kills the PHP script.

// Sets the date format.
date_default_timezone_set('UTC');

echo date('h:i:s:u a, l F jS Y e'); // 04:09:10000000 pm, Saturday August 9th 2014 UTC
?>
```

## Exceptions

Syntax:

```php
<?php
    function zeroDivide($num) {
        if($num == 0) {
            throw new Exception("Can't divide by zero.");
        }
        return $calc = 100/$num;
    }

    try {
        zeroDivide(0);
    } catch(Exception $e) {
        echo "Exception: " . $e->getMessge();
    }
?>
```

## Classes & Objects

Sample class:

```php
<?php
class Animal {
    // Class fields.
    protected $name;
    protected $favorite_food;
    protected $sound;
    protected $id;

    // Static field.
    public static $number_of_animals = 0;

    // Constant field.
    const PI = '3.14';

    // Constructor.
    function __construct() {
        $this->id = rand(100, 1000000);
        echo $this->id . " has been assigned.<br>";

        Animal::$number_of_animals++;
    }

    // Class method.
    function what_am_i() {
        return "I'm an animal.<br>"
    }

    // 'Magic' Getters/Setters
    function __get($name) {
        echo "Asking for name value."
        return $this->name;
    }

    function __set($name, $value) {
        switch($name) {
            case "name":
                $this->name = $value;
                break;
            case "favorite_food":
                $this->favorite_food = $value;
                break;
            case "sound":
                $this->sound = $value;
                break;
            default:
                echo $name . " not found.<br>"
        }
        echo "Set " . $name . " to " . $value . ".<br>";
    }

    // Final functions.
    final function cant_override() {
        echo "I can't be overriden."
    }

    // toString function.
    function __toString() {
        return "Name $this->name<br>";
    }

    // Destructor.
    public function __destruct() {
        echo $this->name . " is being destroyed.<br>";
    }
}


$animal1 = new Animal();

// Calls the __set() magic method.
$animal1->name = "Spot";
$animal1->favorite_food = "Meat";
$animal1->sound = "Woof";

// Calls the __get() magic method.
echo $animal1->name;

// Calls a class method.
echo $animal1->what_am_i();

// Calls a static method.
echo Animal::number_of_animals;

// Calls the __toString() method.
echo $animal1;
?>
```

### Inheritance

Child class sample:

```php
<?php
class Dog extends Animal {

    // Override parent class method.
    function what_am_i() {
        return "I'm a dog.<br>"
    }
}

$animal2 = new Dog();
$animal2->name = "Grover";
$animal2->favorite_food = "Mushrooms";
$animal2->sound = "Ruff";

echo $animal2->name;
echo $animal2->what_am_i();
echo Dog::number_of_animals;
echo $animal2;

// Check inheritance.
echo $animal2 instanceof Animal? "True" : "False";
?>
```

### Interfaces

Like other languages, you can't extend multiple classes, but you can implement multiple
interfaces.

Interface syntax:

```php
<?php
interface Singable {
    // MUST override this method.
    public function sing();
}

class Bird extends Animal implements Singable {
    
    public function sing() {
        echo "Tweet!<br>";
    }

}

// Works for any animal who implements the Singable interface.
function sing(Singable $singing_animal) {
    $singing_animal->sing();
}
?>
```

## Language Specifics

## Libraries & Frameworks
